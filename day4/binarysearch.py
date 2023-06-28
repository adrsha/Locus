stri = int(input("Enter your string:"))
x = int(input("Enter your value to search"))

#
found = False
while not found:
    index = int(len(stri)/2)
    if (int(x) == int(stri[index])):
        found = True
        print(a[])
    else:
        if (int(x) < int(str[index])):
            str = str[:index]
        elif (int(x) > int(str[index])):
            str = str[index+1:]

# left = 0
# right = len(a) - 1
#
# while left <= right:
#     mid == (left+right)//2
#     if a[midj] == search_value:
#          print("Searched element is at index", mid)
#          break
#      elif a[mid]
