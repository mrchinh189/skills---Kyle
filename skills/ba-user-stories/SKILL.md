---
name: ba-user-stories
description: "Turn requirements into an agile backlog — epics, user stories in the 'As a… I want… so that…' form, and acceptance criteria in Given/When/Then (Gherkin) — and quality-check them against INVEST. Use this skill whenever a business analyst or product owner needs to break work down for a dev team: writing user stories, splitting an epic, drafting acceptance criteria, refining a backlog, or sizing/prioritizing stories. Trigger on 'user story', 'viết story', 'acceptance criteria', 'Given/When/Then', 'Gherkin', 'epic', 'backlog refinement', 'tiêu chí chấp nhận', 'bóc tách yêu cầu thành story', or when a feature or requirement needs to become buildable, testable backlog items. Upstream from ba-requirements-spec; feeds ba-solution-validation."
license: Complete terms in LICENSE.txt
---

# BA User Stories

A user story is a **promise of a conversation**, not a mini-spec. Its value is that it keeps the team
focused on *who* benefits and *why* — so the team can build the right thing, not just a thing. Your
job here is to slice work into stories that are independently valuable, testable, and small enough to
flow.

## The three parts of a good story

1. **The card** — the story statement:
   > As a **[role/persona]**, I want **[capability]**, so that **[benefit]**.

   The "so that" is the most important clause. If you can't state a real benefit, question whether
   the story should exist.

2. **The conversation** — context, notes, mockup links, open questions. Stories are deliberately
   under-specified; the detail emerges in conversation and is captured as acceptance criteria.

3. **The confirmation** — acceptance criteria in Given/When/Then form (see below). This is how
   everyone agrees what "done" means *before* building.

## Acceptance criteria: Given / When / Then

Write each criterion as a concrete, testable scenario:

```gherkin
Scenario: Account locks after repeated failed logins
  Given a user has entered the wrong password 4 times
  When they enter a wrong password a 5th time within 10 minutes
  Then the account is locked for 15 minutes
  And the user sees "Account locked. Try again in 15 minutes."
```

Cover the **happy path, alternate paths, and error/edge cases** — a story with only a happy-path
criterion is usually under-analyzed. For more worked examples (including data tables and negative
cases), read `references/examples.md`.

## INVEST — the quality bar

Check every story against INVEST. This is the heart of the skill: most backlog problems are an
INVEST failure.

| Letter | Means | Smell that it's violated | Fix |
|---|---|---|---|
| **I**ndependent | Stand-alone, minimal ordering deps | "can't start until 3 other stories done" | re-slice along value, not layers |
| **N**egotiable | Room for conversation, not a frozen spec | reads like a 2-page contract | move detail into AC, keep card lean |
| **V**aluable | Delivers value to a user/customer | "build the database table" | frame around the user outcome |
| **E**stimable | Team can size it | "research-y", too many unknowns | spike first, then write the story |
| **S**mall | Fits comfortably in a sprint | "epic-sized", many AND/ORs | split (see patterns below) |
| **T**estable | Clear pass/fail | "should be intuitive" | write concrete Given/When/Then |

## Splitting epics into stories

When a story is too big, split by a *value-preserving* axis — never by technical layer
(UI/API/DB makes none of the slices shippable). Useful patterns:

- **Workflow steps**: each step of a process as its own story.
- **Business rule variations**: simple case first, complex rules later.
- **Happy path vs. error handling**: ship the main flow, then harden.
- **CRUD operations**: create first, then read/update/delete.
- **Data variations**: one country/currency/format first, then more.
- **Effort/optimization**: a manual or basic version first, automate later.

## Workflow

1. **Identify the epic(s)** from the requirement or feature.
2. **Define the persona(s)** — be specific ("warehouse clerk", not "user").
3. **Write stories** in the card form, each with a real "so that".
4. **Add acceptance criteria** (Given/When/Then) covering happy + alternate + error paths.
5. **Run the INVEST check**; split anything that fails Small or Independent.
6. **Suggest priority** (MoSCoW or value-vs-effort) and flag dependencies and open questions.

## Output format

```markdown
## Epic: [name]

### Story US-01 — [short title]
**As a** [persona] **I want** [capability] **so that** [benefit].

**Acceptance criteria**
```gherkin
Scenario: [happy path]
  Given ...
  When ...
  Then ...
```
**INVEST**: ✅ / ⚠️ [note any concern] · **Priority**: Must · **Deps**: none · **Open**: [...]
```

## Guardrails

- Don't smuggle a spec into a story. If there are many rigid rules, link to the SRS
  (`ba-requirements-spec`) and keep the story negotiable.
- Don't write solution-shaped stories ("add a dropdown"). Frame the need; let design decide the UI.
- A story without testable acceptance criteria is not ready. Mark it `[needs AC]` rather than passing
  it to the team.
