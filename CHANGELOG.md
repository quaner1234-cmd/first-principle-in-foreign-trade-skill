# Changelog

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
