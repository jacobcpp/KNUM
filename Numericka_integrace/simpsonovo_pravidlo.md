## 🧩 ŠABLONA – Simpsonovo pravidlo

```python
import math

# 1) definice funkce f(x)
def f(x):
    # TODO: uprav podle zadání
    return math.sin(x)


# 2) Simpsonovo pravidlo
def simpson(f, a, b, n):
    # n MUSÍ být sudé
    if n % 2 != 0:
        raise ValueError("n musí být sudé")

    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)

    return s * h / 3


# 3) meze integrace a počet dílků (sudý!)
a = 0
b = math.pi
n = 1000

# 4) výpočet
I = simpson(f, a, b, n)

# 5) výpis výsledku
print("Aproximace integrálu:", I)
```

---

## 🧠 Jak to použít na zkoušce

Změníš jen:

* `f(x)`
* meze `a`, `b`
* **sudé** `n`

Zbytek necháš.

---

## ⚠️ Typické zkouškové chyby (VELMI ČASTÉ)

❌ `n` liché
❌ špatné koeficienty 4–2–4–2
❌ zapomenuté dělení `/ 3`
❌ `range(1, n+1)` místo `range(1, n)`

---

## 🆚 Kdy Simpson brát

* když je v zadání „vyšší řád“
* když chtějí **přesnější výsledek**
* když není metoda určena (a chceš zazářit)
