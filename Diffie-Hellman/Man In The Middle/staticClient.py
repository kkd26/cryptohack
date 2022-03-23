import telnetlib
import json
from modexp import modexp

HOST = "socket.cryptohack.org"
PORT = 13373

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline().decode()
    line = line[line.find("{"):]
    return json.loads(line)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def getInitMessage():
  d = json_recv()
  p = int(d["p"], 16)
  g = int(d["g"], 16)
  A = int(d["A"], 16)
  return (p,g,A)

def createSharedSecret(pk, sk, p):
  return modexp(pk, sk, p)

def makePK(sk, g, p):
  return modexp(g, sk, p)

def sendToBob(p,g,A):
  d = {"p":p, "g":g, "A":A}
  json_send(d)

def getFromB():
  d = json_recv()
  B = int(d["B"], 16)
  return B

def sendToAlice(B):
  d = {"B":B}
  json_send(d)

def getIvAndFlag():
  d = json_recv()
  iv = d["iv"]
  encrypted_flag = d["encrypted"]
  return (iv, encrypted_flag)

(p,g,A) = getInitMessage() # From A
B = getFromB() # from B
(iv, enc_flag) = getIvAndFlag() # From A

sendToBob(hex(p), hex(A), "0x01") # To Bob
sharedK = getFromB() # from B

from decrypt import decrypt_flag
flag = decrypt_flag(sharedK, iv, enc_flag)
print(flag)
