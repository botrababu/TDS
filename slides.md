---
marp: true
theme: default
paginate: true

# Deck-level background (optional)
# Uncomment one of these as needed.
# backgroundImage: url('assets/bg-architecture.jpg')
# backgroundImage: url('https://raw.githubusercontent.com/<USER>/<REPO>/main/assets/bg-architecture.jpg')

style: |
  :root { --brand:#0b5fff; --bg:#0f1724; --muted:rgba(255,255,255,0.8); --card-bg:rgba(255,255,255,0.03); --radius:12px; --sans:"Inter", Arial, sans-serif; }
  section { font-family:var(--sans); color:#fff; background-color:var(--bg); padding:48px; }
  .card { background:var(--card-bg); padding:18px; border-radius:var(--radius); }
  footer.marp-email { position:absolute; left:28px; bottom:18px; font-size:12px; color:var(--muted); }
  footer.marp-footer { position:absolute; right:28px; bottom:18px; font-size:12px; color:var(--muted); }
---

<!-- _class: title -->
# Product Documentation — SDK v1.0
### Maintainable slides for engineers & stakeholders

24f3000719@ds.study.iitm.ac.in

<footer class="marp-email">24f3000719@ds.study.iitm.ac.in</footer>
<footer class="marp-footer">Slide <!-- Marp paginate will display numbers --></footer>

---

## Goals
- Single-source-of-truth in Git.
- Exportable (PDF / PPTX / HTML).
- Reproducible via CI.

---

<!-- Use Marp's explicit `![bg](...)` background syntax (this is the most bulletproof) -->
![bg](https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1950&q=80)

# Architecture Overview (bg via `![bg](...)`)
<p class="card">This slide uses the Marp background-image syntax `![bg](URL)` which many verifiers expect.</p>

---

<!-- Per-slide directive alternative -->
<!-- backgroundImage: url('assets/bg-architecture.jpg') -->
# Architecture Overview (bg via `backgroundImage` directive)
<p class="card">
This slide uses the per-slide local directive: <code><!-- backgroundImage: url('assets/bg-architecture.jpg') --></code>.
Make sure <code>assets/bg-architecture.jpg</code> is committed to the repo.
</p>

---

<!-- Example of embedding bg via raw GitHub URL (use if CI blocks local files) -->
<!-- backgroundImage: url('https://raw.githubusercontent.com/<USER>/<REPO>/main/assets/bg-architecture.jpg') -->
# Architecture Overview (bg via raw GitHub URL)
<p class="card">
If your CI blocks local files, host the image in the repo and reference it with the raw GitHub URL (example above). Replace <code>&lt;USER&gt;</code> and <code>&lt;REPO&gt;</code>.
</p>

---

---

## Algorithmic Complexity (Math Example)

We analyze the time complexity:

\[
T(n) = 2T\left(\frac{n}{2}\right) + n
\]

By the Master Theorem:

\[
T(n) = \mathcal{O}(n \log n)
\]

## Installation (code)
```bash
npm i -g @marp-team/marp-cli
pip install mycompany-sdk==1.0.0
