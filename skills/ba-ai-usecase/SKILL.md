---
name: ba-ai-usecase
description: "Assess whether a business process is a good candidate for AI / Agentic AI automation, and shape it into a responsible, scoped proposal — value-vs-feasibility scoring, data readiness, human-in-the-loop design, risk and failure-mode analysis, success metrics, and an MVP scope. Use this skill whenever a business analyst is evaluating AI/automation opportunities: deciding if a workflow should use an LLM or agent, sizing the ROI and feasibility, checking if the data is ready, designing where humans stay in the loop, or assessing the risks of an AI feature. Trigger on 'use case AI', 'đánh giá AI', 'tự động hoá bằng AI', 'agentic AI', 'có nên dùng AI', 'AI feasibility', 'ROI AI', 'human-in-the-loop', 'AI risk', 'automate with LLM', or any request to judge or scope an AI/automation opportunity for an enterprise. Complements the requirements lifecycle skills (elicitation, process-modeling, requirements-spec)."
license: Complete terms in LICENSE.txt
---

# BA for AI / Agentic AI Use Cases

The most valuable thing an AI-focused BA does is say **"not this one"** to the wrong use cases and
**"here's exactly how"** for the right ones. Enthusiasm is cheap; this skill brings discipline:
assess fit honestly, scope responsibly, and design for the reality that AI is probabilistic — it will
sometimes be wrong, and the design must account for that.

The mental model: AI doesn't replace a process, it **changes who/what does each step and how errors
are caught**. So always start from the process (ideally an AS-IS from `ba-process-modeling`), then
ask where AI genuinely helps.

## 1. Is this even an AI problem? (fit screen)

Many "AI" requests are better solved by plain automation, a rule, or a form fix. Screen first:

| Signal it's a good AI/LLM fit | Signal it is NOT (use rules/RPA/plain code) |
|---|---|
| Unstructured input (text, docs, images) | Fully structured, deterministic data |
| Fuzzy judgment, many edge cases | Fixed rules with clear right answers |
| Language understanding/generation needed | Simple lookups, calculations, transfers |
| Volume too high for humans, too varied for rules | Low volume, or rules already work |
| Tolerable, recoverable error cost | Zero-error-tolerance with no review possible |

If a deterministic solution works, recommend it — it's cheaper, faster, and auditable. Don't use AI
to look modern.

## 2. Value vs. feasibility scoring

Score the opportunity on two axes to prioritize. Read `references/assessment-frameworks.md` for the
detailed scoring rubric, ROI model, and a portfolio (value × feasibility) chart pattern.

- **Value**: time saved, error reduction, revenue/cost impact, risk reduction, experience uplift.
  Quantify wherever possible ("2h/day × 5 clerks", "5% → <1% error").
- **Feasibility**: data readiness, task complexity, integration effort, error tolerance, change-mgmt
  difficulty.

High value + high feasibility = do now. High value + low feasibility = invest to enable. Low value =
decline regardless of how interesting it is.

## 3. Data readiness (the usual blocker)

AI is only as good as the data it sees. Check, honestly:
- **Availability**: does the needed data exist and is it accessible?
- **Quality**: complete, accurate, consistent, current?
- **Volume & coverage**: enough examples, including the edge cases?
- **Access & governance**: PII? consent? regulatory limits on use?
- **Ground truth**: is there a way to know the right answer to measure against?

A use case with weak data readiness is a *data project first, AI project second* — say so plainly.

## 4. Human-in-the-loop (HITL) design

Because AI is probabilistic, decide deliberately where humans stay involved. Match oversight to the
cost of being wrong:

| Pattern | When | Example |
|---|---|---|
| **Human in the loop** (AI proposes, human approves each) | High-stakes, low error tolerance | AI drafts a contract clause; lawyer approves |
| **Human on the loop** (AI acts, human monitors & can intervene) | Medium stakes, high volume | AI triages tickets; supervisor watches a queue |
| **Human out of the loop** (AI acts autonomously, audited) | Low stakes, recoverable, well-bounded | AI tags emails by topic |

For **agentic** use cases (the AI takes multi-step actions with tools), be stricter: define the
allowed actions, the boundaries (what it must never do), approval gates for irreversible steps, and an
audit trail. Autonomy scales with reversibility — the easier to undo, the more autonomy is safe.

## 5. Risk & failure-mode analysis

Name how it can go wrong and what catches each failure:

| Risk | Example | Mitigation |
|---|---|---|
| Wrong output (hallucination) | Fabricated figure in a report | grounding/citations, human review, confidence thresholds |
| Bias / unfairness | Skewed prioritization | representative data, fairness checks, human override |
| Privacy / leakage | PII in prompts/logs | redaction, access control, retention limits |
| Over-automation | acts where it shouldn't | clear boundaries, approval gates, kill switch |
| Adoption failure | users distrust/ignore it | involve users early, explainability, gradual rollout |

## 6. Success metrics & MVP scope

- **Metrics**: define before building — quality (accuracy/precision on a held-out set), business
  (time saved, error rate, throughput), and adoption (usage, override rate). The override rate is a
  great trust signal: high overrides = the AI isn't earning autonomy yet.
- **MVP**: smallest slice that proves value on a real, narrow case with humans in the loop. Resist
  boiling the ocean; an agent that does one workflow reliably beats one that does ten unreliably.

## Output format

```markdown
# AI Use-Case Assessment — [process]
## Recommendation: [Do now / Enable then do / Pilot / Decline] — [one-line why]
## Fit screen: [AI-suited? or better solved by rules/RPA — why]
## Value: [quantified] · Feasibility: [score + main constraint]
## Data readiness: [Ready / Gaps: ...]
## HITL design: [pattern + where humans gate]
## Top risks & mitigations: [table]
## Success metrics: [quality / business / adoption]
## MVP scope: [the narrow first slice] · Out of scope: [...]
```

## Guardrails

- Be willing to say no. Recommending against an AI use case (or for plain automation) is a feature,
  not a failure — it builds trust and saves money.
- Don't hand-wave data readiness or risk. These are where AI projects actually fail; a confident
  assessment that skips them is worse than useless.
- Scale autonomy with reversibility and oversight. Never propose autonomous action on
  high-stakes/irreversible steps without an approval gate and an audit trail.
- Quantify honestly. If value or feasibility is a guess, label it an assumption to be validated, not a
  fact.
