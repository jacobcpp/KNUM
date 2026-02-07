## 🧩 ŠABLONA – LU faktorizace

```python
import numpy as np
from scipy.linalg import lu, solve

# 1) definice matice A a vektoru b
A = np.array([[2, 1, 1],
              [4, -6, 0],
              [-2, 7, 2]], dtype=float)

b = np.array([5, -2, 9], dtype=float)

# 2) LU faktorizace
P, L, U = lu(A)  # A = P @ L @ U

# 3) řešení soustavy
# dopředná substituce: L y = P.T @ b
y = np.linalg.solve(L, P.T @ b)

# zpětná substituce: U x = y
x = np.linalg.solve(U, y)

# 4) výpis výsledku
print("Řešení soustavy (LU):", x)
```

---

### 🧠 Jak to poznáš v zadání

* „Vyřešte soustavu (Ax=b) pomocí LU faktorizace“
* Často se používá, když je **více pravých stran** (b_1, b_2,…)

---

### ⚠️ Typické chyby

* Zapomenutý pivot (někdy nutné použít `scipy.linalg.lu_factor`)
* Nesprávně řešená dopředná substituce
* Přepsání `x` místo uložení do nové proměnné

---

### 🔁 Tipy

* Pokud máš jen **jednu soustavu**, Gauss je rychlejší
* Pro více soustav → LU faktorizace šetří výpočty
