## 🧩 ŠABLONA – Jacobiho metoda

```python
import numpy as np

# 1) definice matice A a vektoru b
A = np.array([[10, -1, 2, 0],
              [-1, 11, -1, 3],
              [2, -1, 10, -1],
              [0, 3, -1, 8]], dtype=float)

b = np.array([6, 25, -11, 15], dtype=float)

# 2) Jacobiho metoda
def jacobi(A, b, x0=None, eps=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.copy()
    x_new = np.zeros(n)

    for k in range(max_iter):
        for i in range(n):
            s = sum(A[i,j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i,i]

        if np.linalg.norm(x_new - x, ord=np.inf) < eps:
            return x_new

        x = x_new.copy()

    return x_new

# 3) počáteční odhad, přesnost
x0 = np.zeros(len(b))
eps = 1e-6

# 4) výpočet
x = jacobi(A, b, x0, eps)

# 5) výpis výsledku
print("Řešení soustavy (Jacobi):", x)
```

---

## 🧠 Jak to poznáš v zadání

* „Vyřešte soustavu iterativně metodou Jacobi…“
* Obvykle **malá diagonálně dominantní matice**
* Počet iterací `max_iter` a tolerance `eps` často zkouška toleruje

---

## ⚠️ Typické zkouškové chyby

* matice **není diagonálně dominantní** → metoda nemusí konvergovat
* zapomenutá kopie `x_new.copy()` → chyba při aktualizaci
* ukončení podle `x` místo rozdílu iterací
* příliš malé `eps` → zbytečně dlouhý běh

---

## 🔁 Tipy

* Pro malé soustavy (3–4 rovnice) 10–20 iterací obvykle stačí
* Pro stabilitu **vždy zkontroluj diagonální dominanci**:

  ```python
  all(abs(A[i,i]) > sum(abs(A[i,j]) for j in range(len(A)) if j!=i) for i in range(len(A)))
  ```
