import math
price = float(input())
x = price * 100
a = math.ceil(x // 100)
b = math.ceil(x % 100)
print(a, b)
