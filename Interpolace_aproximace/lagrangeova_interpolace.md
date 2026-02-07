## 🧩 ŠABLONA – Lagrangeova interpolace

```python
import numpy as np

# 1) zadání bodů (x_i, y_i)
x_points = np.array([0, 1, 2], dtype=float)
y_points = np.array([1, 3, 2], dtype=float)

# 2) Lagrangeova interpolace
def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    L = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        L += term
    return L

# 3) bod, ve kterém chceme odhadnout hodnotu
x = 1.5

# 4) výpočet interpolované hodnoty
y = lagrange_interpolation(x_points, y_points, x)

# 5) výpis výsledku
print(f"Interpolovaná hodnota v x={x}: y ≈ {y:.6f}")
```

---

## 🧠 Jak to poznáš v zadání

* „Najděte interpolovanou hodnotu pomocí Lagrangeovy interpolace“
* Máš **několik bodů** a chceš hodnotu mezi nimi

---

## ⚠️ Typické zkouškové chyby

* zapomenuté `j != i` → chyba v součinu
* špatný index v `x_points[i] - x_points[j]`
* přepsání proměnné `term` místo sčítání do `L`
* velký počet bodů → numerická nestabilita (na zkoušce obvykle 3–5 bodů)

---

## 🔁 Tipy

* Malý počet bodů → použít přímo Lagrange
* Více bodů → raději **lineární nebo spline interpolace**
* Na graf → vypočítat pro více `x` bodů a vykreslit
