from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x * np.log(x/0.75) + y * np.log(y/0.25)

x = np.linspace(0, 0.5, 100)
y = np.linspace(0, 0.5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 400, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
plt.show()
print(np.min(Z))