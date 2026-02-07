## 🧩 ŠABLONA – Gaussova eliminace

```python
import numpy as np

# 1) definice matice A a vektoru b
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

b = np.array([8, -11, -3], dtype=float)


# 2) Gaussova eliminace
def gauss_elimination(A, b):
    n = len(b)
    # přední eliminace
    for i in range(n):
        # pivot
        if A[i,i] == 0:
            raise ValueError("Pivot je nulový, potřebná výměna řádků")
        for j in range(i+1, n):
            m = A[j,i] / A[i,i]
            A[j] -= m * A[i]
            b[j] -= m * b[i]
    
    # zpětná substituce
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]
    return x


# 3) výpočet
x = gauss_elimination(A, b)

# 4) výpis výsledku
print("Řešení soustavy:", x)
```

---

## 🧠 Jak to použít na zkoušce

* Změníš **A** a **b** podle zadání.
* Funkce zvládne soustavy malé až střední velikosti (typicky 2–5 rovnic).

---

## ⚠️ Typické zkouškové chyby

* nulový pivot → potřeba výměna řádků
* zapomenutá zpětná substituce
* chybný index při dot produktu `np.dot(A[i,i+1:], x[i+1:])`
* chyba při typové konverzi (např. `int` místo `float`)

---

## 🔁 Varianty a tipy

* malou soustavu (2–3 rovnice) lze dělat **i ručně**, kód jen pro kontrolu
* pro větší soustavy se často používá **numpy.linalg.solve(A,b)**

Napiš číslo a pokračujeme 👌
