## 🧩 ŠABLONA – Regula Falsi

Patří mezi metody pro hledání kořenů funkcí (f(x)=0) a je příbuzná metodě bisekce, ale místo středu intervalu používá lineární aproximaci průsečíku s osou x.

```python
import math

# 1) definice funkce f(x)
def f(x):
    # TODO: uprav podle zadání
    return x**3 - x - 2  # příklad

# 2) Regula Falsi
def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) a f(b) musí mít opačná znaménka")
    
    for _ in range(max_iter):
        # výpočet nového bodu podle regula falsi
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)

        # kontrola přesnosti
        if abs(fc) < tol:
            return c

        # výběr nového intervalu
        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c

# 3) interval, kde hledáme kořen
a = 1
b = 2

# 4) výpočet
root = regula_falsi(f, a, b)

# 5) výpis výsledku
print(f"Kořen rovnice f(x)=0 je x ≈ {root:.6f}")
```

---

### 🧠 Jak to poznáš v zadání

* „Najděte kořen funkce pomocí metody regula falsi“
* Musí být interval ([a, b]) s opačnými znaménky (f(a)\cdot f(b)<0)

---

### ⚠️ Typické chyby

* zvolit interval, kde f(a) a f(b) mají stejné znaménko
* špatný vzorec pro c
* zapomenutá kontrola tolerance `tol`

---

### 🔁 Tipy

* Stabilnější než metoda sekantová u nepravidelných funkcí
* Pomalejší konvergence než Newton-Raphson, ale **vždy konverguje, pokud existuje kořen v intervalu**
