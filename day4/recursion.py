# def power(a, n):
#     if (n == 0):
#         return 1
#     else:
#         return a*power(a, n - 1)
#
#

# print(power(2, 0))
# reqd = 5
# def binsearch(i, a):
#     if (a == reqd):
#         return a
#     else:
#         i = len//2
#         a = a[i:]

vals = {}


def fibo(n):
    if (n in vals):
        return vals[n]
    else:
        if (n == 1) or (n == 2):
            return 1
        else:
            vals[n] = fibo(n-2) + fibo(n-1)
            return fibo(n-2) + fibo(n-1)


def fibo(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibo(n-2) + fibo(n-1)


print(fibo(52))
