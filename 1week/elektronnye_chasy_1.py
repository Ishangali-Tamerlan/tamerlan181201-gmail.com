N = int(input())

time = (N % (60 * 24))
print(time // 60, N % 60)
