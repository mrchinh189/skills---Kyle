---
name: ba-requirements-spec
description: "Write structured business and software requirements documents — BRD (business requirements), SRS/FRD (functional/software requirements), and NFR catalogs — with traceable requirement IDs. Use this skill whenever a business analyst needs to turn business goals or elicitation notes into a formal specification: drafting a BRD, an SRS or FRD, a functional spec, a requirements section, or a non-functional requirements list. Trigger on 'viết BRD', 'đặc tả yêu cầu', 'SRS', 'FRD', 'functional spec', 'requirements document', 'yêu cầu phi chức năng / NFR', or any request to formalize requirements into a document with numbered, testable requirements. Pair with ba-elicitation (upstream) and ba-user-stories / ba-solution-validation (downstream)."
license: Complete terms in LICENSE.txt
---

# BA Requirements Specification

A specification's job is to be a **single source of truth** that three different audiences can all
trust: business sponsors (does this solve our problem?), developers (what exactly do I build?), and
testers (how do I prove it's done?). The hard part isn't formatting — it's writing requirements that
are unambiguous, testable, and traceable.

## Pick the right document

| Document | Audience | Answers | Level |
|---|---|---|---|
| **BRD** (Business Requirements) | Sponsors, business owners | *Why* are we doing this, what business outcome? | What, in business terms |
| **SRS / FRD** (Software/Functional Requirements) | Developers, testers, BA | *What* must the system do, exactly? | Functional detail |
| **NFR catalog** | Architects, ops, security | *How well* must it perform? | Quality attributes |

A small project may fold these into one document; a large one keeps them separate. Ask if unsure,
but default to: BRD for the "why/what-business", SRS for the "what-system", NFR woven into the SRS.

## What makes a requirement good

Every requirement you write must pass these tests — this is the core of the skill:

- **Unambiguous**: one interpretation only. Replace "fast", "user-friendly", "etc." with specifics.
- **Testable**: someone can write a pass/fail check. If you can't test it, rewrite it.
- **Atomic**: one requirement = one need. Split "and" sentences.
- **Traceable**: has a stable ID (e.g., `REQ-014`) so it can be tracked from origin → design → test.
- **Necessary**: traces back to a business goal. If it doesn't, question it.
- **Feasible & consistent**: doesn't contradict another requirement or a known constraint.

Use **"shall"** for mandatory system behavior: *"The system shall lock an account after 5 consecutive
failed login attempts."* Reserve "should" for recommendations and "may" for options — and say so.

## ID scheme

Give every requirement a stable, prefixed ID so it survives reordering and traces downstream:
- `BR-###` business requirement · `FR-###` functional · `NFR-###` non-functional · `BRule-###`
  business rule · `CON-###` constraint · `AS-###` assumption.

Never renumber on edit — IDs are anchors for the traceability matrix in `ba-solution-validation`.

## Non-functional requirements (don't skip these)

NFRs are where projects silently fail. Cover at least these categories, each with a *measurable*
target:

| Category | Bad (untestable) | Good (testable) |
|---|---|---|
| Performance | "fast" | "95th-percentile page load < 2s under 500 concurrent users" |
| Availability | "always up" | "99.9% monthly uptime (≤ 43 min downtime)" |
| Security | "secure" | "all data encrypted at rest (AES-256) and in transit (TLS 1.2+)" |
| Scalability | "scalable" | "handle 10k orders/day, scalable to 50k without redesign" |
| Usability | "easy" | "a trained clerk completes a return in ≤ 3 minutes" |
| Compliance | "compliant" | "meets [GDPR/PCI-DSS/local regulation] requirements X, Y" |

## Workflow

1. **Confirm scope & goals.** Restate the business objective and what's explicitly *out* of scope —
   scope boundaries prevent the worst arguments later.
2. **Choose the document(s)** per the table above.
3. **Draft requirements**, each ID'd and written to pass the "good requirement" tests.
4. **Add NFRs** with measurable targets.
5. **List assumptions, constraints, and dependencies** explicitly — unstated ones cause failures.
6. **Cross-check**: every FR traces to a BR; no two requirements contradict.

For ready-to-fill templates, read `assets/brd-template.md` and `assets/srs-template.md` and adapt the
sections to the project's size.

## Guardrails

- Don't pad. A short, sharp spec beats a long vague one. Cut sections that add no information.
- Flag ambiguity rather than guessing. If elicitation left a gap, write the requirement as a clearly
  marked `[OPEN: needs confirmation from <role>]` instead of inventing a number.
- Keep business and solution separate. The BRD says *what outcome*; resist specifying *how* to build
  it there — that belongs in the SRS/design.
