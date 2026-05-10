import math

def f(x):
 return math.sqrt(1 - 0.4*x*x) - math.asin(x)

def df(x):
 return (-0.4*x)/math.sqrt(1 - 0.4*x*x) - 1/math.sqrt(1-x*x)

def d2f(x):
 return (-0.4)/math.sqrt(1-0.4*x*x) - (0.16*x*x)/((1-0.4*x*x)**(3/2)) - x/((1-
x*x)**(3/2))

a = 0.3
b = 0.9
eps = 0.0001

if f(a) * d2f(a) > 0:
 x = a
else:
 x = b

del_ = 1

print("Крок | x (попереднє) | y (наступне) | del")
print("-"*60)

i = 0

while del_ > eps:
 y = x - f(x)/df(x)

 del_ = abs(y-x)
 
 print(f"{i+1} | {x:.6f} | {y:.6f} | {del_:.6f}")
 x = y
 i += 1
print("-"*60)
print("Корінь:", x)