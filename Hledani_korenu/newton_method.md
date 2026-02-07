## 🧩 ŠABLONA – Newtonova metoda(metoda tecen)

```python
import math

# 1) definice funkce f(x)
def f(x):
    # TODO: uprav podle zadání
    return x**3 - x - 1


# 2) definice derivace f'(x)
def df(x):
    # TODO: uprav podle zadání
    return 3*x**2 - 1


# 3) Newtonova metoda
def newton(f, df, x0, eps=1e-6, max_iter=1000):
    x = x0

    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-12:
            raise ValueError("Derivace je příliš blízká nule")

        x_new = x - fx / dfx

        if abs(x_new - x) < eps:
            return x_new

        x = x_new

    return x


# 4) počáteční odhad a přesnost
x0 = 1.5
eps = 1e-6

# 5) výpočet
root = newton(f, df, x0, eps)

# 6) výpis výsledku
print("Aproximace kořene:", root)
print("Hodnota f(root):", f(root))
```

---

## 🧠 Jak to použít na zkoušce

V 90 % případů stačí změnit:

* `f(x)`
* `df(x)`
* počáteční odhad `x0`

Zbytek necháš beze změny.

---

## ⚠️ Typické zkouškové chyby

* špatně spočítaná derivace
* počáteční bod daleko od kořene
* chybějící kontrola `df(x) ≈ 0`
* ukončení podle `f(x)` místo změny `x`

---

## 📝 Když **není derivace zadána**

Použij **numerickou derivaci** (často projde):

```python
def df(x, h=1e-5):
    return (f(x+h) - f(x-h)) / (2*h)
```

---

## 🆚 Kdy Newtona NEbrat

* funkce má zlomy / nespojitosti
* derivace se blíží nule
* špatný počáteční odhad

→ v tom případě je bezpečnější **metoda půlení**.
