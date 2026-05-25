# AI Use-Case Assessment Frameworks — Reference

Detailed rubrics, the ROI model, and chart patterns. Read when scoring an opportunity or building the
portfolio view. SKILL.md has the workflow; this is the depth.

## Table of contents
1. Value scoring rubric
2. Feasibility scoring rubric
3. Portfolio chart (value × feasibility)
4. ROI model
5. Data-readiness scorecard
6. Agentic-specific design checklist

---

## 1. Value scoring rubric (score each 1–5, then sum or weight)

| Dimension | 1 (low) | 5 (high) |
|---|---|---|
| Time saved | minutes/month | many FTE-hours/week |
| Error reduction | negligible | eliminates a costly, frequent error |
| Financial impact | rounding error | material revenue/cost change |
| Risk reduction | none | removes a compliance/safety exposure |
| Experience uplift | unnoticed | clearly better for customer/employee |
| Strategic fit | tangential | core to a stated business goal |

Quantify in real units wherever possible — "2h/day × 5 clerks × $X" beats "saves time".

## 2. Feasibility scoring rubric (score each 1–5; **low** feasibility = high risk)

| Dimension | 1 (hard) | 5 (easy) |
|---|---|---|
| Data readiness | scarce/dirty/inaccessible | abundant, clean, accessible |
| Task complexity | open-ended, expert judgment | bounded, well-defined |
| Integration effort | many brittle systems | one clean API / standalone |
| Error tolerance | zero-tolerance, irreversible | tolerant, recoverable, reviewable |
| Change management | strong resistance, retraining | users eager, low disruption |
| Explainability need | must justify every decision | black-box acceptable |

## 3. Portfolio chart (value × feasibility)

```mermaid
quadrantChart
    title AI opportunity portfolio
    x-axis Low feasibility --> High feasibility
    y-axis Low value --> High value
    quadrant-1 Do now (quick wins + bets)
    quadrant-2 Invest to enable
    quadrant-3 Decline / park
    quadrant-4 Easy but low value (fill-ins)
    Invoice extraction: [0.75, 0.8]
    Contract review assistant: [0.35, 0.85]
    Email auto-tagging: [0.85, 0.3]
    Full autonomous procurement: [0.2, 0.7]
```

Interpretation: top-right = do now; top-left = high value but build data/capability first; bottom =
deprioritize regardless of novelty.

## 4. ROI model

```
Annual benefit  = (hours saved/yr × loaded hourly cost)
                + (errors avoided/yr × cost per error)
                + (revenue uplift or risk-cost avoided)

Annual cost     = build (one-off, amortized) + run (model/API + infra)
                + human-review time + maintenance + change-mgmt

Net value/yr    = Annual benefit − Annual cost
Payback (months)= build cost ÷ (monthly net benefit)
```

Always include the **human-review cost** — HITL is not free, and omitting it is the most common way
AI business cases lie.

## 5. Data-readiness scorecard

| Check | Red | Yellow | Green |
|---|---|---|---|
| Exists & accessible | not collected | siloed/manual export | available via system/API |
| Quality | inconsistent/incomplete | needs cleaning | clean, validated |
| Volume & coverage | sparse, missing edge cases | enough for common cases | rich, covers edges |
| Labels / ground truth | none | partial/proxy | reliable labels exist |
| Governance | PII/consent unclear | restricted use | cleared for this use |

Any **red** in "exists" or "governance" → treat as a data/governance project before AI build.

## 6. Agentic-specific design checklist

For use cases where the AI takes multi-step actions with tools (an *agent*):

- [ ] **Allowed actions** enumerated (the tools/APIs it may call).
- [ ] **Hard boundaries** defined (what it must never do, e.g., no payments > $X, no deletes).
- [ ] **Approval gates** on irreversible/high-stakes steps (human-in-the-loop there).
- [ ] **Autonomy scaled to reversibility** — more autonomy only where actions are easy to undo.
- [ ] **Audit trail** of every action and the reasoning/inputs behind it.
- [ ] **Kill switch / pause** and a clear escalation path on uncertainty.
- [ ] **Confidence handling** — defined behavior when the model is unsure (ask, defer, escalate).
- [ ] **Monitoring** — override rate, error rate, and drift tracked after launch.

> Principle: an agent's autonomy should grow only as fast as your evidence that it's trustworthy on
> that task. Start narrow, human-gated, and measured; widen scope as the override rate falls.
