## 🧩 ŠABLONA – Lineární interpolace

```python
import numpy as np

# 1) zadání bodů (x_i, y_i)
x_points = np.array([0, 1, 2], dtype=float)
y_points = np.array([1, 3, 2], dtype=float)

# 2) lineární interpolace mezi body
def linear_interpolation(x_points, y_points, x):
    # najdi interval, ve kterém leží x
    for i in range(len(x_points) - 1):
        if x_points[i] <= x <= x_points[i+1]:
            # lineární vzorec: y = y0 + (y1-y0)/(x1-x0)*(x-x0)
            x0, x1 = x_points[i], x_points[i+1]
            y0, y1 = y_points[i], y_points[i+1]
            return y0 + (y1 - y0) / (x1 - x0) * (x - x0)
    # pokud x je mimo interval
    raise ValueError("x je mimo rozsah bodů")

# 3) bod, ve kterém chceme odhadnout hodnotu
x = 1.5

# 4) výpočet interpolované hodnoty
y = linear_interpolation(x_points, y_points, x)

# 5) výpis výsledku
print(f"Interpolovaná hodnota v x={x}: y ≈ {y:.6f}")
```

---

## 🧠 Jak to poznáš v zadání

* „Najděte hodnotu mezi dvěma body lineární interpolací“
* Počet bodů: 2 (nebo několik pro různé intervaly)

---

## ⚠️ Typické zkouškové chyby

* zapomenutý vzorec `(y1 - y0)/(x1 - x0)`
* špatně vybraný interval
* pokus o interpolaci mimo zadané body bez ošetření
* přepsání proměnné `x0`, `y0`

---

## 🔁 Tipy

* Malé soustavy dat → ideální metoda
* Více bodů → použít **krok po kroku** mezi každým intervalem
* Pokud potřebuješ graf → vypočítat pro více `x` bodů a spojit čarou
