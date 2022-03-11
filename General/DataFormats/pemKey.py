from Crypto.PublicKey import RSA

f = open('transparency.pem','r')
key = RSA.importKey(f.read())

print(key.n)
