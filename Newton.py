import numpy as np
import loss_functions as loss
import sys


def magnitude(w):
    return np.sqrt(w.dot(w))

class GradientDescent:
    tol = np.longdouble(10**(-8))          # tolerance
    N = 10                          # Maximal number of iterations
    armijo = 10**(-4) - 10**(-1)    # Armijo rule
    initial_step = 15.0             # Initial Step
    ro = 0.5                        # Exp. Backtracking constant

    def __init__(self, func):
        self.f = func.f; self.df = func.df;
        self.good = func.good; self.Hessian = func.H


    def classic(self, g):
        return (-1) * g

    def CD(self, g_n, g, d):
        return np.double(-1)*g_n + (g_n - g).dot(g_n)/g.dot(g) * d

    def Newton(self, x, g):
        return (-1) * np.linalg.solve(self.Hessian(x), g)

    # Gradient descent with backtracking
    # Post: return x* s.t. f(x*) = min f(x)
    def Run(self, st):
        return self.Run(st, "Classic")
    def Run(self, st, type, n):
        toPlot = open("VacationProject/toPlot.csv", "w")
        toPlot.write("Iteration;Accuracy\n")
        self.N = n
        f = self.f; df = self.df;  armijo = self.armijo
        x = st; step = self.initial_step; good = self.good

        fval = f(x); g = df(x); d = (-1)*g
        initial_gradient = magnitude(g)
        n = 0
        while n < self.N:
            x_new = x + step*d
            fval_new = f(x_new)
            while fval_new > fval + armijo*step*(g.dot(d)):
                step = step * self.ro
                x_new = x + step*d
                fval_new = f(x_new)
            n += 1
            toPlot.write(str(n) + ";"+ str(good(x_new)) + "\n")
            g_new = df(x_new);
            if type in ["Newton", "N", "newton", "n"]:
                d_new = self.Newton(x_new, g_new)
            elif type in ["Conjugate", "C", "c", "conjugate"]:
                d_new = self.CD(g_new, g, d)
            else:
                d_new = self.classic(g_new)

            step *= (g.dot(d))/(g_new.dot(d_new))
            g = g_new; d = d_new; x = x_new; fval = fval_new
            if magnitude(g) < self.tol * (1.0 + initial_gradient):
                break
        toPlot.close()
        if(n == self.N):
            print("Warning: GD achieved maximal number of iterations that equals to " + str(self.N))
        return x

"""
zero = np.zeros(137)
F = loss.function1()
gd = GradientDescent(F)
x = gd.Run(zero, "N", 5)
print("Accuracy: " + str(F.good(x)*100) + "%")
f = open("VacationProject/result.out", "w")
f.write("[")
for i in range(137):
    f.write("\t" + str(x[i]))
    if i == 136:
        f.write(" ]\n")
    else:
        f.write(" ,\n")
f.close()
"""
