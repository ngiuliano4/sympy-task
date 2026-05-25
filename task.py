import sympy
from typing import Dict

# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str,variabile: str) -> sympy.Expr:
    import sympy as sp
    x = sp.Symbol('x')
    y = espressione
    yd = sp.diff(y, x)
    return yd
    pass

def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float) -> sympy.Expr:
    from sympy import integrate
    valore= integrate(espressione, (variabile, estremo_inf, estremo_sup))
    return valore
    pass

def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    from sympy import limit
    valore=limit(espressione,variabile,punto)
    return valore
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    from sympy import symbols, series
    x = symbols('x')
    expr = series(espressione, variabile,punto,ordine)
    return expr
    pass
d
ef risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:

    pass

def main():
    print("Sub-task 1:", calcola_derivata("4*x+5", "x"))
    print("Sub-task 2:", calcola_integrale_definito("4*x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("(g**2 - 1)/(g - 1)", "g", "1"))
    print("Sub-task 4:", calcola_polinomio_taylor("cos(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
