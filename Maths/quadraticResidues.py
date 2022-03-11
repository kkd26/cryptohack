p = 29

ints = [14,6,11]

def findQR(p, a):
	return [i for i in range(1, p) if (i*i) % p == a]

def findQRList(p, a):
	return [findQR(p, i) for i in a]

print(findQRList(p, ints))
