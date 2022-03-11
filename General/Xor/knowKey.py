x='0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

b=bytes.fromhex(x)

phrase = 'crypto{1'

def xor(a, b):
	return bytes([i^j for (i,j) in zip(a,b)])

def getKey(n):
	xx = b[:n]
	yy = phrase[:n].encode()
	return xor(xx, yy)

def encode(key, code):
	n = len(key)
	return bytes([code[j] ^ key[j%n] for j in range(len(code))])


for i in range(1, len(phrase)+1):
	key = getKey(i)
	print(key)
	s = encode(key, b)
	print(s)
