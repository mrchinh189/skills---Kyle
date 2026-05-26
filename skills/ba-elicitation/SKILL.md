---
name: ba-elicitation
description: "Plan and run business-requirements elicitation — interviews, workshops, questionnaires, observation, and document analysis — then capture and classify the raw requirements that come out. Use this skill whenever a business analyst needs to prepare to talk to stakeholders or make sense of what they said: preparing interview guides or workshop agendas, drafting discovery questions, running a requirements workshop, writing up interview notes, or turning a messy conversation into a clean, classified requirements list. Trigger on phrases like 'phỏng vấn stakeholder', 'workshop lấy yêu cầu', 'discovery questions', 'elicit requirements', 'biên bản phỏng vấn', or whenever requirements are still vague and need to be drawn out before any spec can be written."
license: Complete terms in LICENSE.txt
---

# BA Elicitation

Elicitation is where requirements *come from*. Do it well and everything downstream (specs,
stories, tests) gets easier; do it badly and the whole project inherits the gaps. The job of this
skill is to help you **prepare** a high-signal session, **run** it, and **capture** the output in a
form the next stage can use.

The deep principle: stakeholders rarely hand you requirements. They describe symptoms, habits, and
frustrations. Your job is to draw out the underlying *need* behind what they say — and to separate
what they want (a solution they imagined) from what they actually need (the problem to solve).

## Choose the technique first

Different situations call for different techniques. Pick deliberately rather than defaulting to "a
meeting".

| Situation | Best technique | Why |
|---|---|---|
| Deep understanding of one role's work | 1:1 interview | Safe space, can probe pain points |
| Conflicting views must be reconciled | Workshop | Surface and resolve disagreement live |
| Many people, little time | Questionnaire/survey | Breadth over depth |
| Stated process ≠ real process | Observation / shadowing | See what people actually do |
| A system/process already exists | Document & data analysis | Ground truth before asking opinions |

When the user hasn't said which, recommend one and explain the trade-off in a sentence.

## Workflow

### 1. Frame the session
Before writing any question, pin down: **who** you're talking to (role, not name), **why** (the
decision this informs), and **what's already known** (so you don't waste their time re-asking).
State these back to the user if they're missing.

### 2. Build the question set
Structure questions as a funnel: **context → current state → pain points → desired state →
constraints → edge cases**. Open-ended first ("walk me through how you..."), closed only to confirm
specifics ("does that always happen, or only month-end?"). Always leave room to probe: every pain
point deserves a "why does that happen?" follow-up.

For the full technique catalog, question banks, and a ready-to-use interview/workshop template, read
`references/techniques.md`.

### 3. Run / simulate the session
If the user wants a live agenda, produce a timeboxed one. If they're feeding you raw notes or a
transcript, move straight to capture.

### 4. Capture and classify
Turn raw input into a clean list. Classify every item so nothing is lost and the next stage can
sort fast:

- **Type**: business need · functional · non-functional · business rule · constraint · assumption
- **Source**: who said it (role)
- **Confidence**: confirmed · implied · to-verify
- **Open question**: anything that needs follow-up

Always end an elicitation write-up with an **Open Questions** list and a **Suggested next step**
(usually: which requirements are ready to spec, which need another round).

## Output format

Use this structure for an elicitation write-up:

```markdown
# Elicitation Summary — [topic]
**Session**: [interview/workshop] · **Participants**: [roles] · **Date**: [date]

## Context & goal
[1-2 sentences: what we set out to learn]

## Captured requirements
| ID | Statement | Type | Source | Confidence |
|----|-----------|------|--------|------------|
| E-01 | ... | functional | Warehouse lead | confirmed |

## Pain points & root causes
- [symptom] → [underlying cause]

## Open questions
- [ ] ...

## Suggested next step
[e.g., "E-01..E-06 ready for ba-requirements-spec; E-07 needs IT to verify"]
```

## Guardrails

- Don't invent stakeholder answers. If you're preparing a session, produce *questions*; if you're
  capturing, work only from what the user gave you and mark gaps as open questions.
- Separate problem from solution. When a stakeholder says "I need a button that…", record the
  underlying need too — the solution may change, the need won't.
- Keep the user in the loop on assumptions. Flag every inferred requirement as `implied` so a human
  confirms it before it hardens into a spec.
