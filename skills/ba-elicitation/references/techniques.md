# Elicitation Techniques — Reference

Read this when you need the full technique catalog, question banks, or templates. The main SKILL.md
covers the workflow; this file is the depth.

## Table of contents
1. Technique catalog (when/how/pitfalls)
2. Interview question bank (by funnel stage)
3. Workshop facilitation patterns
4. Questionnaire design
5. Templates (interview guide, workshop agenda)

---

## 1. Technique catalog

### Interview (1:1 or small group)
- **Best for**: deep understanding of a single role, sensitive topics, pain points.
- **How**: funnel structure, 45–60 min, one note-taker if possible, record only with consent.
- **Pitfalls**: leading questions ("you'd want X, right?"); accepting the first answer without
  asking "why"; interviewing only managers and missing the people who do the work.

### Workshop (facilitated group)
- **Best for**: reconciling conflicting views, co-designing a TO-BE process, prioritization.
- **How**: clear objective, timeboxed agenda, a facilitator separate from a scribe, visible parking
  lot for off-topic items, decisions captured live.
- **Pitfalls**: dominated by the loudest voice; no decision owner; outputs not written down.

### Questionnaire / survey
- **Best for**: breadth — many stakeholders, geographically spread, quantifiable.
- **How**: mostly closed questions for analysis, a few open ones for surprises; pilot it on 2–3
  people first.
- **Pitfalls**: ambiguous wording; too long (drop-off); no way to probe answers.

### Observation / job shadowing
- **Best for**: when the documented process differs from reality, or tacit knowledge.
- **How**: watch without interrupting, note workarounds and "shadow systems" (the spreadsheet
  everyone secretly uses), debrief afterward.
- **Pitfalls**: Hawthorne effect (people behave differently when watched); over-generalizing from
  one observation.

### Document & data analysis
- **Best for**: existing systems, regulated domains, establishing ground truth before opinions.
- **How**: read SOPs, forms, screenshots, sample data, audit logs; note what fields/steps actually
  exist.
- **Pitfalls**: trusting stale docs; mistaking "what the manual says" for "what people do".

### Prototyping / wireframe walkthrough
- **Best for**: fuzzy UI requirements; "I'll know it when I see it" stakeholders.
- **How**: low-fidelity first; ask "what would you do next?" rather than "do you like it?".
- **Pitfalls**: anchoring on the prototype as if it were the final design.

---

## 2. Interview question bank (by funnel stage)

**Context**
- "Walk me through a typical day/week in your role."
- "Where does this process start for you, and where does it hand off?"

**Current state (AS-IS)**
- "Show me exactly how you do X today, step by step."
- "What systems or spreadsheets do you touch to get this done?"
- "Roughly how long does X take? How often?"

**Pain points**
- "What's the most frustrating part of this?"
- "When was the last time this went wrong? What happened?"
- "What do you do when [the system is down / data is missing]?"
- (Probe every answer with) "Why does that happen?"

**Desired state (TO-BE)**
- "If you had a magic wand, what would change?"
- "What would 'good' look like a year from now?"

**Constraints & rules**
- "Are there policies, regulations, or approvals that govern this?"
- "What absolutely must not change?"

**Edge cases**
- "What happens at month-end / year-end / during a sale?"
- "Who covers this when you're on leave?"
- "What's the weirdest case you've had to handle?"

---

## 3. Workshop facilitation patterns

- **Round-robin** to stop one voice dominating: everyone answers in turn before open discussion.
- **Silent brainstorm → cluster**: write ideas on cards first, then group — reduces anchoring.
- **Dot voting** for quick prioritization.
- **Parking lot**: a visible list for important-but-off-topic items so the agenda stays on track.
- **Decision log**: capture every decision with an owner and date, live, on screen.

---

## 4. Questionnaire design

- Keep under ~15 questions; group by theme.
- One idea per question; avoid double-barreled ("Is the system fast and reliable?").
- Use consistent scales (e.g., 1–5 Likert) so answers aggregate.
- Add one open "anything else?" field for surprises.
- Always pilot before sending widely.

---

## 5. Templates

### Interview guide

```markdown
# Interview Guide — [role]
**Goal**: [the decision this informs]
**Known already**: [so we don't re-ask]
**Time**: 45–60 min

## Warm-up (5m)
- Intro, purpose, consent to take notes.

## Context (10m)
- [questions]

## Current state (15m)
- [questions]

## Pain points (15m)
- [questions + "why?" probes]

## Desired state & constraints (10m)
- [questions]

## Wrap-up (5m)
- "Anything I should have asked but didn't?"
- Next steps, thank you.
```

### Workshop agenda

```markdown
# Workshop — [topic]
**Objective**: [single clear outcome]
**Participants**: [roles] · **Facilitator**: [name] · **Scribe**: [name]

| Time | Activity | Output |
|------|----------|--------|
| 0:00 | Goal & ground rules | shared understanding |
| 0:10 | AS-IS walkthrough | current-state map |
| 0:40 | Pain points (silent brainstorm → cluster) | ranked pain list |
| 1:10 | TO-BE co-design | draft future process |
| 1:40 | Decisions & parking lot review | decision log |
| 1:55 | Next steps | owners + dates |
```
