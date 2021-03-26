import functools as ft


def foldl(c, n, xs):
    ret = n
    for x in xs:
        ret = c(ret, x)
    return ret

def foldr(c, n, xs):
    ret = n
    ys = xs.reverse()
    for y in ys:
        ret = c(y, ret)
    return ret

def zipWith(f, xs, ys): [f(a, b) for (a, b) in list(zip(xs, ys))]

def scanl(c, n, xs):
    ret = [n]
    value = n
    for x in xs:
        value = c(value, x)
        ret.append(value)
    return ret

def scanr(c, n, xs):
    ret = [n]
    value = n
    ys = xs.reverse()
    for y in ys:
        value = c(y, value)
        ret.append(value)
    return ret.reverse()

def Map(f, xs): list(map(f, xs))
def Zip(xs, ys): list(zip(xs, ys))

def compose(f, g):
        return lambda x : f(g(x))

def composite_function(*func):         
    return ft.reduce(compose, func, lambda x : x)