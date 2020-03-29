p = float(input())
x = float(input())
y_= float(input())

cash1 = 100 * x + y
cash2 = int(cash1 *(100+p)/100)
print(cash2//100,cash2 % 100)