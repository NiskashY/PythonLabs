import numpy as np
import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def CalcX_025(x, y):
    z = x ** 0.25 + y * 0.25
    return z


def CalcX_2(x, y):
    z = x ** 2 - y ** 2
    return z


def Calc2X(x, y):
    z = 2 * x + 3 * y
    return z


def CalcX_2_plus(x, y):
    z = x ** 2 + y ** 2
    return z


def CalcLong(x, y):
    z = 2 + 2 * x + 2 * y - CalcX_2_plus(x, y)
    return z


min_x = min_y = 0
max_x = max_y = 4
step = 0.5


arguments = [item for item in np.arange(min_x, max_x + 0.1, step)]
v_1 = np.array([CalcX_025(item, item) for item in np.arange(min_x, max_x + 0.1, step)]) # v - values
v_2 = np.array([CalcX_2(item, item) for item in np.arange(min_x, max_x + 0.1, step)]) # v - values
v_3 = np.array([Calc2X(item, item) for item in np.arange(min_x, max_x + 0.1, step)]) # v - values
v_4 = np.array([CalcX_2_plus(item, item) for item in np.arange(min_x, max_x + 0.1, step)]) # v - values
v_5 = np.array([CalcLong(item, item) for item in np.arange(min_x, max_x + 0.1, step)]) # v - values


fig = plt.figure(figsize=(len(arguments), len(arguments)))# Create 3D container
ax = plt.axes(projection='3d')# Visualize 3D scatter plot
ax.plot3D(arguments, arguments, v_1)# Give labels
ax.plot3D(arguments, arguments, v_2)# Give labels
ax.plot3D(arguments, arguments, v_3)# Give labels
ax.plot3D(arguments, arguments, v_4)# Give labels
ax.plot3D(arguments, arguments, v_5)# Give labels

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# Save figure
plt.savefig('3d_scatter.png', dpi = 300);
plt.show()
