key1='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key21='37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key23='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
flagkey123='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

def xor(a,b):
    b1 = bytes.fromhex(a)
    b2 = bytes.fromhex(b)
    return bytes.hex(bytes([(i ^ j) for (i,j) in zip(b1,b2)]))

key2 = xor(key1, key21)
key3 = xor(key2, key23)

flag = xor(key1,xor(flagkey123, key23))

print(bytes.fromhex(flag))
