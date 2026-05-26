# UAT Test Script — [Project / Module]

**Tester**: [business user role] · **Environment**: [UAT URL] · **Date**: [date]
**Test data**: [accounts, sample records needed]

---

## TC-12a — Account locks after repeated failed logins
**Traces to**: FR-01 / US-12 · **Objective**: Confirm lockout protects accounts.
**Preconditions**: A test account `uat_user1` exists and is unlocked.

| # | Step | Expected result | Pass/Fail | Actual / notes |
|---|------|-----------------|:---------:|----------------|
| 1 | Enter wrong password 4 times | Each shows "Incorrect password" | | |
| 2 | Enter wrong password a 5th time | "Account locked. Try again in 15 minutes." | | |
| 3 | Enter correct password immediately | Still locked; login refused | | |
| 4 | Wait 15 min, enter correct password | Login succeeds | | |

**Overall**: ☐ Pass ☐ Fail · **Defect ID (if fail)**: ______

---

## TC-13 — Password reset (happy + expired link)
**Traces to**: FR-02 / US-12

| # | Step | Expected result | Pass/Fail | Actual / notes |
|---|------|-----------------|:---------:|----------------|
| 1 | Request reset for registered email | "Check your inbox" + email arrives | | |
| 2 | Open reset link within 30 min, set new password | Password changed; can log in | | |
| 3 | Open an expired link (> 30 min) | "This link has expired." | | |

**Overall**: ☐ Pass ☐ Fail

---

## Sign-off
| | Name | Role | Decision (Accept / Accept w/ conditions / Reject) | Date | Signature |
|---|------|------|---------------------------------------------------|------|-----------|
| Business owner | | | | | |
| BA | | | | | |
| QA lead | | | | | |

**Known gaps / conditions**: [list with severity, or "none"]
