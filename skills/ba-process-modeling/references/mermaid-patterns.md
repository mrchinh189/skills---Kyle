# Mermaid Patterns for Process Modeling — Reference

Copy-adapt these patterns. They render on GitHub and in most Markdown viewers. Read when you need a
shape, a swimlane, a loop, or styling you don't remember.

## Table of contents
1. Node shapes (process notation)
2. Decisions and branches
3. Loops and rework
4. Sub-processes
5. Swimlanes (cross-functional)
6. Sequence diagram (for system interactions)
7. Styling pain points / changes
8. Common mistakes

---

## 1. Node shapes

```mermaid
flowchart LR
    s([Start / End])
    t[Task / activity]
    d{Decision}
    doc[/Document or data/]
    sub[[Sub-process]]
    db[(Data store)]
```

---

## 2. Decisions and branches

```mermaid
flowchart TD
    A[Submit expense] --> B{Amount > $500?}
    B -->|Yes| C[Director approval]
    B -->|No| D[Auto-approve]
    C --> E([Reimbursed])
    D --> E
```

Label *every* branch from a decision. An unlabeled branch is ambiguous.

---

## 3. Loops and rework

Rework loops are often the real cost in a process — show them explicitly.

```mermaid
flowchart TD
    A[Draft contract] --> B[Legal review]
    B --> C{Changes needed?}
    C -->|Yes| A
    C -->|No| D([Signed])
```

---

## 4. Sub-processes

Keep the top level readable; detail heavy steps separately.

```mermaid
flowchart LR
    A([Order received]) --> B[[Credit check]] --> C[[Fulfilment]] --> D([Delivered])
```

Then detail `Credit check` in its own diagram.

---

## 5. Swimlanes (cross-functional)

Use `subgraph` per actor. Cross-lane arrows = hand-offs (watch these for delay/error).

```mermaid
flowchart TD
    subgraph Customer
        A([Place order])
    end
    subgraph Sales
        B[Confirm order] --> C[Check stock]
    end
    subgraph Warehouse
        D[Pick & pack] --> E[Ship]
    end
    subgraph Finance
        F[Invoice]
    end
    A --> B
    C --> D
    E --> F
    F --> G([Order complete])
```

> Tip: Mermaid `flowchart` swimlanes are approximate. For strict BPMN pools/lanes you'd use a BPMN
> tool, but for BA communication this is usually enough and stays in version control.

---

## 6. Sequence diagram (system interactions)

When the question is "which system calls which, in what order", a sequence diagram beats a flowchart.

```mermaid
sequenceDiagram
    actor U as User
    participant W as Web app
    participant A as Auth service
    participant D as Database
    U->>W: Submit login
    W->>A: Validate credentials
    A->>D: Lookup user
    D-->>A: User record
    A-->>W: Token (or error)
    W-->>U: Logged in / error message
```

---

## 7. Styling pain points / changes

```mermaid
flowchart LR
    A[Manual re-keying] --> B[Send email]
    style A fill:#ffd6d6,stroke:#c0392b,stroke-width:2px
    B:::changed
    classDef changed fill:#d6f5d6,stroke:#27ae60,stroke-width:2px;
```

Convention: red = pain/removed, green = new/improved, yellow = needs verification.

---

## 8. Common mistakes

- **No start/end** → the process looks like it floats. Always bound it.
- **Unlabeled decision branches** → ambiguous logic.
- **Hidden rework loops** → you miss the biggest cost. Draw the loop back.
- **One giant diagram** → unreadable. Use sub-processes past ~15–20 nodes.
- **Modeling the SOP, not reality** → the AS-IS must include the workarounds.
