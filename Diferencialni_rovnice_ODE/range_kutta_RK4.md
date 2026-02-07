## 🧩 ŠABLONA – Runge-Kutta 4. řádu (RK4)

```python
import math

# 1) definice funkce f(t, y), která představuje dy/dt = f(t, y)
def f(t, y):
    # TODO: uprav podle zadání
    return y - t**2 + 1

# 2) Runge-Kutta 4. řádu
def rk4(f, t0, y0, t_end, n):
    h = (t_end - t0) / n
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
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
t_values, y_values = rk4(f, t0, y0, t_end, n)

# 5) výpis výsledků
for t, y in zip(t_values, y_values):
    print(f"t = {t:.4f}, y ≈ {y:.6f}")
```

---

## 🧠 Jak to poznáš v zadání

* „Vyřešte ODE metodou Runge-Kutta 4. řádu“
* ODE ve tvaru ( \frac{dy}{dt} = f(t,y) )
* Počáteční hodnota (y(t_0) = y_0)

---

## ⚠️ Typické zkouškové chyby

* špatně spočítané k1–k4 (např. chybný posun `h/2`)
* zapomenutý dělenec `/6`
* špatně aktualizované `t` nebo `y`
* příliš hrubý počet kroků → menší přesnost

---

## 🔁 Tipy

* RK4 je standardní volba pro přesnější numerické řešení ODE
* Euler se hodí pro rychlou kontrolu výsledku
* Pro graf → použít `t_values` a `y_values`
