import re

from .errors import DomainValidationError


PROBABILITY_PATTERN = re.compile(
    r"(?:成交概率|诚意|下单概率|likelihood|chance|probability)[^\n%]{0,24}\b\d{1,3}(?:\.\d+)?\s*%",
    re.IGNORECASE,
)


class DomainValidator:
    def validate_route(self, route):
        errors = []
        if route["primary_mode"] in route.get("secondary_modes", []):
            errors.append("primary_mode must not be repeated in secondary_modes")
        if route["requires_context_question"] and not route.get("context_question"):
            errors.append("requires_context_question=true requires one context_question")
        if not route["requires_context_question"] and route.get("context_question") is not None:
            errors.append("context_question must be null when it is not required")
        if route["buyer_identity_evidence"] == "insufficient" and route["due_diligence_strategy"] == "none":
            errors.append("insufficient identity evidence cannot use due_diligence_strategy=none")
        if errors:
            raise DomainValidationError(errors)
        return route

    def validate_turn(self, turn, routing, project, customer_reply_requested):
        errors = []
        if turn["status"] == "needs_tools":
            if turn["decision"] is not None:
                errors.append("needs_tools turn must not include a final decision")
            if not turn["tool_requests"]:
                errors.append("needs_tools turn requires at least one tool request")
        elif turn["status"] == "final":
            if turn["decision"] is None:
                errors.append("final turn requires a decision")
            if turn["tool_requests"]:
                errors.append("final turn must not include tool requests")

        call_ids = [item["call_id"] for item in turn["tool_requests"]]
        if len(call_ids) != len(set(call_ids)):
            errors.append("tool call ids must be unique within a turn")

        if turn["decision"] is not None:
            errors.extend(
                self._decision_errors(turn["decision"], routing, project, customer_reply_requested)
            )
        if errors:
            raise DomainValidationError(errors)
        return turn

    def _decision_errors(self, decision, routing, project, customer_reply_requested):
        errors = []
        if routing["project_stage"] != "unknown" and decision["project_stage"] != routing["project_stage"]:
            errors.append("decision project_stage must match the routed stage")
        if decision["primary_mode"] != routing["primary_mode"]:
            errors.append("decision primary_mode must match the routed primary_mode")

        hard_blockers = []
        for index, unknown in enumerate(decision["unknowns"]):
            if unknown["blocker_status"] == "hard_blocking":
                hard_blockers.append(unknown)
                if unknown["resolution_path"] != "no_path":
                    errors.append(
                        "unknowns[{}]: hard_blocking requires resolution_path=no_path".format(index)
                    )
                if unknown["low_cost_path"]:
                    errors.append("unknowns[{}]: hard_blocking cannot have a low-cost path".format(index))
        if decision["disposition"] == "stop" and not hard_blockers:
            errors.append("disposition=stop requires at least one current hard blocker")
        if decision["disposition"] == "stop" and not decision["stop_conditions"]:
            errors.append("disposition=stop requires explicit stop conditions")

        for group_name in ("next_actions", "parallel_actions"):
            for index, action in enumerate(decision[group_name]):
                if action["risk"] in ("write", "external"):
                    if not action["approval_required"]:
                        errors.append(
                            "{}[{}]: write/external actions require human approval".format(group_name, index)
                        )
                    if not action["idempotency_key"]:
                        errors.append(
                            "{}[{}]: write/external actions require an idempotency_key".format(group_name, index)
                        )

        reply = decision.get("customer_reply")
        if reply is not None and not customer_reply_requested:
            errors.append("customer_reply was generated without explicit user request")
        if reply is not None and reply.get("requires_approval") is not True:
            errors.append("customer_reply must require approval")

        allowed_sources = set()
        for fact in project.get("facts", []):
            if fact.get("source_ref"):
                allowed_sources.add(fact["source_ref"])
        for fact in decision["facts"]:
            allowed_sources.add(fact["source_ref"])
        for inference_index, inference in enumerate(decision["inferences"]):
            for source_ref in inference["basis_source_refs"]:
                if source_ref not in allowed_sources:
                    errors.append(
                        "inferences[{}]: unknown basis source_ref {!r}".format(inference_index, source_ref)
                    )
        for commitment_index, commitment in enumerate(decision["can_say"]):
            for source_ref in commitment["source_refs"]:
                if source_ref not in allowed_sources:
                    errors.append(
                        "can_say[{}]: unknown source_ref {!r}".format(commitment_index, source_ref)
                    )

        can_say = {self._normalize(item["claim"]) for item in decision["can_say"]}
        cannot = {self._normalize(item) for item in decision["cannot_promise"]}
        overlap = can_say.intersection(cannot)
        if overlap:
            errors.append("the same claim cannot appear in can_say and cannot_promise")

        text_fields = [decision["summary"]]
        text_fields.extend(item["claim"] for item in decision["inferences"])
        for value in text_fields:
            if PROBABILITY_PATTERN.search(value):
                errors.append("precise deal/intention probabilities are not allowed")
                break

        if routing.get("requires_context_question") and decision["disposition"] != "need_context":
            errors.append("missing material context requires disposition=need_context")
        return errors

    @staticmethod
    def _normalize(value):
        return re.sub(r"\s+", "", value).casefold()
