import numpy as np
import sys

class function:
    N = 2000
    ys = []
    xss = []
    # Initializing self.ys and self.xss
    def __init__(self):
        yfile = open("vectorY", "r")
        for y in yfile:
            self.ys.append(int(y))
        yfile.close()
        xfile = open("matrixX", "r")
        for line in xfile.readlines():
            xs = []
            for x in line.split('\t'):
                xs.append(float(x))
            self.xss.append(xs)
        xfile.close() 

    def EXP(self, w, i):
         x = np.array(np.longdouble(self.xss[i]))
         return np.exp(np.longdouble(-self.ys[i])  * (w.dot(x)))

    def f(self, w):
        ret = 0.0
        for i in range(self.N):
            ret += self.EXP(w, i)
        return ret

    def df(self, w):
        ret = np.array([0.0]*137)
        for i in range(self.N):
            x = np.array(self.xss[i])
            ret += self.EXP(w, i) *  np.longdouble(-self.ys[i]) * x
        return ret

    def H(self, w):
        ret = np.zeros((137, 137))
        for i in range(self.N):
            x = np.array([self.xss[i]])
            ret += self.EXP(w, i) * (x.transpose()@x)
        return ret


    def good(self, w):
        cnt = 0
        for i in range(self.N):
            if  (self.ys[i]) * (w.dot(np.array(self.xss[i]))) > 0:
                cnt += 1
        return str(float(cnt)*100.0/float(self.N)) + "%"


def magnitude(w):
    return np.sqrt(w.dot(w))

class GradientDescent:
    tol = np.longdouble(10**(-8))          # tolerance
    N = 30                          # Maximal number of iterations
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
            print(str(n) + ": " + str(f(x_new)) + " , " + good(x_new))
            g_new = df(x_new); 
            d_new = self.classic(g_new)
            step *= (g.dot(d))/(g_new.dot(d_new))
            g = g_new; d = d_new; x = x_new; fval = fval_new
            if magnitude(g) < self.tol * (1.0 + initial_gradient):
                break
        if(n == self.N):
            print("Warning: GD achieved maximal number of iterations that equals to " + str(self.N))
        return x

zero = np.zeros(137)
F = function()
gd = GradientDescent(F)
x = gd.Run(zero)
print(x)