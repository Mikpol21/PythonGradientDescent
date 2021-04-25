import numpy as np

class function1:
    N = 2000
    ys = []
    xss = []
    # Initializing self.ys and self.xss
    def __init__(self):
        yfile = open("VacationProject/vectorY.in", "r")
        for y in yfile:
            self.ys.append(int(y))
        yfile.close()
        xfile = open("VacationProject/matrixX.in", "r")
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
        return (float(cnt)/float(self.N))



"""
    Not working
"""
class function2:
    N = 2000
    ys = []
    xss = []
    # Initializing self.ys and self.xss
    def __init__(self):
        yfile = open("VacationProject/vectorY.in", "r")
        for y in yfile:
            self.ys.append(int(y))
        yfile.close()
        xfile = open("VacationProject/matrixX.in", "r")
        for line in xfile.readlines():
            xs = []
            for x in line.split('\t'):
                xs.append(float(x))
            self.xss.append(xs)
        xfile.close()

    def good(self, w):
        cnt = 0
        for i in range(self.N):
            if  (self.ys[i]) * (w.dot(np.array(self.xss[i]))) > 0:
                cnt += 1
        return str(float(cnt)*100.0/float(self.N)) + "%"

    def EXP(self, x):
        return np.exp(-0.5 * x * x)

    def f(self, x):
        ret = np.double(0.0)
        for i in range(self.N):
            ret += np.double(self.ys[i]) * self.EXP(x.dot(np.array(self.xss[i])))
        return ret

    def df(self, x):
        ret = np.zeros(137)
        for i in range(self.N):
            a = np.array(self.xss[i])
            ret += np.double(-self.ys[i]) * self.EXP(x.dot(a)) * (x.dot(a)) * a
        return ret
    
    def H(self, x):
        ret = np.zeros((137, 137))
        for i in range(self.N):
            a = np.array(self.xss[i])
            a_ = np.array([self.xss[i]])
            ret += np.double(self.ys[i])*self.EXP(x.dot(a))*(x.dot(a)*x.dot(a) - 1.0) * a_.transpose() * a_
        return ret
