import base64
cipher = "1ef0bf77f79f71f71f32f31f20f39f26f24f3df26f21f16f28f20f30f1cf3df26f31f38f".split('f')
key = ['4' + i for i in "935935"]
cipher = cipher[:-1]
res = []
for i, n in enumerate(cipher):
  x = int(n, 16)
  y = int(key[i % len(key)], 16)
  res.append(hex(x ^ y)[2:])
res = "".join(res)
print(bytes.fromhex(res).decode())
