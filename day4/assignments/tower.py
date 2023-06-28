A = [1, 2, 3, 4, 5]
B = []
C = []


def move(stack_level, init, last):
    for i in stack_level:
        last.append(init.pop())


def moveSorted(n, init, unfinal, final):
    if (init[-1] == n):
        move(n, init, unfinal)
    else:
        moveSorted(n-1, init, unfinal)
        move(n, init, final)


def showData():
    print(A, B, C)


moveSorted(4, A, C, B)
