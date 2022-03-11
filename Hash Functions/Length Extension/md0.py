#!/usr/bin/env python3

import telnetlib
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

HOST = "socket.cryptohack.org"
PORT = 13388

tn = telnetlib.Telnet(HOST, PORT)

def readline():
	return tn.read_until(b"\n")

def json_recv():
	line = readline()
	return line

def json_send(hsh):
	request = json.dumps(hsh).encode()
	tn.write(request)

def getSignature(m):
	request = {"option":"sign", "message": m}
	json_send(request)
	r=json_recv()
	sig=json.loads(r.decode())["signature"]
	return bytes.fromhex(sig)

def getFlag(s, m):
	request = {"option": "get_flag", "signature": s, "message": m}
	json_send(request)
	r=json_recv()
	return r

def bxor(a, b):
	return bytes(x ^ y for x, y in zip(a, b))

def hash(sig, key):
	key = pad(key, 16)
	out = bxor(AES.new(key, AES.MODE_ECB).encrypt(sig), sig)
	return out

data1=b'\x10' *16
data2=b"admin=True"

print(json_recv())
s = getSignature('') # the padding equal to data1 will be added
forged = hash(s, data2)

f = getFlag(forged.hex(), (data1+data2).hex())
print(f)
