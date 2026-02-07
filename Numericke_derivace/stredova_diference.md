## 🧩 ŠABLONA – Středová diference

```python
import math

# 1) definice funkce f(x)
def f(x):
    # TODO: uprav podle zadání
    return math.sin(x)


# 2) středová diference
def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


# 3) bod, ve kterém derivujeme
x = 1.0
h = 1e-5

# 4) výpočet derivace
df = central_difference(f, x, h)

# 5) výpis výsledku
print("Aproximace derivace f'(x):", df)
```

---

## 🧠 Jak to poznáš v zadání

Typické formulace:

* „Aproximujte derivaci funkce v bodě pomocí středové diference“
* „Použijte centrální diferenci…“

👉 Pokud **jde o přesnější aproximaci** než dopředná, středová je volba číslo 1.

---

## 📏 Volba kroku `h`

* typicky: `1e-4` až `1e-6`
* příliš malé → numerický šum
* příliš velké → ztráta přesnosti

---

## ⚠️ Typické zkouškové chyby

* zaměnění pořadí `(x+h)` a `(x-h)`
* zapomenuté dělení `2*h`
* použití h=0
* derivace v bodě mimo definiční obor

---

## 🔁 Časté použití

* jako přesnější náhrada dopředné diference
* kontrola výsledků Newtonovy metody
* rychlá numerická derivace, když není analytická
