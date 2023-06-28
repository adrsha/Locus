
# fx = x3 - x + 2

low = -5
high = 5


def func(x):
    return x**3 - x + 2


while low <= high:
    mid = (low+high)/2
    func_value = func(mid)
    if (abs(func_value) < 0.00001):
        print("The value is :", mid)
        break
    elif func_value < 0:
        low = mid
    else:
        high = mid
