no = [1, 2, 3, 4, 5]
length = len(no)
rev = []

rev = no[::-1]

for i in range(1, length+1):
    rev.append(no[-i])

for i in range(length):
    rev.append(no.pop())

print(rev)
