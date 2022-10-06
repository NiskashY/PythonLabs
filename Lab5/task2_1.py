import numpy as np
import math
from matplotlib import pyplot as plt

x = 3.567

def CalculateFunction(a):
    y = 1 / np.tan(x ** 3) + 2.24 * a * x
    return y


step = 0.75
min_a = 3.5
max_a = 25.6

function_values = []
function_arguments = []

for item in np.arange(min_a, max_a, step):
    function_arguments.append(item)
    function_values.append(CalculateFunction(item))

for i in range(len(function_values)):
    print(f"a = {function_arguments[i]} => y = {function_values[i]}")


min_el = min(function_values)
max_el = max(function_values)
avg_el = np.average(function_values)
print(f"Min element = {min_el}")
print(f"Max element = {max_el}")
print(f"Avg element = {avg_el}")

cp_values = function_values.copy()
cp_values.sort(reverse=True)
print("Before sort:", function_values)
print("After  sort:", cp_values)


plt.plot(function_arguments, function_values)
plt.plot(function_arguments, [avg_el for i in np.arange(min_a, max_a, step)])

plt.title("Task #20")
plt.xlabel("Argument x")
plt.ylabel("Value f(x)")

plt.legend(loc="lower right", labels=[f"ctg(x ^ 3) + {2.24 * x}  * x", "average"])
plt.axis([3.5, 26, 0, 150])

plt.grid()
plt.show()
