import numpy as np
x = 3
np.array([1, 1, 1, 1])  # easy on memory
np.random.randn(x, x)  # an array of x by x
newList = np.random.randn(x, x)  # an array of x by x by x
newList2 = np.random.randn(x, x)  # an array of x by x by x
newSin = np.sin(x)
print(newList, newList2)
print(" ")
print(newList@newList2)  # matrix multiplication

y = np.random.randn(32).astype(float)
range_style = np.arange(101, dtype=np.float32)

# sliced = np.arange(101, dtype=np.float32)
# y[:10] = 0  # To replace all elements from 0 to 10 with 0
# print()
# print(np.pi)
# print(y == 0)
# any, all  # these are to check if all of the elements in array are true or if any is true
