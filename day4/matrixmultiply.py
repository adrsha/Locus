
import numpy as np

size = 4

x = np.random.randn(size, size)
y = np.random.randn(size, size)
z = np.random.randn(size, size)

for i in range(size):
    for j in range(size):
        for k in range(size):
            z[i][j] += x[i][k] * y[k][j]
