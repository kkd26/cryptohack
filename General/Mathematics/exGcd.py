def exGcd(a,b):
	if b == 0:
		return [1, 0]

	[x, y] = exGcd(b, a%b)
	n = a//b
	return [y, x - n*y]
