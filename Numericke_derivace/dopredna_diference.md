## 🧩 ŠABLONA – Dopředná diference

```python
import math

# 1) definice funkce f(x)
def f(x):
    # TODO: uprav podle zadání
    return math.sin(x)


# 2) dopředná diference
def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


# 3) bod, ve kterém derivujeme
x = 1.0
h = 1e-5

# 4) výpočet derivace
df = forward_difference(f, x, h)

# 5) výpis výsledku
print("Aproximace derivace f'(x):", df)
```

---

## 🧠 Jak to poznáš v zadání

Typické formulace:

* „Aproximujte derivaci funkce v bodě…“
* „Použijte dopřednou diferenci…“
* „Numericky určete f′(x)…“

👉 Když **není řečeno jinak**, dopředná diference je **nejjednodušší volba**.

---

## 📏 Volba kroku `h`

* typicky: `1e-4` až `1e-6`
* příliš malé `h` → numerický šum
* příliš velké `h` → nepřesnost

Na zkoušce klidně:

```python
h = 1e-5
```

---

## ⚠️ Typické zkouškové chyby

* zapomenuté dělení `h`
* použití `(f(x+h)-f(x-h))` → to už **není** dopředná
* `h = 0`
* derivace v bodě mimo definiční obor

---

## 🔁 Časté použití

* když **není analytická derivace**
* jako součást **Newtonovy metody**
* rychlá kontrola výsledku

Napiš číslo a pokračujeme 👌
