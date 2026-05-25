# Requirements Traceability Matrix — [Project]

Links each requirement forward (to design, story, test, result) and back (to a business goal).

| REQ ID | Requirement (summary) | Business goal | User story | Test case(s) | Status | Result |
|--------|-----------------------|---------------|-----------|--------------|--------|--------|
| FR-01 | Lock account after 5 failed logins | BR-03 (security) | US-12 | TC-12a, TC-12b | Built | ✅ Pass |
| FR-02 | Password reset link (30 min) | BR-03 | US-12 | TC-13 | Built | ✅ Pass |
| FR-07 | Export to PDF & Excel | BR-05 (reporting) | US-21 | TC-30 | Partial | ⚠️ Excel missing |
| NFR-01 | Login p95 < 1s @ 500 users | BR-03 | — | TC-PERF-01 | Built | ✅ Pass |

## Coverage summary
- **Requirements total**: [Y]
- **With passing tests**: [X] ([X/Y]%)
- **Uncovered (no test)**: [list REQ IDs] — *cannot prove these work*
- **Orphan builds (test/story with no REQ)**: [list] — *possible scope creep*

## Legend
Status: Not started / In design / Built / Partial · Result: ✅ Pass / ❌ Fail / ⚠️ Partial / — N/A
