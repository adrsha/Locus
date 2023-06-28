def russian_roulette(name, shots=4):
    print(f"You, {name} are shot {shots} many times")


database = [
    "Adarsh", "Ashwin", "Abinash", "Bijen"
]
for n in database:
    russian_roulette(n)


def facto(num):
    f = 1
    for i in range(1, num+1):
        f = f*i
    return f


print(facto(4))
