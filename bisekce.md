## 🧩 ŠABLONA – Metoda půlení intervalu

```python
import math

# 1) definice funkce f(x)
def f(x):
    # TODO: uprav podle zadání
    return x**3 - x - 1


# 2) metoda půlení intervalu
def bisection(f, a, b, eps=1e-6, max_iter=1000):
    # kontrola podmínky
    if f(a) * f(b) > 0:
        raise ValueError("Na intervalu [a,b] není zaručen kořen")

    for _ in range(max_iter):
        m = (a + b) / 2

        if abs(f(m)) < eps or (b - a) / 2 < eps:
            return m

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

    return (a + b) / 2


# 3) zadání intervalu a přesnosti
a = 1
b = 2
eps = 1e-6

# 4) výpočet
root = bisection(f, a, b, eps)

# 5) výpis výsledku
print("Aproximace kořene:", root)
print("Hodnota f(root):", f(root))
```

---

## 🧠 Jak to použít na zkoušce

Stačí změnit:

* **funkci `f(x)`**
* **interval `[a, b]`**
* případně **`eps`**

Všechno ostatní necháš být.

---

## ⚠️ Typické zkouškové chyby

* zapomenutá podmínka `f(a)*f(b) < 0`
* nekonečný `while` bez limitu iterací
* návrat `a` nebo `b` místo středu
* příliš malé `eps` → zbytečně dlouhý běh

---

## 📝 Co když zadání chce výpis iterací?

Stačí do smyčky přidat např.:

```python
print(_, m, f(m))
```
