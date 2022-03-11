t="label"

ans=''.join([chr(ord(i) ^ 13) for i in t])
print(ans)
