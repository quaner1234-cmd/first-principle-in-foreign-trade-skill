# Changelog

## 1.4.6

- Aligned the public, cross-industry Skill with Project Edition 1.4.6 (2026-08-28)
- Added Product Reality Check / Domain Expert Lens for complex product, Tech Pack, material, component, and special-process decisions
- Added targeted Reality Benchmark: use mature comparable products, supplier technical documentation, standards/testing methods, and reliable industry guidance only when they can materially change the solution
- Added Preferred Candidate + Main Trade-off + Reality Verification as the default output of product/technical frame review
- Added Wide In → Narrow Out across judgment, customer communication, internal handoff, supplier/lab verification, and management escalation
- Standardized reality-owner handoff to one recommendation + 1–3 necessary reasons + 1–3 questions that would change the next step; multiple options only when real trade-offs require them
- Added explicit guardrails that public benchmark evidence is Reference/Candidate, not current-project Verified Input or company capability
- Expanded anti-hallucination rules from 35 to 37
- Kept Runtime schemas unchanged because 1.4.6 adds no new Mode, state field, approval gate, or machine-action contract

## 1.4.5

- Aligned the public, modular Skill with Project Edition 1.4.5 (2026-08-25)
- Added Decision Owner / Decision Barrier analysis and separated it from Current Key Uncertainty and Hard Blocker
- Added Sample Purpose Check for development, validation, and PP / production-intent samples
- Added Reply the Delta, Minimum Sufficient Reply, decision-first reply structure, and confirmation-without-restatement guidance
- Added explicit buyer country / region output for New Lead and Qualified Inquiry, with Fact / Inference / Unknown status
- Added Reply Asset Check and Available Asset Before Ask without assuming that assets exist
- Separated confirmed Hard Constraints from provisional price, lead-time, and other commercial variables
- Expanded anti-hallucination rules from 32 to 35
- Kept company-specific context out of the public repository; all company facts remain local
- Changed the repository license from Apache-2.0 to MIT for this and future versions; previously published versions remain available under their original license terms

## 1.4

- Aligned Skill content with ChatGPT Project Edition 1.4 (2026-08-13)
- Added Order Conversion / 大货推进 (Mode 11)
- Added Clarity → Commitment; Development ≠ Endless Development; Order Blocker ≠ Remaining Detail
- Added Validation + Conversion, Next Commitment Check, Commercial Commitment Ladder, Order Conversion Check
- Updated product development cadence to Diverge → Explore → Verify → Converge → Convert
- Expanded anti-hallucination rules to 32; added corresponding anti-patterns
- Updated SKILL, clarity-engine, decision-engine, output-contract, project-stage, cheatsheet, README

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
