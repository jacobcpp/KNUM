## 🧩 ŠABLONA – Eulerova metoda

```python
import math

# 1) definice funkce f(t, y), která představuje dy/dt = f(t, y)
def f(t, y):
    # TODO: uprav podle zadání
    return y - t**2 + 1

# 2) Eulerova metoda
def euler(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    for _ in range(n):
        y = y + h * f(t, y)
        t = t + h

        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

# 3) počáteční podmínka a parametry
t0 = 0
y0 = 0.5
t_end = 2
n = 10  # počet kroků

# 4) výpočet
t_values, y_values = euler(f, t0, y0, t_end, n)

# 5) výpis výsledků
for t, y in zip(t_values, y_values):
    print(f"t = {t:.4f}, y ≈ {y:.6f}")
```

---

## 🧠 Jak to poznáš v zadání

* „Vyřešte ODE numericky pomocí Eulerovy metody“
* ODE ve tvaru ( \frac{dy}{dt} = f(t,y) )
* Počáteční hodnota (y(t_0) = y_0)

---

## ⚠️ Typické zkouškové chyby

* zapomenutý krok `h = (t_end - t0)/n`
* špatně aktualizované `t` nebo `y`
* výpis jen posledního bodu, když se chtějí **všechny** kroky
* příliš hrubý krok → velká chyba

---

## 🔁 Tipy

* Pro lepší přesnost → použij **RK4 (Runge-Kutta 4. řádu)**
* Euler je skvělý na **rychlé zkouškové výpočty**
* Na grafy → ukládat `t_values` a `y_values`
