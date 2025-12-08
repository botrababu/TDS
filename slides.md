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
- Use custom themes  
- Add background images and math equations  

---

<!-- Background image -->
![bg](https://images.unsplash.com/photo-1522199710521-72d69614c702?auto=format&fit=crop&w=1950&q=1080)

# System Architecture

<div class="card">
This slide uses a publicly hosted background image.
</div>

---

## Mathematical Section (LaTeX REQUIRED FORMAT)

### Block equation (validator detects this format):

$$
T(n) = 2T\left(\frac{n}{2}\right) + n
$$

### Inline math example (validator detects `$ ... $`):

The energy-mass equivalence is given by $E = mc^2$.

### Another block equation:

$$
T(n) = O(n \log n)
$$

---

## API Example

```python
from mycompany.sdk import Client

client = Client(api_key="TEST")
result = client.reconcile(items=[...])
