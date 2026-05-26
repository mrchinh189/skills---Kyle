# RACI Matrix — [Project Name]

**R**esponsible (does the work) · **A**ccountable (owns outcome — exactly one per row) ·
**C**onsulted (input before) · **I**nformed (told after)

| Activity / Deliverable | Sponsor | BA | Product Owner | Dev Lead | QA | Ops | [Stakeholder] |
|------------------------|:-------:|:--:|:-------------:|:--------:|:--:|:---:|:-------------:|
| Approve business case | A | C | C | I | | I | |
| Elicit & document requirements | I | R/A | C | C | | | C |
| Approve requirements (BRD/SRS) | A | R | C | C | I | I | C |
| Design solution | I | C | C | R/A | C | C | |
| Build feature | | I | C | A | | | |
| Write & run UAT | I | C | A | C | R | | C |
| Approve go-live | A | C | C | C | C | C | I |
| Post-launch support | I | I | C | C | C | R/A | |

## Validation checklist
- [ ] Every row has **exactly one A**.
- [ ] Every row has **at least one R**.
- [ ] No row is all C/I (someone must do the work).
- [ ] No person is A on everything (single point of failure).
- [ ] Heavy C columns reviewed (too many consulted = slow decisions).
