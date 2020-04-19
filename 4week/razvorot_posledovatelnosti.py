def recurse():
    n = int(input())
    if n != 0:
        recurse()
    print(n)
recurse()
