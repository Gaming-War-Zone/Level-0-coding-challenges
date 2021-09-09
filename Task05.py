import math

def area_triangle(a, b, c):
    s = ( a + b + c )/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

area_triangle(23,14,8)
