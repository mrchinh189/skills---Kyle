# Agent Skills — Hướng dẫn trực quan (bản đầy đủ cho BA)

> Tài liệu này giải mã **cốt lõi** mà tác giả repo `anthropics/skills` muốn truyền tải, rồi
> chỉ ra cách một **Business Analyst (BA) ứng dụng doanh nghiệp** — vừa là *Agentic AI BA*
> vừa là *IT BA* — vận dụng nó. Đọc xong tài liệu này bạn sẽ trả lời được 3 câu hỏi:
>
> 1. **Skill là gì** và tại sao nó tồn tại?
> 2. Skill **được nạp và kích hoạt** như thế nào (cơ chế kỹ thuật)?
> 3. Làm sao **tự viết** một skill tốt, và áp vào nghiệp vụ BA?

---

## 0. TL;DR trong 60 giây

- **Skill = một thư mục** chứa `SKILL.md` (hướng dẫn + metadata) cùng tài nguyên đính kèm
  (`scripts/`, `references/`, `assets/`). Nó *dạy* Claude làm **một loại việc chuyên biệt theo
  cách lặp lại được** — như "viết tài liệu theo brand công ty", "trích xuất form PDF", "viết BRD".
- Nguyên lý trung tâm là **Progressive Disclosure (tiết lộ tiệm tiến)**: chỉ nạp đúng thứ cần,
  đúng lúc cần — để tiết kiệm "bộ nhớ làm việc" (context) và mở rộng gần như vô hạn.
- **`description` là công tắc kích hoạt**. Viết description tốt = skill được dùng đúng lúc.
- Triết lý viết: **giải thích "tại sao" thay vì ra lệnh cứng nhắc**; giữ gọn; gom việc lặp lại
  thành script dùng chung; lặp *draft → đánh giá (eval) → cải tiến*.

```mermaid
flowchart LR
    A["Người dùng nêu yêu cầu<br/>(ngôn ngữ tự nhiên)"] --> B{"Claude quét<br/>danh sách skills"}
    B -->|"description khớp +<br/>việc đủ phức tạp"| C["Nạp thân SKILL.md"]
    B -->|"không khớp"| Z["Tự xử lý<br/>bằng công cụ cơ bản"]
    C --> D["Đọc references/ khi cần"]
    C --> E["Chạy scripts/ khi cần"]
    C --> F["Dùng assets/ cho đầu ra"]
    D & E & F --> G["Hoàn thành tác vụ<br/>theo cách chuẩn hoá"]
```

---

## 1. Vấn đề mà Skill giải quyết

Một mô hình ngôn ngữ "trần" rất giỏi việc chung nhưng có 3 điểm yếu khi vào **doanh nghiệp**:

| Điểm yếu của LLM trần | Hệ quả với doanh nghiệp | Skill khắc phục thế nào |
|---|---|---|
| Không biết **quy ước riêng** của tổ chức | Mỗi lần ra một kiểu, không nhất quán | Đóng gói quy ước (template, tone, brand) vào skill |
| **Context có hạn** — nhồi hết tài liệu vào là tốn & loãng | Trả lời lan man, quên chi tiết | Progressive disclosure: chỉ nạp khi cần |
| **Lặp lại** việc dựng công cụ mỗi phiên | Chậm, dễ sai, tốn token | Bundle sẵn `scripts/` để chạy thẳng |

> **Tinh thần của tác giả:** Skill biến Claude từ "trợ lý vạn năng nhưng generic" thành
> "đồng nghiệp đã được *onboard* vào đúng cách làm việc của tổ chức bạn".

---

## 2. Giải phẫu một Skill

```mermaid
flowchart TD
    subgraph S["skill-name/  (một thư mục tự chứa)"]
        direction TB
        M["SKILL.md  ★ bắt buộc<br/>─ YAML frontmatter: name, description<br/>─ Phần thân: hướng dẫn dạng Markdown"]
        R["references/  (tuỳ chọn)<br/>Tài liệu đọc-khi-cần"]
        SC["scripts/  (tuỳ chọn)<br/>Code chạy được cho việc lặp/định lượng"]
        AS["assets/  (tuỳ chọn)<br/>Template, font, icon dùng cho đầu ra"]
    end
    M -.->|"trỏ tới khi cần"| R
    M -.->|"gọi để chạy"| SC
    M -.->|"dùng để xuất"| AS
```

**Chỉ `SKILL.md` là bắt buộc.** Trong đó chỉ 2 trường frontmatter bắt buộc:

```yaml
---
name: ten-skill            # định danh, viết-thường-có-gạch-nối
description: Skill làm gì + KHI NÀO Claude nên dùng nó.
---
# Tiêu đề skill
[Hướng dẫn Claude sẽ tuân theo khi skill được kích hoạt]
```

- `scripts/` → việc **xác định/lặp đi lặp lại** (vd: dựng file .docx, kiểm tra form PDF). Quan
  trọng: *script chạy được mà không cần nạp nội dung vào context* → tiết kiệm cực lớn.
- `references/` → tài liệu **đọc-khi-cần** (vd: bảng tra cú pháp, hướng dẫn chi tiết theo từng biến thể).
- `assets/` → **vật liệu đầu ra** (template tài liệu, font, ảnh nền).

---

## 3. Trái tim kỹ thuật: Progressive Disclosure (3 tầng)

Đây là ý tưởng quan trọng nhất của repo. Context của Claude là tài nguyên khan hiếm; skill được
thiết kế để **chỉ tốn context cho thứ thực sự cần ngay lúc đó**.

```mermaid
flowchart TB
    subgraph L1["TẦNG 1 — Metadata (LUÔN nằm trong context)"]
        T1["name + description (~100 từ)<br/>Claude đọc cái này để quyết định CÓ dùng skill không"]
    end
    subgraph L2["TẦNG 2 — Thân SKILL.md (nạp KHI skill kích hoạt)"]
        T2["Hướng dẫn quy trình (lý tưởng < 500 dòng)"]
    end
    subgraph L3["TẦNG 3 — Tài nguyên đính kèm (nạp/chạy KHI cần)"]
        T3["references/ · scripts/ · assets/  (dung lượng ~ không giới hạn)"]
    end
    L1 -->|"nếu khớp & việc đủ phức tạp"| L2
    L2 -->|"khi quy trình yêu cầu"| L3
```

| Tầng | Khi nào vào context | Ngân sách | Ví dụ |
|---|---|---|---|
| 1. Metadata | **Luôn luôn** | ~100 từ | `name`, `description` |
| 2. Thân SKILL.md | Khi skill **kích hoạt** | < 500 dòng (mềm) | quy trình các bước |
| 3. Tài nguyên | Khi **cần dùng** | gần như vô hạn | `references/aws.md`, `scripts/build.py` |

> **Hệ quả thiết kế:** giữ `SKILL.md` gọn; tài liệu dài/biến thể nhiều thì tách ra `references/`
> và **trỏ rõ** "khi gặp X thì đọc file Y". Đây chính là cách skill `claude-api` hay `mcp-builder`
> trong repo tổ chức nội dung.

**Mẫu tổ chức đa biến thể (domain organization):**

```text
cloud-deploy/
├── SKILL.md            # quy trình chung + cách CHỌN biến thể
└── references/
    ├── aws.md          # chỉ đọc khi triển khai AWS
    ├── gcp.md
    └── azure.md
```

---

## 4. Cơ chế kích hoạt (Triggering) — vì sao `description` là vua

Claude nhìn thấy mọi skill dưới dạng **name + description** trong danh sách `available_skills`,
rồi tự quyết định có "tham vấn" skill đó không. Hai điều cốt yếu:

1. **Description quyết định trigger.** Phải nêu *làm gì* **và** *khi nào dùng* — kèm ngữ cảnh,
   từ khoá, cả khi người dùng **không gọi tên** skill.
2. **Việc phải đủ phức tạp.** Câu hỏi 1 bước ("đọc file PDF này") có thể **không** trigger skill
   vì Claude tự làm được. Skill được tham vấn cho việc nhiều bước/chuyên biệt.

```mermaid
sequenceDiagram
    participant U as Người dùng
    participant C as Claude
    participant SK as Danh sách skills (metadata)
    U->>C: "Viết giúp BRD cho hệ thống quản lý kho..."
    C->>SK: Quét description của tất cả skills
    SK-->>C: "ba-requirements-spec" khớp (BRD/SRS/FRD)
    C->>C: Việc đủ phức tạp? → Có
    C->>C: Nạp thân SKILL.md của ba-requirements-spec
    C-->>U: Làm theo quy trình chuẩn trong skill
```

> ⚠️ **Bẫy thường gặp: under-trigger** (skill hữu ích nhưng không được gọi). Tác giả khuyên viết
> description **"hơi pushy"**. So sánh:
>
> - ❌ *"How to build a dashboard for internal data."*
> - ✅ *"How to build a dashboard for internal data. **Use this skill whenever the user mentions
>   dashboards, data visualization, internal metrics, or wants to display any company data — even
>   if they don't explicitly say 'dashboard'.**"*

**Mẫu description tốt** thường có cấu trúc: `[Làm gì] + [TRIGGER khi: ...] + (tuỳ chọn) [SKIP khi: ...]`.
Xem skill `claude-api` và `xlsx` trong repo để thấy mẫu TRIGGER/SKIP rõ ràng.

---

## 5. Vòng đời tạo skill — `skill-creator` (meta-skill)

`skill-creator` là skill *để tạo ra skill khác*. Nó mã hoá một vòng lặp thực nghiệm:

```mermaid
flowchart LR
    I["1 Nắm ý định<br/>(làm gì / trigger khi nào /<br/>đầu ra ra sao)"] --> D["2 Viết bản nháp<br/>SKILL.md"]
    D --> T["3 Tạo 2-3 test prompt<br/>thực tế"]
    T --> R["4 Chạy SONG SONG:<br/>có-skill vs không-skill"]
    R --> E["5 Người dùng review<br/>(eval viewer) +<br/>đo định lượng"]
    E --> IM["6 Cải tiến skill"]
    IM -->|"lặp lại"| R
    IM --> O["7 Tối ưu description<br/>để trigger chính xác"]
    O --> P["8 Đóng gói .skill"]
```

Các ý niệm đáng nhớ từ vòng lặp này (rất hữu ích cho BA khi "đặc tả" bất cứ thứ gì):

- **Baseline so sánh:** luôn chạy *có-skill* cạnh *không-skill* để biết skill có thực sự thêm giá trị.
- **Đừng overfit:** skill phải đúng cho *hàng triệu* tình huống tương lai, không chỉ vài ví dụ test.
- **Đọc transcript, không chỉ kết quả:** nếu nhiều lần test đều tự viết một script giống nhau →
  dấu hiệu nên *bundle* script đó vào skill.
- **Eval = bằng chứng, không phải cảm tính.** Tư duy này trùng khớp với UAT/nghiệm thu của BA.

---

## 6. Triết lý viết skill (rất quan trọng — và rất "BA")

Tác giả nhấn mạnh **văn phong & tư duy**, không chỉ cú pháp:

```mermaid
mindmap
  root((Cách viết skill tốt))
    Giải thích TẠI SAO
      "LLM thông minh, có theory-of-mind"
      "Tránh ALWAYS/NEVER in hoa cứng nhắc"
      "Nêu lý do để model tự suy luận tình huống mới"
    Giữ gọn (lean)
      "Bỏ phần không tạo giá trị"
      "SKILL.md < 500 dòng"
      "Tách chi tiết sang references/"
    Dạng mệnh lệnh (imperative)
      "Viết hướng dẫn ở thể sai khiến"
      "Định nghĩa rõ định dạng đầu ra"
    Khái quát hoá
      "Đừng bám ví dụ cụ thể"
      "Dùng ẩn dụ/khuôn mẫu thay vì luật cứng"
    Nguyên tắc không gây bất ngờ
      "Không malware/khai thác"
      "Nội dung đúng như mô tả"
```

> Câu trích đáng dán lên tường: *"If you find yourself writing ALWAYS or NEVER in all caps, that's
> a yellow flag — reframe and explain the reasoning."* (Nếu bạn đang viết ALWAYS/NEVER in hoa, hãy
> dừng lại và **giải thích lý do** thay vì ra lệnh.)

Với BA, đây chính là khác biệt giữa một **đặc tả tốt** (nêu *ý định & ràng buộc*, cho phép suy
luận) và một **checklist chết** (liệt kê cứng, vỡ khi gặp tình huống mới).

---

## 7. Bản đồ catalog repo gốc (17 skill)

```mermaid
flowchart TB
    ROOT["anthropics/skills"]
    ROOT --> DOC["📄 Tài liệu"]
    ROOT --> CRE["🎨 Sáng tạo & Thiết kế"]
    ROOT --> TECH["🛠️ Kỹ thuật"]
    ROOT --> ENT["🏢 Doanh nghiệp & Giao tiếp"]

    DOC --> docx & pdf & pptx & xlsx
    CRE --> canvas-design & algorithmic-art & frontend-design & theme-factory & brand-guidelines & slack-gif-creator
    TECH --> mcp-builder & webapp-testing & web-artifacts-builder & claude-api & skill-creator
    ENT --> internal-comms & doc-coauthoring
```

| Nhóm | Skill | Lõi giá trị |
|---|---|---|
| Tài liệu | `docx`,`pdf`,`pptx`,`xlsx` | Tạo/đọc/sửa tài liệu văn phòng chuẩn (đang chạy production) |
| Sáng tạo | `canvas-design`,`algorithmic-art`,`frontend-design`,`theme-factory`,`brand-guidelines`,`slack-gif-creator` | Thiết kế hình ảnh/giao diện có gu, đúng brand |
| Kỹ thuật | `mcp-builder`,`webapp-testing`,`web-artifacts-builder`,`claude-api`,`skill-creator` | Xây MCP, test web, dựng artifact, dùng API, tạo skill |
| Doanh nghiệp | `internal-comms`,`doc-coauthoring` | Viết comms nội bộ; đồng-soạn tài liệu có quy trình |

> Hai skill `internal-comms` và `doc-coauthoring` là *họ hàng gần nhất* của nghề BA — và là khuôn
> mẫu trực tiếp cho bộ skill BA mà repo này bổ sung (xem mục 8 và tài liệu playbook).

---

## 8. Hiện thực hoá cho vai trò BA doanh nghiệp

Repo gốc thiếu lớp **phân tích nghiệp vụ**. Bộ skill `ba-*` được thêm vào để phủ trọn vòng đời BA
(theo tinh thần BABOK, nhưng tinh gọn để dùng được ngay). Sơ đồ ánh xạ:

```mermaid
flowchart LR
    subgraph BA["Vòng đời Phân tích Nghiệp vụ"]
        direction LR
        E["Khơi gợi<br/>yêu cầu"] --> A["Phân tích &<br/>đặc tả"]
        A --> MO["Mô hình hoá<br/>quy trình"]
        A --> US["User story &<br/>backlog"]
        E -.-> SH["Quản lý<br/>stakeholder"]
        US --> V["Kiểm thử &<br/>nghiệm thu"]
        MO --> V
    end
    E -.->|skill| s1["ba-elicitation"]
    A -.->|skill| s2["ba-requirements-spec"]
    MO -.->|skill| s3["ba-process-modeling"]
    US -.->|skill| s4["ba-user-stories"]
    SH -.->|skill| s5["ba-stakeholder-mgmt"]
    V -.->|skill| s6["ba-solution-validation"]
    BA -.->|"xuyên suốt (AI)"| s7["ba-ai-usecase"]
```

| Skill BA | Giai đoạn | Đầu ra chính |
|---|---|---|
| `ba-elicitation` | Khơi gợi | Kế hoạch phỏng vấn/workshop, bộ câu hỏi, biên bản khơi gợi |
| `ba-requirements-spec` | Đặc tả | BRD, SRS/FRD, danh mục NFR |
| `ba-user-stories` | Backlog | Epic, user story, tiêu chí chấp nhận (Gherkin), kiểm INVEST |
| `ba-process-modeling` | Mô hình hoá | Sơ đồ AS-IS/TO-BE (Mermaid), swimlane, phân tích gap quy trình |
| `ba-stakeholder-mgmt` | Xuyên suốt | Bản đồ stakeholder, ma trận RACI, kế hoạch truyền thông, status report |
| `ba-solution-validation` | Nghiệm thu | Ma trận truy vết (RTM), kịch bản UAT, gap analysis, biên bản chấp nhận |
| `ba-ai-usecase` | Xuyên suốt (Agentic AI) | Khung đánh giá use-case AI: khả thi, ROI, mức sẵn sàng dữ liệu, HITL, rủi ro |

Chi tiết cách dùng từng skill (đầu vào, đầu ra, prompt mẫu) nằm ở **[`02-ba-skills-playbook.md`](./02-ba-skills-playbook.md)**.

---

## 9. Cách dùng nhanh trong Claude Code

```text
# Đăng ký marketplace (chạy trong Claude Code)
/plugin marketplace add <repo-này>

# Cài bộ skill BA
/plugin install ba-enterprise-skills@anthropic-agent-skills

# Sau đó chỉ cần nói tự nhiên, skill tự kích hoạt:
"Viết BRD cho hệ thống quản lý kho cho công ty bán lẻ 200 cửa hàng."
"Vẽ quy trình AS-IS rồi TO-BE cho luồng phê duyệt mua hàng."
"Bóc user story + tiêu chí chấp nhận cho module đăng nhập SSO."
```

---

## 10. 7 nguyên tắc để mang đi (cheat-sheet)

1. **Skill = thư mục + `SKILL.md`.** Tự chứa, gói được, chia sẻ được.
2. **Progressive disclosure** — chỉ nạp thứ cần, đúng lúc. Giữ thân gọn, đẩy chi tiết ra `references/`.
3. **`description` là công tắc.** Nêu *làm gì + khi nào*, hơi "pushy", có thể kèm SKIP.
4. **Giải thích TẠI SAO**, đừng ra lệnh cứng. Model thông minh — cho nó lý do để suy luận.
5. **Gom việc lặp thành `scripts/`.** Viết một lần, dùng mãi, khỏi tốn context.
6. **Lặp có bằng chứng:** draft → eval (có/không skill) → cải tiến. Đừng overfit vài ví dụ.
7. **Không gây bất ngờ.** Nội dung đúng như mô tả, an toàn, minh bạch.
