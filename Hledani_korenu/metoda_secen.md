## 🧩 ŠABLONA – Metoda sečen

```python
import math

# 1) definice funkce f(x)
def f(x):
    # TODO: uprav podle zadání
    return x**3 - x - 1


# 2) metoda sečen
def secant(f, x0, x1, eps=1e-6, max_iter=1000):
    for _ in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)

        if abs(f1 - f0) < 1e-12:
            raise ValueError("Dělení nulou v metodě sečen")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        if abs(x2 - x1) < eps:
            return x2

        x0, x1 = x1, x2

    return x1


# 3) počáteční odhady
x0 = 1
x1 = 2
eps = 1e-6

# 4) výpočet
root = secant(f, x0, x1, eps)

# 5) výpis výsledku
print("Aproximace kořene:", root)
print("Hodnota f(root):", f(root))
```

---

## 🧠 Jak ji poznáš v zadání

Typické formulace:

* „Použijte metodu sečen…“
* „Použijte metodu bez výpočtu derivace…“
* „Jsou dány dva počáteční odhady…“

👉 Když **nemáš derivaci**, ale **máš dva body**, sečny jsou správná volba.

---

## ⚠️ Typické zkouškové chyby

* záměna pořadí `x0`, `x1`
* zapomenutá kontrola dělení nulou
* ukončení podle `f(x)` místo rozdílu iterací
* příliš špatné počáteční body → divergence

---

## 🆚 Rychlé srovnání

* **Půlení** → jistota, pomalé
* **Sečny** → rychlejší, bez derivace
* **Newton** → nejrychlejší, ale riskantní

---
