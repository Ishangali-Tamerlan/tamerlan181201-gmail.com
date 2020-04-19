digit = int(input())
dig1 = digit // 100
dig2 = (digit // 10) % 10
dig3 = digit % 10
sum = dig1 + dig2 + dig3
print(sum)
