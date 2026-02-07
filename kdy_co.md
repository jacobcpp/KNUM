# 🧠 NUMERICKÉ METODY

## 🔍 Hledání kořene rovnice ( f(x)=0 )

### ❓ Zadání říká:

> „Najděte kořen rovnice…“

### 👉 Rozhodování:

* **Máš interval ([a,b]) a (f(a)f(b)<0)**
  ➜ **Metoda půlení**
* **Máš derivaci (f'(x))**
  ➜ **Newtonova metoda**
* **Nemáš derivaci, ale 2 počáteční body**
  ➜ **Metoda sečen**

| Metoda | Výhoda       | Nevýhoda        |
| ------ | ------------ | --------------- |
| Půlení | vždy funguje | pomalá          |
| Newton | velmi rychlá | může divergovat |
| Sečen  | bez derivace | méně stabilní   |

---

## ∫ Numerická integrace

### ❓ Zadání říká:

> „Numericky vypočtěte integrál…“

### 👉 Rozhodování:

* **Jen hrubý výpočet / jednoduché zadání**
  ➜ Obdélníkové
* **Standardní zkouškové zadání**
  ➜ **Lichoběžníkové**
* **Chce se přesnost / je zmíněno „vyšší řád“**
  ➜ **Simpsonovo pravidlo**

| Metoda       | Přesnost | Poznámka                |
| ------------ | -------- | ----------------------- |
| Obdélníky    | nízká    | skoro jistota že projde |
| Lichoběžníky | střední  | velmi časté             |
| Simpson      | vysoká   | `n` musí být sudé       |

---

## 📈 Numerická derivace

### ❓ Zadání říká:

> „Aproximujte derivaci…“

### 👉 Automatická volba:

➜ **Středová diference**

```python
(f(x+h) - f(x-h)) / (2*h)
```

📝 Často:

* součást Newtonovy metody
* když není analytická derivace

---

## 🧮 Lineární soustava ( Ax=b )

### ❓ Zadání říká:

> „Vyřešte soustavu lineárních rovnic…“

### 👉 Rozhodování:

* **Malá soustava (2–5 rovnic)**
  ➜ **Gaussova eliminace**
* **Je zmíněno „iteračně“**
  ➜ **Jacobi / Gauss-Seidel**

| Metoda       | Kdy ji vzít           |
| ------------ | --------------------- |
| Gauss        | klasika, rychlá       |
| Jacobi       | jednoduchá, pomalejší |
| Gauss-Seidel | rychlejší než Jacobi  |

⚠️ Pozor:

* diagonála nesmí být nulová
* ideálně diagonálně dominantní matice

---

## ⏱️ Diferenciální rovnice (ODE)

### ❓ Zadání říká:

> „Řešte diferenciální rovnici…“

### 👉 Rozhodování:

* **Úplný základ / krátké zadání**
  ➜ **Eulerova metoda**
* **Chce se přesnost / standardní metoda**
  ➜ **RK4**

| Metoda | Plus                | Mínus     |
| ------ | ------------------- | --------- |
| Euler  | extrémně jednoduchá | nepřesná  |
| RK4    | velmi přesná        | delší kód |

---

## 📐 Interpolace / aproximace

### ❓ Zadání říká:

> „Interpolujte hodnoty…“

### 👉 Volba:

* **Pár bodů (≤6)**
  ➜ **Lagrangeova interpolace**
* **Je zmíněno „polynom“**
  ➜ Lagrange skoro jistota

⚠️ Neplést:

* interpolace ≠ regrese
* polynom vždy prochází body

---

## 🚨 Typické zkouškové pasti

❌ zapomenuté `n` sudé u Simpsona
❌ Newton bez kontroly konvergence
❌ špatně zvolený krok `h`
❌ nekonečný `while` bez limitu iterací
❌ nulový prvek na diagonále u Gaussa

---
