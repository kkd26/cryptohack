from decrypt import decrypt_flag

p = 0xde26ab651b92a129
g = 0x2
A = 0xd148c16c6b031b3a
B = 0x2551ffb124f2f182

# use online tool https://www.alpertron.com.ar/DILOG.HTM
b = 0x3d0bb9a2bc4e3d81
a = 0x582f023963c91ffe

sK = pow(A,b,p)

iv = "9373cb36004fde9ee2727ed16d495f09"
encrypted_flag = "ae3c9fa1c73d3a9bf0710e8bb19399c7ed41438d68d4f80edb4b963340f3c2cf"

flag = decrypt_flag(sK, iv, encrypted_flag)
print(flag)