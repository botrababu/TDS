---
marp: true
theme: default
paginate: true
style: |
  /* --- Custom theme variables --- */
  :root{
    --brand: #0b5fff;
    --bg: #0f1724;
    --muted: rgba(255,255,255,0.8);
    --card-bg: rgba(255,255,255,0.03);
    --radius: 12px;
    --sans: "Inter", "Helvetica Neue", Arial, sans-serif;
  }
  section { font-family: var(--sans); color: #fff; background-color: var(--bg); padding: 48px; }
  section.title { padding: 72px; }
  h1 { color: var(--brand); font-size: 48px; margin: 0 0 8px 0; }
  h2 { color: var(--muted); margin: 0 0 16px 0; }
  .card { background: var(--card-bg); padding: 18px; border-radius: var(--radius); }
  footer.marp-email { position: absolute; left: 28px; bottom: 18px; font-size: 12px; color: var(--muted); }
  footer.marp-footer { position: absolute; right: 28px; bottom: 18px; font-size: 12px; color: var(--muted); }
---

<!-- _class: title -->
# Product Documentation — SDK v1.0
### Maintainable, version-controlled slides for engineers & stakeholders

24f3000719@ds.study.iitm.ac.in

<footer class="marp-email">24f3000719@ds.study.iitm.ac.in</footer>
<footer class="marp-footer">Slide <!-- paginate provided by Marp --></footer>

---

## Goals
- Single-source-of-truth in Git
- Exportable (PDF / PPTX / HTML)
- Reproducible builds via CI

---

<!-- Background slide using an absolute URL (guaranteed to render if CI allows external images) -->
<!-- background: url('https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1950&q=80') center / cover -->
<!-- _class: center middle -->
# Architecture Overview (external image)
<p class="card">
This slide uses a full-bleed background image from Unsplash. Use absolute URLs or put images under `assets/` in the repo.
</p>

---

<!-- Background slide using a repo-local image.
     Make sure the file `assets/bg-architecture.jpg` exists in your repository (commit it).
     Many CI validators require images to be stored in-repo rather than external hotlinks. -->
<!-- background: url('assets/bg-architecture.jpg') center / cover -->
<!-- _class: center middle -->
# Architecture Overview (local image)
<p class="card">
This uses a **local** image at `assets/bg-architecture.jpg`. Store the image in your repo to ensure the slide renderer / verifier can access it during CI.
</p>

---

## Installation
```bash
npm i -g @marp-team/marp-cli
pip install mycompany-sdk==1.0.0
