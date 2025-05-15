#naq_ellipse


def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

import math


#(x_low, y_low) = (xc - a, yc - b)
#(x_high, y_high) = (xc + a, yc + b)

#distance from center to foci = sqrt((x2-x1)^2 + (y2-y1)^2)

#a = major axis / 2
#b = sqrt(a^2 - c^2)

#-5 0 5 0 16
#x1 y1 x2 y2 a

x1, y1, x2, y2, d = invr()

x_c = (x1 + x2) / 2
y_c = (y1 + y2) / 2

a = d / 2

c = math.sqrt((x2- x1)**2 + (y2-y1)**2) / 2

b = math.sqrt((a**2) - (c**2))


x_low, y_low, x_high, y_high = x_c - a, y_c - b, x_c + a, y_c + b

print(f"{x_low} {y_low} {x_high} {y_high}")






