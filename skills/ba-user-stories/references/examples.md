# User Story & Acceptance-Criteria Examples — Reference

Worked examples to model new stories on. Read when you need concrete patterns for acceptance
criteria, splitting, or tricky cases.

## Table of contents
1. A well-formed story (with happy + alternate + error AC)
2. Gherkin with a data table (Scenario Outline)
3. Negative / edge-case criteria
4. A good epic split
5. Before/after: fixing common story smells

---

## 1. A well-formed story

### US-12 — Reset a forgotten password
**As a** registered customer **I want** to reset my password from the login page **so that** I can
regain access without contacting support.

```gherkin
Scenario: Successful reset request (happy path)
  Given I am on the login page and have forgotten my password
  When I click "Forgot password" and submit my registered email
  Then I receive a reset email with a link valid for 30 minutes
  And I see "Check your inbox for a reset link."

Scenario: Email not registered (alternate path)
  Given I submit an email that has no account
  When I request a reset
  Then I still see "Check your inbox for a reset link." (no account enumeration)
  And no email is sent

Scenario: Expired link (error path)
  Given my reset link is older than 30 minutes
  When I open it
  Then I see "This link has expired. Please request a new one."
```

> Note how the alternate path encodes a *security* business rule (no account enumeration) — the kind
> of thing that's invisible if you only write the happy path.

---

## 2. Gherkin with a data table (Scenario Outline)

Use when one behavior has many input/output combinations:

```gherkin
Scenario Outline: Shipping fee by order total
  Given a cart subtotal of <subtotal>
  When the customer reaches checkout
  Then the shipping fee shown is <fee>

  Examples:
    | subtotal | fee   |
    | $0–49.99 | $5.00 |
    | $50–99.99| $2.50 |
    | $100+    | $0.00 |
```

---

## 3. Negative / edge-case criteria

Things juniors forget — always ask about these:

```gherkin
Scenario: Concurrent edit conflict
  Given two users open the same record
  When both save changes
  Then the second save is rejected with "This record was changed by someone else. Reload and retry."

Scenario: Boundary value
  Given the discount applies to orders strictly over $100
  When the order total is exactly $100.00
  Then no discount is applied

Scenario: Empty / missing data
  Given a report is requested for a period with no transactions
  When the report runs
  Then it renders with "No data for the selected period" rather than erroring
```

---

## 4. A good epic split

**Epic: Customer can return an order online**

Split by *workflow step + variation* (each slice is shippable and valuable):

- US-01 Start a return for a single eligible item (happy path)
- US-02 Handle ineligible items (out of return window) — error path
- US-03 Return multiple items in one request — data variation
- US-04 Generate a prepaid return label — integration
- US-05 Refund to original payment method — business rule
- US-06 Refund to store credit when original method unavailable — rule variation

**Anti-pattern (don't do this)** — split by layer:
- ❌ "Build returns DB table" / "Build returns API" / "Build returns UI" — none is independently
  shippable or testable by a user.

---

## 5. Before/after: fixing story smells

| Smell | Before | After |
|---|---|---|
| No benefit | "As a user I want a search box." | "As a shopper I want to search products by name **so that** I can find an item without browsing every category." |
| Solution-shaped | "Add an export-to-CSV button." | "As an analyst I want to export my filtered results **so that** I can analyze them in my own spreadsheet." (format becomes an AC, not the story) |
| Too big | "As a user I want to manage my account." | Split: update profile / change password / manage notifications / close account. |
| Untestable AC | "It should be fast." | "Given 10k rows, when I sort a column, then results render in < 1s." |
