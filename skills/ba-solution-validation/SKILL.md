---
name: ba-solution-validation
description: "Prove that what was built matches what was asked for — requirements traceability matrices (RTM), UAT test scenarios and scripts, gap analysis, and acceptance/sign-off documents. Use this skill whenever a business analyst needs to validate or accept a solution before go-live: building a traceability matrix linking requirements to stories to tests, writing UAT scenarios, planning user acceptance testing, doing a gap analysis between delivered and required, or drafting a sign-off document. Trigger on 'traceability matrix', 'RTM', 'ma trận truy vết', 'UAT', 'user acceptance testing', 'kịch bản kiểm thử', 'test scenario', 'nghiệm thu', 'acceptance criteria coverage', 'gap analysis', 'go-live checklist', or any request to confirm requirements are met and get formal acceptance. Downstream of ba-requirements-spec and ba-user-stories."
license: Complete terms in LICENSE.txt
---

# BA Solution Validation

Validation answers the only two questions that matter at the end of a project: **"Did we build it
right?"** (verification — meets the spec) and **"Did we build the right thing?"** (validation — meets
the business need). This skill produces the artifacts that answer both with evidence, not opinion —
so go-live is a decision, not a gamble.

## 1. Requirements Traceability Matrix (RTM)

The RTM is the backbone. It links each requirement forward to the things that satisfy it and back to
why it exists, so you can prove coverage and spot orphans:

```
Business goal → Requirement (REQ-###) → User story (US-##) → Test case (TC-##) → Result
```

Two failure modes the RTM catches:
- **Uncovered requirement** — a REQ with no test → you can't prove it works.
- **Orphan build** — a story/test with no REQ → you built something nobody asked for (scope creep).

See `assets/rtm-template.md` for the grid and a coverage-summary pattern. Always finish an RTM with a
coverage statement: "X of Y requirements have passing tests; the following N are uncovered."

## 2. UAT scenarios and scripts

UAT is the business confirming the solution works *for real work*, not just that code passes. Design
it around **real business scenarios**, end-to-end, in the users' language — not around screens.

Each UAT case has: a clear objective, preconditions/test data, numbered steps, expected result, and a
pass/fail + actual-result column for the tester. Reuse the Given/When/Then acceptance criteria from
`ba-user-stories` as the seed for cases — they're already testable. See `assets/uat-template.md`.

Cover happy paths **and** the alternate/error paths and edge cases. UAT that only walks the happy
path gives false confidence.

## 3. Gap analysis

When the delivered solution doesn't fully match the requirements, document the gap precisely so
stakeholders can decide: fix-before-launch, launch-with-workaround, or descope.

| Requirement | Expected | Delivered | Gap | Severity | Recommendation |
|---|---|---|---|---|---|
| FR-07 | Export to PDF & Excel | PDF only | Excel missing | Medium | Phase 2; manual export workaround for now |

Severity drives the decision: a **Critical** gap blocks go-live; a **Low** one goes on the backlog.

## 4. Acceptance & sign-off

Acceptance is formal. The sign-off document states what was tested, the results, known
gaps/workarounds, and an explicit decision (accept / accept-with-conditions / reject) with named
approvers. No "it seems fine" — acceptance is a recorded decision by accountable people.

## Workflow

1. **Build the RTM** from the requirements (`ba-requirements-spec`) and stories (`ba-user-stories`);
   flag uncovered requirements and orphan builds.
2. **Write UAT scenarios** for each requirement/story, seeded from acceptance criteria, covering
   happy + alternate + edge cases.
3. **Record results**; for failures, capture the gap with severity.
4. **Do the gap analysis**; recommend an action per gap.
5. **Produce the sign-off** with the coverage summary and an explicit decision.

## Output expectations

- An RTM with a coverage summary line.
- UAT scripts a non-technical business user can execute unaided.
- A gap log with severities, if any gaps exist.
- A sign-off doc with named approvers and a clear decision.

## Guardrails

- Don't claim coverage you can't show. If a requirement has no test, say so — an honest "uncovered"
  is worth more than a green checkmark you can't defend.
- Keep UAT in business language. If a clerk can't follow the script without a developer, rewrite it.
- A gap is a decision, not a defect to hide. Surface every gap with a severity so accountable people
  choose consciously — don't quietly descope.
