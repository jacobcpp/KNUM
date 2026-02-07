# **Souhrnný přehled numerických metod**

| Bod | Metoda                                         | Typ                       | Kdy použít                                       | Python / poznámka                                             |
| --- | ---------------------------------------------- | ------------------------- | ------------------------------------------------ | ------------------------------------------------------------- |
| 1   | Primitivní (Riemannova, lichoběžníky, Simpson) | Numerická integrace       | Když chceš spočítat $\(\int_a^b f(x) dx)\$           | Lichoběžníky a Simpson = standard na zkoušku                  |
| 2   | Metoda lichoběžníků                            | Numerická integrace       | Rychlá aproximace integrálu                      | `np.trapz` nebo ručně smyčka                                  |
| 3   | Metoda Simpsonova                              | Numerická integrace       | Přesnější než lichoběžníky                       | Parabolická aproximace                                        |
| 4   | Dopředná diference                             | Numerická derivace        | Když potřebuješ (f'(x)) a znáš jen hodnoty f(x)  | `(f(x+h)-f(x))/h`                                             |
| 5   | Zadní diference                                | Numerická derivace        | Alternativa dopředné, horší přesnost             | `(f(x)-f(x-h))/h`                                             |
| 6   | Středová diference                             | Numerická derivace        | Přesnější než dopředná / zadní                   | `(f(x+h)-f(x-h))/(2*h)`                                       |
| 7   | Gaussova eliminace                             | Přímé řešení soustav      | Řešení (Ax=b) přímo                              | Eliminace na horní trojúhelník + zpětná substituce            |
| 8   | LU faktorizace                                 | Přímé řešení soustav      | Více pravých stran (b), efektivní                | Rozklad $\(A = L \cdot U)\$, pak dopředná + zpětná substituce     |
| 9   | Jacobiho metoda                                | Iterativní řešení soustav | Diagonálně dominantní soustavy                   | Iterace do konvergence                                        |
| 10  | Gauss-Seidel                                   | Iterativní řešení soustav | Rychlejší než Jacobi                             | Aktualizace x přímo během iterace                             |
| 11  | Eulerova metoda                                | ODE                       | Řešení $\(y' = f(t,y))\$ s počáteční podmínkou       | Jednoduchá iterace $\(y_{n+1}=y_n+h f(t_n,y_n))\$                 |
| 12  | Runge-Kutta 4. řádu (RK4)                      | ODE                       | Přesnější než Euler                              | Kombinace k1,k2,k3,k4, stabilní a přesná                      |
| 13  | Lagrangeova interpolace                        | Interpolace               | Interpolace mezi několika body                   | Součin členů $\(\prod (x-x_j)/(x_i-x_j))\$                        |
| 14  | Lineární interpolace                           | Interpolace               | Rychlá aproximace mezi 2 body                    | $\(y = y_0 + (y_1-y_0)/(x_1-x_0)*(x-x_0))\$                       |
| 15  | Regula Falsi (falešná poloha)                  | Kořeny funkcí             | Hledání (f(x)=0) v intervalu s opačnými znaménky | $\(c = (a f(b) - b f(a)) / (f(b)-f(a)))\$, iterace do konvergence |

---

### ✅ Rychlé tipy, kdy co použít

* **Integrace:** Lichoběžníky (rychle) / Simpson (přesněji)
* **Derivace:** Dopředná (jednoduchá), středová (přesnější)
* **Soustavy (Ax=b):**

  * Malá, jednorázová → Gaussova eliminace
  * Více pravých stran → LU faktorizace
  * Iterativní, diagonálně dominantní → Jacobi / Gauss-Seidel
* **ODE:** Euler (rychlá kontrola), RK4 (přesně)
* **Interpolace:** Lagrange (více bodů), lineární (2 body)
* **Kořeny funkcí:**

  * Interval znám → Regula Falsi (stabilní)
  * Rychlá konvergence možná → Newton-Raphson (pokud znáš derivaci)


# **Numerické metody – one-page**

| Metoda                            | Typ                 | Vzorec / princip                                                  | Kdy použít                                     |
| --------------------------------- | ------------------- | ----------------------------------------------------------------- | ---------------------------------------------- |
| **Lichoběžníky**                  | Integrace           | $\int_a^b f(x) , dx \approx \frac{h}{2} \sum (f(x_i)+f(x_{i+1}))$ | Rychlá aproximace integrálu                    |
| **Simpsonova**                    | Integrace           | Parabolická aproximace přes intervaly                             | Přesnější integrace než lichoběžníky           |
| **Dopředná diference**            | Derivace            | $f'(x) \approx \frac{f(x+h)-f(x)}{h}$                             | Jednoduchá derivace                            |
| **Zadní diference**               | Derivace            | $f'(x) \approx \frac{f(x)-f(x-h)}{h}$                             | Alternativa dopředné                           |
| **Středová diference**            | Derivace            | $f'(x) \approx \frac{f(x+h)-f(x-h)}{2h}$                          | Přesnější derivace                             |
| **Gaussova eliminace**            | Přímé řešení $Ax=b$ | Horní trojúhelník + zpětná substituce                             | Malé až střední soustavy                       |
| **LU faktorizace**                | Přímé řešení $Ax=b$ | $A = L U$, dopředná + zpětná substituce                           | Více pravých stran, efektivní                  |
| **Jacobi**                        | Iterativní řešení   | $x_i^{k+1} = \frac{b_i - \sum_{j \neq i} A_{ij} x_j^k}{A_{ii}}$   | Diagonálně dominantní soustavy                 |
| **Gauss-Seidel**                  | Iterativní řešení   | Aktualizace $x$ během iterace                                     | Rychlejší než Jacobi                           |
| **Euler**                         | ODE                 | $y_{n+1} = y_n + h f(t_n, y_n)$                                   | Rychlá kontrola ODE                            |
| **Runge-Kutta 4. řádu (RK4)**     | ODE                 | Kombinace $k_1, k_2, k_3, k_4$                                    | Přesné řešení ODE                              |
| **Lagrange**                      | Interpolace         | $L(x) = \sum y_i \prod_{j \neq i} \frac{x-x_j}{x_i-x_j}$          | Interpolace mezi více body                     |
| **Lineární**                      | Interpolace         | $y = y_0 + \frac{y_1-y_0}{x_1-x_0}(x-x_0)$                        | Interpolace mezi 2 body                        |
| **Regula Falsi (falešná poloha)** | Kořeny funkcí       | $c = \frac{a f(b) - b f(a)}{f(b)-f(a)}$                           | Hledání kořene v intervalu s opačnými znaménky |

---

### 🔹 Rychlé tipy

1. **Integrace:** Lichoběžníky = rychle, Simpson = přesně
2. **Derivace:** Dopředná = jednoduchá, středová = přesnější
3. **Soustavy $Ax=b$:**

   * Malé → Gaussova eliminace
   * Více pravých stran → LU faktorizace
   * Iterativní → Jacobi / Gauss-Seidel
4. **ODE:** Euler = kontrola, RK4 = přesně
5. **Interpolace:** 2 body = lineární, více = Lagrange
6. **Kořeny funkcí:** Regula Falsi = stabilní, Newton-Raphson = rychle (pokud znám derivaci)


