import numpy as np
import bisect as bi

# NPV funkce
def NPV(i, CF, K):
    n = len(CF)
    return sum(CF[t] / (1 + i)**(t + 1) for t in range(n)) - K

def bisection(CF, K, a, b, tol=1e-6, max_iter=100):
    fa = NPV(a, CF, K)
    fb = NPV(b, CF, K)

    if fa * fb > 0:
        raise ValueError("V intervalu není změna znaménka.")
    cntr = 0
    for _ in range(max_iter):
        m = (a + b) / 2
        fm = NPV(m, CF, K)

        if abs(fm) < tol:
            print(f"Iterations: {cntr}")
            return m

        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
        cntr+=1

    print(f"Iterations: {cntr}")
    return (a + b) / 2

def regula_falsi(CF, K, a, b, tol=1e-6, max_iter=100):
    fa = NPV(a, CF, K)
    fb = NPV(b, CF, K)

    if fa * fb > 0:
        raise ValueError("V intervalu není změna znaménka.")

    for _ in range(max_iter):
        i = a - fa * (b - a) / (fb - fa)
        fi = NPV(i, CF, K)

        if abs(fi) < tol:
            return i

        if fa * fi < 0:
            b = i
            fb = fi
        else:
            a = i
            fa = fi

    return i

CF = [-8,4,4,4]  # cash flow
K = 0            # počáteční investice

a = 0.1    # 0 %
b = 0.3    # 50 %

i_bis = bisection(CF, K, a, b)
i_rf  = regula_falsi(CF, K, a, b)

print(f"Bisection: i = {i_bis:.6f}")
print(f"Regula falsi: i = {i_rf:.6f}")

