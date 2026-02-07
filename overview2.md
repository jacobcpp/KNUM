# **Numerické metody – prehled**

| Metoda                            | Typ                 | Vzorec / princip                                          | Kdy použít                                     |
| --------------------------------- | ------------------- | --------------------------------------------------------- | ---------------------------------------------- |
| **Lichoběžníky**                  | Integrace           | (\int_a^b f(x) dx ≈ \frac{h}{2} \sum (f(x_i)+f(x_{i+1}))) | Rychlá aproximace integrálu                    |
| **Simpsonova**                    | Integrace           | Parabolická aproximace                                    | Přesnější integrace než lichoběžníky           |
| **Dopředná diference**            | Derivace            | (f'(x) ≈ (f(x+h)-f(x))/h)                                 | Jednoduchá derivace                            |
| **Zadní diference**               | Derivace            | (f'(x) ≈ (f(x)-f(x-h))/h)                                 | Alternativa dopředné                           |
| **Středová diference**            | Derivace            | (f'(x) ≈ (f(x+h)-f(x-h))/(2h))                            | Přesnější derivace                             |
| **Gaussova eliminace**            | Přímé řešení (Ax=b) | Horní trojúhelník + zpětná substituce                     | Malé až střední soustavy                       |
| **LU faktorizace**                | Přímé řešení (Ax=b) | (A = L U), dopředná + zpětná substituce                   | Více pravých stran, efektivní                  |
| **Jacobi**                        | Iterativní řešení   | (x_i^{k+1} = (b_i - \sum_{j≠i} A_{ij} x_j^k)/A_{ii})      | Diagonálně dominantní soustavy                 |
| **Gauss-Seidel**                  | Iterativní řešení   | Aktualizace x během iterace                               | Rychlejší než Jacobi                           |
| **Euler**                         | ODE                 | (y_{n+1} = y_n + h f(t_n, y_n))                           | Rychlá kontrola ODE                            |
| **Runge-Kutta 4. řádu (RK4)**     | ODE                 | Kombinace k1,k2,k3,k4                                     | Přesné řešení ODE                              |
| **Lagrange**                      | Interpolace         | (L(x) = \sum y_i \prod_{j≠i} (x-x_j)/(x_i-x_j))           | Interpolace mezi více body                     |
| **Lineární**                      | Interpolace         | (y = y_0 + (y_1-y_0)/(x_1-x_0)*(x-x_0))                   | Interpolace mezi 2 body                        |
| **Regula Falsi (falešná poloha)** | Kořeny funkcí       | (c = (a f(b) - b f(a)) / (f(b)-f(a)))                     | Hledání kořene v intervalu s opačnými znaménky |

---

### 🔹 Rychlé tipy

1. **Integrace:** Lichoběžníky = rychle, Simpson = přesně
2. **Derivace:** Dopředná = jednoduchá, středová = přesnější
3. **Soustavy (Ax=b):**

   * Malé → Gaussova eliminace
   * Více pravých stran → LU faktorizace
   * Iterativní → Jacobi / Gauss-Seidel
4. **ODE:** Euler = kontrola, RK4 = přesně
5. **Interpolace:** 2 body = lineární, více = Lagrange
6. **Kořeny funkcí:** Regula Falsi = stabilní, Newton-Raphson = rychle (pokud znám derivaci)
