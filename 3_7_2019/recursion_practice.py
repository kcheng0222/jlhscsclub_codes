def s(n):
	if n == 1:
		return 1
	return s(n-1) + n

print(s(5))


d = {}

def fib(n):
	if n == 0:
		return 0
	if n == 1 or n == 2:
		return 1
	if n in d:
		return d[n]
	else:
		x = fib(n-1)+fib(n-2)
		d[n] = x
		return x
	
print(fib(100))
