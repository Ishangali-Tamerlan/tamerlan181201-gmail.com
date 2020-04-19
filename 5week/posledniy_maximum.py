intList = list(map(int, input().split()))
maxDig = intList[0]
maxIndex = 0
for i, v in enumerate(intList):
    if v >= maxDig:
        maxIndex = i
        maxDig = v
print(maxDig, maxIndex)
