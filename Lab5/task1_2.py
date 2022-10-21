import numpy as np
import random

column_first = [1 for index in range(12)]
column_second = [random.randint(20, 32) for index in range(12)]
column_third = [random.randint(60, 82) for index in range(12)]

X_T = np.array([column_first, column_second, column_third])
X = np.transpose(X_T.copy())
print("\nX:\n",X)
print("\nX_T:\n", X_T)

Y = (np.array([random.uniform(13.5, 18.6) for index in range(12)]))

print("\nY:\n", Y)

multiple_first = X_T.copy().dot(X)
multiple_second = X_T.copy().dot(Y)
multiple_first = np.linalg.inv(multiple_first.copy())
A = multiple_first.dot(multiple_second)

print("\nA:\n", A)

checked = np.add(np.add(A[0], A[1] * X_T[1]), A[2] * X_T[2])
print("\nmatrix check:\n", checked)

