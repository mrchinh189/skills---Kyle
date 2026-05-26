---
name: ba-stakeholder-mgmt
description: "Identify, analyze, and plan communication with project stakeholders — power/interest mapping, RACI responsibility matrices, communication plans, and status updates (3P). Use this skill whenever a business analyst needs to manage the people side of a project: listing and analyzing stakeholders, building a RACI matrix, deciding who to engage how often, or writing a status/leadership update. Trigger on 'stakeholder', 'bên liên quan', 'RACI', 'ma trận trách nhiệm', 'communication plan', 'kế hoạch truyền thông', 'power/interest', 'status report', 'cập nhật cho lãnh đạo', 'ai chịu trách nhiệm gì', or any project-governance question about who is involved and how to keep them aligned. Runs throughout the project lifecycle, not just at kickoff."
license: Complete terms in LICENSE.txt
---

# BA Stakeholder Management

Most projects don't fail on technology — they fail on alignment. This skill handles the people side:
knowing *who* matters, *how much*, and *how* to keep each of them engaged so requirements get
confirmed, decisions get made, and nobody is surprised at go-live.

## 1. Identify stakeholders

Cast a wide net first. Prompt for stakeholders across categories so none are missed:
- **Sponsors / funders** — own the budget and the business outcome.
- **Business owners / process owners** — accountable for the affected process.
- **End users** — the people who'll actually use it (often under-consulted).
- **IT / ops / security** — build, run, and secure it.
- **External** — customers, vendors, regulators, auditors.
- **Influencers** — no formal role but sway opinion.

For each, capture: role, what they care about, and what they can give or block.

## 2. Analyze: Power / Interest grid

Plot each stakeholder by **power** (ability to affect the project) and **interest** (how much they
care). The quadrant dictates the engagement strategy — this is the analytical core:

| Quadrant | Strategy |
|---|---|
| **High power, high interest** | **Manage closely** — engage deeply, co-decide, frequent contact |
| **High power, low interest** | **Keep satisfied** — concise updates, don't overload, watch for shifts |
| **Low power, high interest** | **Keep informed** — they're your allies and detail-checkers |
| **Low power, low interest** | **Monitor** — minimal effort, watch for change |

```mermaid
quadrantChart
    title Power / Interest
    x-axis Low interest --> High interest
    y-axis Low power --> High power
    quadrant-1 Manage closely
    quadrant-2 Keep satisfied
    quadrant-3 Monitor
    quadrant-4 Keep informed
    CFO (sponsor): [0.8, 0.85]
    Warehouse lead: [0.9, 0.45]
    Internal audit: [0.4, 0.8]
    End-user clerks: [0.85, 0.25]
```

## 3. RACI — who does what

For each major activity or deliverable, assign exactly one of:
- **R** (Responsible) — does the work · **A** (Accountable) — owns the outcome, *one per row* ·
  **C** (Consulted) — two-way input before · **I** (Informed) — told after.

Rules that prevent dysfunction: **exactly one A per row** (no shared accountability), at least one R,
and don't make everyone C (decision paralysis). See `assets/raci-template.md` for a ready grid.

## 4. Communication plan

Match cadence and channel to the engagement strategy from the grid:

| Audience | What | Channel | Cadence |
|---|---|---|---|
| Sponsor | Status, risks, decisions needed | 1-page update | Weekly |
| Working team | Detailed progress, blockers | Standup / chat | Daily |
| Keep-informed group | Milestones | Newsletter / email | Per milestone |

## 5. Status updates (3P)

Default to the **3P** format — it's scannable and forces signal over noise:
- **Progress** — what got done since last update (outcomes, not activity).
- **Plans** — what's next.
- **Problems** — blockers, risks, decisions needed (with an owner and a date).

See `assets/status-update-template.md`. For longer-form internal comms (newsletters, FAQs), hand off
to the repo's `internal-comms` skill.

## Workflow

1. Brainstorm the full stakeholder list across the categories above.
2. Analyze with the power/interest grid; assign an engagement strategy each.
3. Build the RACI for the project's major activities/deliverables.
4. Draft the communication plan from the strategies.
5. When asked, produce status updates in 3P form.

## Guardrails

- Don't flatten everyone into "the business". Different stakeholders have different — sometimes
  conflicting — needs; name them so conflicts surface early.
- One Accountable per RACI row. If you're tempted to put two A's, the decision rights are unclear —
  flag it for the user to resolve.
- Updates carry decisions, not just activity. A status update that lists tasks but never says what's
  blocked or what decision is needed has failed its job.
