a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = ((p - a) * (p - b) * (p - c) * p)  ** (1 / 2)
if S == int(S):
    print(int(S))
elif S > int(S):
    print(round(S,6))
