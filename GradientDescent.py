import LinearAlgebra as LA
import Haskell as fp


class GradientDescent:
    tol = float(10**(-16))          # tolerance
    N = 30                          # Maximal number of iterations
    armijo = 10**(-4) - 10**(-1)    # Armijo rule
    initial_step = 10.0             # Initail Step
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
        while n < N:
            x_new = x + step*d
            fval_new = f(x_new)
            while fval_new >= fval + armijo*step*(g*d):
                step = step * ro
                x_new = x + step*d
                fval_new = f(x_new)
            ++n
            g_new = df(x_new); d_new = (-1) * g_new
            step *= (g*d)/(g_new*d_new)
            g = g_new; d = d_new; x = x_new; fval = fval_new
            if g.magnitude() < tol * (1.0 + initial_gradient):
                break
        if(n == N):
            print("\e[31mWarning\e[0m: GD achieved maximal number of iterations that equals to" + N)
        return x


def f(x): return x*x           # function to be optimized
def df(x):                      # derivative of f
    return LA.vector(list(map(lambda y: 2.0 * y, x.arr)))

##gd = GradientDescent(f, df)
##x = gd.Run(LA.vector([10.0, 10.0, 10.0, 10.0]))
##print("x* = " + x + "\n\t f(x*) = " + gd.f(x))

