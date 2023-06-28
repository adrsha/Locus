

def multiply(x, y):
    return x*y


print(multiply(4, 2))  # for repeatitive tasks


def greetings(x):
    print("Good morning,", x)
    # No commas when using format specifiers
    print("Good morning again, %s" % x)
    print(f"Good morning again, {x}")  # Using f'string
    print("Good morning again, {}".format(x))  # using format function


def sum(x, y):
    result = x+y
    print(f"Sum is, {result}")  # Using f'string


sum(10, 12)
