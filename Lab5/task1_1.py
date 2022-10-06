import numpy as np

pi = np.pi
x = 1.59


numerator = np.sin(pi / 6) + np.sqrt((3 + x ** 2)) - (np.log10(x - 1)) ** 3
denominator = np.arcsin(x / 2)

print ("Value of equation =" , numerator / denominator);
