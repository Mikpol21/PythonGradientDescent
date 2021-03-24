# Gradient Descent with backtracking
import Haskell
import LinearAlgebra
from LinearAlgebra import vector


def f(x): return x**x
def df(x): return vector(list(map(lambda y: 2* y, x.arr)))
def swap(a, b):
    temp = a
    a = b
    b = temp

def GradientDescent():
    start = vector([10.0, 10.0, 10.0, 10.0])
    tol = float(10**(-16))
    N = 10  # Maximal number of iterations
    sigma = 10**(-4) - 10**(-1)

    x = start   # x :: vector
    g = df(x)   # g :: vector
    cntrl = g.magnitude()
    d = g * (-1)     # d :: vector
    curr = f(x)    # f :: scalar
    alpha = 10.0
    n = 0
    while n < N:
        n += 1
        xn = x + alpha*d
        fn = f(xn)
        while fn >= curr + (g ** d) * (sigma * alpha):
            alpha = 0.5 * alpha
            xn = x + d * alpha
            fn = f(xn)
        gn = df(xn)
        dn = gn * (-1)
        print("n = " + str(n) + ": x(n) = " + str(xn) + ", d(n) = " + str(dn))
        print(str(d**g) + " " + str(dn**gn))
        alpha *= (d**g)/(dn**gn)
        if gn.magnitude() <= tol * (1 + cntrl):
            break
        x = xn
        curr = fn
        d = dn
        g = gn
    return x


x = GradientDescent()
print("Min = " + str(x))
print("anf f(x) = " + str(f(x)))



