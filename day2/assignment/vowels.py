sentence = input("What'd you have to say?")
c = 0
for w in sentence:
    if w in "aeiou":
        c += 1

print(f"You've total {c} vowels")
