# Changelog

## 1.3.1

- Aligned Skill content with ChatGPT Project Edition 1.3.1 (2026-08-10)
- Added Progressive Specification: Unknown → Public Reference → Candidate Range → Working Assumption → Verified Input → Final Specification
- Added Reference ≠ Specification; Decision Ownership ≠ Information Generation; Tool-before-Question
- Added Responsibility Boundary (Can Do / Assist / Coordinate / Cannot Commit Yet) with Internal ≠ External Disclosure
- Added Development Prototype ≠ Final/Validation Sample; safety-critical Reference still allowed for research
- Added Natural Customer Communication + Reply Gate (`references/customer-reply.md`)
- Added Staged Commitment and Execution Friction / Transaction Node Check
- Expanded anti-hallucination rules to 28; updated SKILL, clarity-engine, decision-engine, output-contract, cheatsheet, README

## 0.4.0

- Added a dependency-free Python 3.9+ Runtime Harness around the Trade Judgment policy
- Added durable project/run state, atomic checkpoints, file locks, and resumable runs
- Added strict JSON Schemas for routing, agent turns, project state, run state, and manual tool results
- Added domain validators for sources, customer-reply authorization, action approvals, idempotency keys, and Hard Blocker semantics
- Added allow/manual/approval/deny tool policy with sandboxed read/search tools and an approval-gated local note tool
- Disabled external message sending in code by default
- Added hash-chained audit events without raw business content by default
- Added OpenAI-compatible, command, and deterministic replay providers
- Split unknown resolution path from independent blocker status; Hard Stop is a disposition result, not an unknown source category
- Changed review learning into a candidate-rule → regression → human approval → policy release flow
- Added runtime CLI, local replay example, Chinese usage guide, and automated regression tests

## 0.3.0

- Added Clarity Engine (`references/clarity-engine.md`): Clarity before closure; Unknown ≠ Blocker; promise boundary ≠ exploration boundary
- Unknown classification with solve-path before waiting
- Conversation momentum (Positive / Weak / Negative); default to progressive clarification while buyer engages
- Replaced “biggest blocker first” bias with **current key uncertainty** + Hard Blocker check + parallel advance tracks
- Research may diverge; judgment must converge; customer communication keeps only next-step information
- Method transfers across projects; answers do not; working hypotheses can be overturned by reality / review
- Mode 10 review cards can record method corrections into patterns
- Updated SKILL, decision engine, output contract, Mode 1, cheatsheet, golden examples

## 0.2.0

- Added project-stage detection (New Lead / Qualified Inquiry / Active Project / Re-engagement) before mode routing
- Added auto due-diligence evidence layer (`references/auto-due-diligence.md`); trigger on Buyer Identity Evidence gap, not only “new inquiry”
- Stage-aware background-check strategy (Quick / Deep / reuse / incremental)
- Output contract now includes project stage + external background facts block
- Low-friction rule: never ask the user to label stage if evidence allows inference; if prior thread is missing, ask only one context question
- Updated decision engine, Mode 1 / Mode 3, cheatsheet, and golden examples

## 0.1.0

- Initial book-to-skill extraction from 《让客户敢下单》 judgment framework
- Added Company Context template and local-context privacy boundary
- Added unified decision engine across 10 task modes
- Added Action Mode (default) and Learning Mode
- Added reality-verification ownership
- Added commitment guardrails
- Added customer-reply workflow (on request)
- Added technical hypothesis workflow
- Added golden examples and public desensitized examples
- Prepared repository for public GitHub release
- Adopted Apache License 2.0
