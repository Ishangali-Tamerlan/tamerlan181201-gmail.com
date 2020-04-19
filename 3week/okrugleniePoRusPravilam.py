import math
num = float(input())
fr = num - int(num)
if fr < 0.5:
    print(math.floor(num))
elif fr >= 0.5:
    print(math.ceil(num))
