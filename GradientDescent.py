import LinearAlgebra as LA
import Haskell as fp
import math
import random
#import np.random.uniform



class GradientDescent:
    tol = float(10**(-10))          # tolerance
    N = 300                          # Maximal number of iterations
    armijo = 10**(-4) - 10**(-1)    # Armijo rule
    initial_step = 10000.0             # Initial Step
    ro = 0.5                        # Exp. Backtracking constant

    def f(self, x): return  sum(x.arr)    # function to be optimized
    def df(self, x): return LA.vector(x)  # derivative of f
        

    def __init__(self, f_, df_):
        self.f = f_; self.df = df_


    # Gradient descent with backtracking
    # Post: return x* s.t. f(x*) = min f(x)
    def Run(self, st):
        f = self.f; df = self.df;  armijo = self.armijo
        x = st; step = self.initial_step
       
        fval = f(x); g = df(x); d = (-1)*g
        initial_gradient = g.magnitude()
        n = 0
        while n < self.N:
            x_new = x + step*d
            #print(str(x_new))
            print(str(f(x_new)))
            fval_new = f(x_new)
            while fval_new > fval + armijo*step*(g*d):
                step = step * self.ro
                x_new = x + step*d
                fval_new = f(x_new)
            n += 1
            g_new = df(x_new); d_new = (-1) * g_new
            step *= (g*d)/(g_new*d_new)
            g = g_new; d = d_new; x = x_new; fval = fval_new
            if g.magnitude() < self.tol * (1.0 + initial_gradient):
                break
        if(n == self.N):
            print("Warning: GD achieved maximal number of iterations that equals to " + str(self.N))
        return x


ys = []
yfile = open("vectorY", "r")
for y in yfile:
    ys.append(int(y))
yfile.close()

xss = []
xfile = open("matrixX", "r")
for line in xfile.readlines():
    xs = []
    for x in line.split('\t'):
        xs.append(float(x))
    xss.append(xs)
xfile.close() 
print(str(len(xss)))  

N = 2000

def f(w):
    ret = 0.0
    for i in range(N):
        x = LA.vector(xss[i])
        try:
            exp = math.exp(-ys[i] * (w * x))
        except OverflowError:
            exp = float('inf')
        ret += exp
    return ret

def df(w):
    ret = LA.vector([0.0]*137)
    for i in range(N):
        x = LA.vector(xss[i])
        try:
            exp = math.exp(-ys[i] * (w * x))
        except OverflowError:
            exp = float('inf')
        ret += exp * (-ys[i])*x
    return ret


def good(w):
    cnt = 0
    for i in range(N):
        if  ys[i] * w * LA.vector(xss[i]) > 0:
            cnt += 1
    return str(float(cnt)*100.0/float(N)) + "%"
zero = LA.vector([0.00]*137)
gd = GradientDescent(f, df)
x = gd.Run(zero)
#print(str(x))
print(good(x))
