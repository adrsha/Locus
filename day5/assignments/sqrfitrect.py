import math
no_of_rects = int(input("Enter the no of rectangles! "))

w = int(input("What is the width of those rectangles"))
l = int(input("What is the length of those rectangles"))

low = 0
high = no_of_rects*l*w
while abs(high-low) > 0.00001:
    mid = (low+high)/2
    if (mid**2 >= no_of_rects * l * w):
        high = mid
    else:
        low = mid
print("The smallest integer size of the square needed is: ", math.ceil(mid))
