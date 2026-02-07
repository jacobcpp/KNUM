import numpy as np
from scipy.optimize import root

# Reduced pressure
def Pr(Vr, Tr):
    return 8*Tr/(3*Vr - 1) - 3/(Vr**2)

# dPr/dVr
def dPr_dVr(Vr, Tr):
    return -24*Tr/(3*Vr - 1)**2 + 6/(Vr**3)

# Choose reduced temperature (try Tr < 1)
Tr = 0.9

# Initial guesses for extrema
initial_guesses = [0.6, 1.5]

extrema = []

for guess in initial_guesses:
    sol = root(dPr_dVr, guess, args=(Tr,))
    if sol.success:
        Vr_ext = sol.x[0]
        Pr_ext = Pr(Vr_ext, Tr)
        extrema.append((Vr_ext, Pr_ext))

# Remove duplicates (Newton can converge twice to same root)
extrema = list(set([tuple(np.round(e, 6)) for e in extrema]))

print("Extrema (Vr, Pr):")
for e in extrema:
    print(e)


import matplotlib.pyplot as plt

Vr_vals = np.linspace(0.35, 3, 1000)
Pr_vals = Pr(Vr_vals, Tr)

plt.plot(Vr_vals, Pr_vals)
for Vr_ext, Pr_ext in extrema:
    plt.plot(Vr_ext, Pr_ext, 'ro')

plt.xlabel("Vr")
plt.ylabel("Pr")
plt.title(f"Van der Waals Isotherm (Tr = {Tr})")
plt.grid()
plt.legend()

plt.savefig("vdw_isotherm.png", dpi=300, bbox_inches="tight")
plt.close()


import numpy as np
from scipy.optimize import root

Tr = 0.89

def dPr_dVr(Vr):
    return -24*Tr/(3*Vr - 1)**2 + 6/(Vr**3)

def Pr(Vr):
    return 8*Tr/(3*Vr - 1) - 3/(Vr**2)

# počáteční odhady (kapalná a plynná větev)
guesses = [0.6, 1.5]

extrema = []

for g in guesses:
    sol = root(dPr_dVr, g)
    if sol.success:
        Vr = sol.x[0]
        extrema.append((Vr, Pr(Vr)))

# odstranění duplicit
extrema = list(set([tuple(np.round(e, 6)) for e in extrema]))

for Vr, Pr_val in extrema:
    print(f"Vr = {Vr}, Pr = {Pr_val}")

    import numpy as np
from scipy.optimize import root

Tr = 0.89

def d2Pr_dVr2(Vr):
    return 144*Tr/(3*Vr - 1)**3 - 18/(Vr**4)

sol = root(d2Pr_dVr2, 1.0)  # počáteční odhad kolem 1

Vr_inf = sol.x[0]

def Pr(Vr):
    return 8*Tr/(3*Vr - 1) - 3/(Vr**2)

Pr_inf = Pr(Vr_inf)

print(f"Vr_inf = {Vr_inf:.6f}")
print(f"Pr_inf = {Pr_inf:.6f}")

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

Tr = 0.89

# tlak
def Pr(Vr):
    return 8*Tr/(3*Vr - 1) - 3/(Vr**2)

# 1. derivace
def dPr_dVr(Vr):
    return -24*Tr/(3*Vr - 1)**2 + 6/(Vr**3)

# 2. derivace
def d2Pr_dVr2(Vr):
    return 144*Tr/(3*Vr - 1)**3 - 18/(Vr**4)

# --- výpočet bodů ---
# extrémy
guesses_ext = [0.6, 1.5]
extrema = []

for g in guesses_ext:
    sol = root(dPr_dVr, g)
    if sol.success:
        Vr = sol.x[0]
        extrema.append((Vr, Pr(Vr)))

# odstranění duplicit
extrema = list(set([tuple(np.round(e, 6)) for e in extrema]))

# inflexní bod
sol_inf = root(d2Pr_dVr2, 1.0)
Vr_inf = sol_inf.x[0]
Pr_inf = Pr(Vr_inf)

# --- vykreslení ---
Vr_vals = np.linspace(0.35, 3.0, 1200)
Pr_vals = Pr(Vr_vals)

plt.figure(figsize=(7, 5))
plt.plot(Vr_vals, Pr_vals, label=r"$T_r = 0.89$")

# extrémy
for Vr_e, Pr_e in extrema:
    plt.plot(Vr_e, Pr_e, "ro", label="extrém")

# inflexní bod
plt.plot(Vr_inf, Pr_inf, "ks", label="inflexní bod")

plt.xlabel(r"$V_r$")
plt.ylabel(r"$P_r$")
plt.title("Van der Waalsova izoterma (redukované veličiny)")
plt.grid()
plt.legend()

plt.xlim(0, 3)
plt.ylim(0, 1.6)

plt.savefig("vdw_isotherm_Tr_0p89.png", dpi=300, bbox_inches="tight")
plt.close()


from scipy.optimize import root_scalar
from scipy.integrate import quad

Tr = 0.89

def Pr(Vr):
    return 8*Tr/(3*Vr - 1) - 3/(Vr**2)

Vl, Vg = 0.716, 1.63

def area_diff(P0):
    integral, _ = quad(lambda Vr: Pr(Vr) - P0, Vl, Vg)
    return integral

# metoda, která nemusí mít různé znaménko:
sol = root_scalar(area_diff, x0=0.36, x1=0.37, method='secant')
Psat = sol.root

print(f"Rovnovážný tlak (Maxwellova konstrukce): P_r = {Psat:.6f}")


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from scipy.integrate import quad

# -------------------------
# parametry
Tr = 0.89

# tlak
def Pr(Vr):
    return 8*Tr/(3*Vr - 1) - 3/(Vr**2)

# 1. derivace
def dPr_dVr(Vr):
    return -24*Tr/(3*Vr - 1)**2 + 6/(Vr**3)

# 2. derivace
def d2Pr_dVr2(Vr):
    return 144*Tr/(3*Vr - 1)**3 - 18/(Vr**4)

# -------------------------
# extrémy
guesses_ext = [0.6, 1.5]
extrema = []
for g in guesses_ext:
    sol = root_scalar(dPr_dVr, x0=g, x1=g+0.1, method='secant')
    if sol.converged:
        Vr = sol.root
        extrema.append((Vr, Pr(Vr)))

# odstranění duplicit
extrema = list(set([tuple(np.round(e, 6)) for e in extrema]))

# inflexní bod
sol_inf = root_scalar(d2Pr_dVr2, x0=1.0, x1=1.1, method='secant')
Vr_inf = sol_inf.root
Pr_inf = Pr(Vr_inf)

# -------------------------
# Maxwellova konstrukce
# extrémní objemy
Vl, Vg = extrema[0][0], extrema[1][0]

def area_diff(P0):
    integral, _ = quad(lambda Vr: Pr(Vr) - P0, Vl, Vg)
    return integral

# rovnovážný tlak (numericky)
sol_psat = root_scalar(area_diff, x0=0.35, x1=0.36, method='secant')
Psat = sol_psat.root

# -------------------------
# vykreslení
Vr_vals = np.linspace(0.35, 3.0, 1200)
Pr_vals = Pr(Vr_vals)

plt.figure(figsize=(8,5))
plt.plot(Vr_vals, Pr_vals, label=r"$T_r = 0.89$")

# extrémy
for Vr_e, Pr_e in extrema:
    plt.plot(Vr_e, Pr_e, "ro", label="extrém" if Vr_e==extrema[0][0] else "")

# inflexní bod
plt.plot(Vr_inf, Pr_inf, "ks", label="inflexní bod")

# Maxwellova přímka
plt.hlines(Psat, Vl, Vg, colors='b', linestyles='--', label=r"Maxwellova přímka")

# popisky
plt.xlabel(r"$V_r$")
plt.ylabel(r"$P_r$")
plt.title("Van der Waalsova izoterma a Maxwellova konstrukce")
plt.grid()
plt.xlim(0,3)
plt.ylim(0,1.6)
plt.legend()

plt.savefig("vdw_isotherm_Tr_0p89_maxwell.png", dpi=300, bbox_inches="tight")
plt.close()

print(f"Rovnovážný tlak (Maxwell): P_r = {Psat:.6f}")
