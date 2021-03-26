import math
from functools import reduce
import PythonAdventure.Haskell

class vector:
    arr = []

    def __str__(self):
        ret = "( "
        for x in (self.arr):
            ret += str(x) + " "
        return ret + ")"
    
    def __init__(self, vec): 
        assert isinstance(vec, list)
        assert len(vec) != 0 
        assert isinstance(vec[0], (int, float))
        self.arr = vec
    # Addition
    # Post: return v1 + v2
    def __add__(self, v2):
        return vector(list(map(lambda x: x[0] + x[1], list(zip(self.arr, v2.arr)))))
  
    # Scalar Multiplication (*)
    # Post: return c * v1
    def __mul__(self, c):
        #assert isinstance(c, (int, float, vector))
        if isinstance(c, (int, float)):
            return vector(list(map(lambda x: x * c, self.arr)))
        if isinstance(c, vector):
            return reduce(lambda acc, z: acc + z[0] * z[1], list(zip(self.arr, c.arr)), 0.0)
        if isinstance(c, Matrix):
            return Matrix([self.arr])*c

    def __rmul__(self, c):
        return self.__mul__(c)
    # Substraction
    # Post: return v1 - v2
    def __sub__(self, v2):
        return self + v2 * (-1.0)
    # Magnitude
    # Post: return ||v1||
    def magnitude(self):
        return math.sqrt(self*self)
    def toRow(self):
        return Matrix([self.arr])
    def toCol(self):
        return Matrix(list(map(lambda x: [x], self.arr)))


class Matrix:
    arr = []
    n = 0; m = 0 # Matrix n by m
    def __init__(self, arr):
        assert isinstance(arr, list)
        self.n = len(arr)
        assert self.n != 0
        self.m = len(arr[0])
        assert all(map(lambda xs: self.m == len(xs), arr))
        #assert isinstance(arr[0][0], (float, int))
        self.arr = arr
    
    def __str__(self):
        ret = ""
        for xs in self.arr:
            ret += str(vector(xs)) + "\n"
        return ret
    
    def T(self):
        return Matrix(list(map(list, (zip(*self.arr)))))


    def __mul__(self, a):
        assert isinstance(a, (vector, Matrix, int, float))
        if isinstance(a, (int, float)):
            new_arr = self.arr
            for i in range(self.n):
                for j in range(self.m):
                    new_arr[i][j] *= a
            return Matrix(new_arr)    

        if isinstance(a, vector):
            B = a.toCol()
        else:
            B = a
        B = B.T()
        assert self.m == B.m
        return Matrix(list(map(lambda xs : list(map(lambda ys: vector(xs) * vector(ys), self.arr)), B.arr)))

    def __rmul__(self, a):
        if isinstance(a, (int, float)):
            return self * a
        return NotImplemented
    
    def __add__(self, B):
        assert isinstance(B, Matrix) & B.n == self.n & self.m == B.m
        new_arr = self.arr
        for i in range(self.n):
            for j in range(self.m):
                new_arr += B.arr[i][j]
        return Matrix(new_arr)

    def __sub__(self, B):
        assert isinstance(B, Matrix) & (B.n == self.n & self.m == B.m)
        new_arr = self.arr
        for i in range(self.n):
            for j in range(self.m):
                new_arr -= B.arr[i][j]
        return Matrix(new_arr)
        

        
        

            
A = Matrix([[1, 2, 3], [2, 3, 4]])
B = Matrix([[1, 2], [2, 3], [3, 4]])
c = vector([1, 2, 3])
fib = Matrix([[1, 1], [1, 0]])
scalar = 12.1
scc = 3.141592
