st = input("Enter your number: ")
length = len(st)
arm = 0
for x in st:
    arm += int(x)**length

if arm == int(st):
    print("It is armstrong")
