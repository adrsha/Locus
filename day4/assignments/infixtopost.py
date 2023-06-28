usr = input("Enter your expression.")
# usr = input("Enter your expression.").replace(" ", "").replace(
#     "+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ")
operators = "/*+-"
opStack = []
numStack = []

opIndex = 0

for i, o in enumerate(usr):
    if o in operators:
        opStack.append([i, o])

# find the highest precedence operator
# solve the no's there
# find another precedence and solve those
