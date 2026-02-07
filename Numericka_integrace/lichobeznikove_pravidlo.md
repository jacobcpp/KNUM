## 🧩 ŠABLONA – Lichoběžníkové pravidlo

```python
import math

# 1) definice funkce f(x)
def f(x):
    # TODO: uprav podle zadání
    return math.sin(x)


# 2) lichoběžníkové pravidlo
def trapezoidal(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x = a + i * h
        s += f(x)

    return s * h


# 3) meze integrace a počet dílků
a = 0
b = math.pi
n = 1000

# 4) výpočet
I = trapezoidal(f, a, b, n)

# 5) výpis výsledku
print("Aproximace integrálu:", I)
```

---

## 🧠 Jak to poznáš v zadání

Typické formulace:

* „Použijte lichoběžníkové pravidlo…“
* „Numericky vypočtěte integrál…“

👉 Pokud **není metoda explicitně určena**, lichoběžníky jsou **bezpečná volba**.

---

## ⚠️ Typické zkouškové chyby

* zapomenutý faktor `0.5` u krajních bodů
* cyklus `range(n+1)` místo `range(1, n)`
* špatně spočítané `h`
* příliš malé `n`

---

## 🆚 Rychlé srovnání

* obdélníky → nejjednodušší
* **lichoběžníky → standard**
* Simpson → vyšší přesnost
