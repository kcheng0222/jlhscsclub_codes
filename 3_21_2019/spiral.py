s = "Hello world!"

i = 0
l = 1
while(l*l < len(s)):
	l += 1
print(l)

grid = [["" for y in range(l)] for x in range(l)]
print(grid)
