def power(a, n):
	if n == 0:
		return 1 
	king = power(a * a, n//2)
	if n%2:
		king *= a 
	return king

a = float(input())
n = float(input())
print(power(a, n))