---
marp: true
theme: default
paginate: true
# You can change "theme" to any builtin theme; we override styles below to create a custom look.
style: |
  /* --- Custom theme variables --- */
  :root {
    --brand: #0b5fff;
    --accent: #00bfa6;
    --bg: #0f1724;
    --muted: rgba(255,255,255,0.72);
    --card-bg: rgba(255,255,255,0.03);
    --radius: 14px;
    --sans: "Inter", "Helvetica Neue", Arial, sans-serif;
  }

  /* Global slide style */
  section {
    font-family: var(--sans);
    color: #fff;
    background-color: var(--bg);
    padding: 48px;
  }

  /* Title styling */
  section.title {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 80px;
    background: linear-gradient(180deg, rgba(11,95,255,0.08), rgba(0,0,0,0.0));
  }
  h1 { font-size: 48px; margin: 0 0 8px 0; color: var(--brand); }
  h2 { font-size: 20px; margin: 0 0 24px 0; color: var(--muted); }

  /* Card blocks */
  .card {
    background: var(--card-bg);
    border-radius: var(--radius);
    padding: 18px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.45);
  }

  /* Footer: email + page counter */
  section::after {
    content: "";
  }
  /* Use Marp's paginate but also render a gentle footer */
  footer.marp-footer {
    position: absolute;
    right: 28px;
    bottom: 18px;
    font-size: 12px;
    color: var(--muted);
    opacity: 0.95;
  }
  footer.marp-email {
    position: absolute;
    left: 28px;
    bottom: 18px;
    font-size: 12px;
    color: var(--muted);
    opacity: 0.95;
  }

  /* Small code + pre style */
  pre, code {
    background: rgba(255,255,255,0.03);
    border-radius: 8px;
    padding: 8px;
    font-family: Menlo, Monaco, "Courier New", monospace;
    font-size: 13px;
  }

---

<!-- _class: title -->
# Product Documentation — SDK v1.0
### Maintainable, version-controlled slides for engineers & stakeholders

24f3000719@ds.study.iitm.ac.in

<footer class="marp-email">24f3000719@ds.study.iitm.ac.in</footer>
<footer class="marp-footer">Slide <!-- Marp paginate will show numbers; keep this line for layout parity --></footer>

---

<!-- _class: center -->
## Goals
- Keep docs **single-source-of-truth** in Git.
- Make slides **exportable** (PDF, PPTX, HTML).
- Provide code + math + visuals for engineers.

---

<!-- background: url('https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1950&q=80') center / cover -->
<!-- _class: center middle -->
# Architecture Overview
<p class="card">
This slide uses a full-bleed background image (Unsplash). The foreground card keeps content readable.
</p>

---

## Installation (code)
```bash
# Install the SDK
pip install mycompany-sdk==1.0.0

# Quick test
python -c "import mycompany; print(mycompany.__version__)"
