## 1️⃣ Řešení nelineárních rovnic ( f(x)=0 )

### 🔹 Metoda půlení intervalu (bisection)

**Kdy:**

* když je dána spojitá funkce
* víš, že ( f(a)\cdot f(b) < 0 )

**Proč se objevuje na zkouškách:**

* extrémně jednoduchá
* vždy konverguje

**Algoritmus (kostra):**

```python
def bisection(f, a, b, eps=1e-6):
    while b - a > eps:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2
```

---

### 🔹 Newtonova metoda

**Kdy:**

* máš derivaci ( f'(x) )
* chceš rychlou konvergenci

**Typické zadání:**
„Použijte Newtonovu metodu k nalezení kořene rovnice…“

```python
def newton(f, df, x0, eps=1e-6):
    x = x0
    while abs(f(x)) > eps:
        x = x - f(x)/df(x)
    return x
```

⚠️ Pozor na:

* špatný počáteční odhad
* nulovou derivaci

---

### 🔹 Metoda sečen (secant)

**Výhoda:**

* nepotřebuje derivaci
* často kompromis mezi Newtonem a půlením

```python
def secant(f, x0, x1, eps=1e-6):
    while abs(f(x1)) > eps:
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0, x1 = x1, x2
    return x1
```

---

## 2️⃣ Numerická integrace

### 🔹 Obdélníkové pravidlo

Nejjednodušší forma, často jen „na rozjezd“.

```python
def rectangle(f, a, b, n):
    h = (b - a) / n
    return sum(f(a + i*h) for i in range(n)) * h
```

---

### 🔹 Lichoběžníkové pravidlo

Velmi časté u zkoušek.

```python
def trapezoidal(f, a, b, n):
    h = (b - a) / n
    s = 0.5*(f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return s * h
```

---

### 🔹 Simpsonovo pravidlo

Trochu složitější, ale **hodně oblíbené**.

```python
def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i % 2 == 1 else 2
        s += coef * f(a + i*h)
    return s * h / 3
```

⚠️ `n` musí být **sudé**

---

## 3️⃣ Numerické derivování

### 🔹 Dopředná / středová diference

```python
def derivative(f, x, h=1e-5):
    return (f(x+h) - f(x-h)) / (2*h)
```

Typické použití:

* aproximace derivace
* součást Newtonovy metody

---

## 4️⃣ Lineární soustavy ( Ax = b )

### 🔹 Gaussova eliminace

Základní klasika. Někdy chtějí **ruční implementaci**.

```python
import numpy as np

def gauss(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    for i in range(n):
        for j in range(i+1, n):
            m = A[j,i] / A[i,i]
            A[j] -= m * A[i]
            b[j] -= m * b[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]
    return x
```

---

### 🔹 Iterační metody (lehčí varianta)

#### Jacobiho metoda

```python
def jacobi(A, b, x0, it=100):
    n = len(b)
    x = x0.copy()
    for _ in range(it):
        x_new = x.copy()
        for i in range(n):
            s = sum(A[i][j]*x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        x = x_new
    return x
```

---

## 5️⃣ Obyčejné diferenciální rovnice (ODE)

### 🔹 Eulerova metoda

Absolutní základ, skoro jistota na zkoušce.

```python
def euler(f, x0, y0, h, n):
    x, y = x0, y0
    for _ in range(n):
        y = y + h * f(x, y)
        x = x + h
    return x, y
```

---

### 🔹 Runge-Kutta 4. řádu (RK4)

Trochu delší, ale **extrémně populární**.

```python
def rk4(f, x0, y0, h, n):
    x, y = x0, y0
    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
    return x, y
```

---

## 6️⃣ Aproximace a interpolace

### 🔹 Lagrangeova interpolace

Čistá matematika + kód.

```python
def lagrange(x, xs, ys):
    s = 0
    n = len(xs)
    for i in range(n):
        p = ys[i]
        for j in range(n):
            if i != j:
                p *= (x - xs[j])/(xs[i] - xs[j])
        s += p
    return s
```
