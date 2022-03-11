x='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

b=bytes.fromhex(x)

s = ""
i= ord('\x73') ^ ord('c')
for bi in b:
	s=s+chr(i ^ bi)
print(s)

