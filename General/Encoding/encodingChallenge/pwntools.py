from pwn import * # pip install pwntools
from Crypto.Util.number import *
import codecs
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode(r):
    encoding = r["type"]
    code = r["encoded"]
    if encoding == "base64":
        decoded = base64.b64decode(code.encode()).decode()
    elif encoding == "hex":
        decoded = bytes.fromhex(code).decode()
    elif encoding == "rot13":
        decoded = codecs.decode(code, 'rot_13')
    elif encoding == "bigint":
        decoded = long_to_bytes(int(code, 16)).decode()
    elif encoding == "utf-8":
        decoded = ''.join([chr(b) for b in code])
    return {"decoded": decoded}

received = json_recv()
while "flag" not in received:
    s = decode(received)
    json_send(s)
    received = json_recv()

print(received)
