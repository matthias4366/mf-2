import numpy as np

a = np.array([[3, 2, 1], [3, 4, 7], [4, 5, 6]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)

print('x')
print(x)
