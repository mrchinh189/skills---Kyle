# Software Requirements Specification — [Project / Module]

| | |
|---|---|
| **Owner** | [BA] · **Version** | 0.1 · **Status** | Draft |
| **Traces to** | [BRD version] |

## 1. Introduction
- **Purpose**: [what this SRS covers]
- **Scope**: [system/module boundaries]
- **Definitions & acronyms**: [glossary]
- **References**: [BRD, process models, standards]

## 2. Overall description
- **Product perspective**: [where this fits in the system landscape]
- **User classes / personas**: [who uses it and their key needs]
- **Operating environment**: [platforms, browsers, integrations]
- **Assumptions & dependencies**: [AS-##, dependencies]

## 3. Functional requirements
Group by feature. Each requirement is atomic, testable, "shall"-phrased, and ID'd.

### 3.1 [Feature area, e.g., Authentication]
| ID | Requirement | Priority | Traces to |
|----|-------------|----------|-----------|
| FR-01 | The system shall lock an account after 5 consecutive failed login attempts within 10 minutes. | Must | BR-03 |
| FR-02 | The system shall send a password-reset link valid for 30 minutes. | Must | BR-03 |

**Business rules** (the logic behind the behavior)
| ID | Rule |
|----|------|
| BRule-01 | Lockout duration is 15 minutes; an admin may unlock manually. |

### 3.2 [Next feature area]
[...]

## 4. Non-functional requirements
| ID | Category | Requirement (measurable) |
|----|----------|--------------------------|
| NFR-01 | Performance | 95th-percentile login response < 1s under 500 concurrent users |
| NFR-02 | Security | Passwords stored with bcrypt (cost ≥ 12); data in transit over TLS 1.2+ |
| NFR-03 | Availability | 99.9% monthly uptime |
| NFR-04 | Usability | A new user completes signup in ≤ 2 minutes without help |

## 5. External interfaces
- **UI**: [key screens / wireframe refs]
- **APIs / integrations**: [endpoints, data exchanged, error handling]
- **Data**: [entities, key fields — or ref a data dictionary]

## 6. Acceptance criteria summary
[High-level "done" conditions; detailed cases live in ba-user-stories / ba-solution-validation.]

## 7. Open questions
- [ ] [FR-## — question — owner]
