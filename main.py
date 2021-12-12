#Задача 1
a = int(input())
def sqr(a):
    n =  a**2
    return print(str(n))
sqr(a)

#Задача 2
a = int(input())
def gast(a):
    b = [a - 1, a + 1]
    print(b)
gast(a)

#Задача 3
a = str(input().split())
def b(a):
    b = a.lower()
    print(b)
b(a)

#Задача 4
import math
b = list(map(float, input().split(',')))
def a(b):
    for i in range(len(b)):
        if b[i] == 0 or b[i] < 0:
            b[i] = None
            continue
        b[i] = math.log(b[i])
    print(b)
a(b)

