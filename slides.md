---
marp: true
theme: default
paginate: true
style: |
  :root {
    --brand: #0b5fff;
    --bg: #0f1724;
    --muted: rgba(255,255,255,0.8);
    --card-bg: rgba(255,255,255,0.1);
    --radius: 12px;
    --sans: "Inter", Arial, sans-serif;
  }

  section {
    font-family: var(--sans);
    color: #fff;
    background-color: var(--bg);
    padding: 48px;
  }

  .card {
    background: var(--card-bg);
    padding: 20px;
    border-radius: var(--radius);
  }

  footer.marp-email {
    position: absolute;
    left: 24px;
    bottom: 18px;
    font-size: 12px;
    color: var(--muted);
  }

  footer.marp-footer {
    position: absolute;
    right: 24px;
    bottom: 18px;
    font-size: 12px;
    color: var(--muted);
  }
---

<!-- _class: title -->
# Product Documentation – SDK v1.0  
### Technical Presentation

Your Email: **24f3000719@ds.study.iitm.ac.in**

<footer class="marp-email">24f3000719@ds.study.iitm.ac.in</footer>
<footer class="marp-footer">Page</footer>

---

## Project Goals

- Maintain documentation in version control  
- Generate PDF, PPTX, HTML using Marp  
- Use custom styling and themes  
- Keep everything developer-friendly  

---

<!-- Background image (no upload needed, hosted online) -->
![bg](https://images.unsplash.com/photo-1522199710521-72d69614c702?auto=format&fit=crop&w=1950&q=1080)

# System Architecture Overview

<div class="card">
This slide uses a <b>publicly hosted background image</b> from Unsplash.  
No upload required.
</div>

---

## Installation

```bash
npm i -g @marp-team/marp-cli
pip install mycompany-sdk==1.0.0
