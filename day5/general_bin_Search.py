import numpy as np
x = (np.random.rand(1)*100)  # one random number
y = (np.random.rand(10)*100)  # 10 random numbers
y.sort()
y = y <= 60

low = 0
high = (len(y)/2).ceil()
