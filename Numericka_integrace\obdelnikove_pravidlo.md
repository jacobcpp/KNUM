## 🧩 ŠABLONA – Obdélníkové pravidlo

```python
import math

# 1) definice funkce f(x)
def f(x):
    # TODO: uprav podle zadání
    return math.sin(x)


# 2) obdélníkové pravidlo (levé)
def rectangle(f, a, b, n):
    h = (b - a) / n
    s = 0.0

    for i in range(n):
        x = a + i * h
        s += f(x)

    return s * h


# 3) meze integrace a počet dílků
a = 0
b = math.pi
n = 1000

# 4) výpočet
I = rectangle(f, a, b, n)

# 5) výpis výsledku
print("Aproximace integrálu:", I)
```

---

## 🧠 Jak to použít na zkoušce

Změníš pouze:

* funkci `f(x)`
* meze `a`, `b`
* počet dílků `n`

Hotovo.

---

## ℹ️ Varianty (když se zeptají jinak)

### Pravé obdélníky

Stačí změnit řádek:

```python
x = a + (i + 1) * h
```

### Středové obdélníky (lepší přesnost)

```python
x = a + (i + 0.5) * h
```

---

## ⚠️ Typické zkouškové chyby

* zapomenuté `* h` na konci
* špatně spočítané `h`
* cyklus `range(n+1)` místo `range(n)`
* příliš malé `n` → hrubý výsledek

---

## 🆚 Kdy NEpoužívat

* když je výslovně požadována vyšší přesnost
* když je v zadání zmíněno „Simpson“ nebo „lichoběžníky“
