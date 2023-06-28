
print(sum([2, 3]))  # sums a list
sum = 7
print(sum)  # NO ERRORS!
# print(sum([4, 5]))  # ERROR!

# Best practice: Dont change global variables


x = 10


def mod_no():
    x = 20


mod_no()  # This doesnt change the variable value as this only changes the new "x" that exists inside the funcn mod_no
print(x)
