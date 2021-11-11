import base64
klucz = "584b51f48bca9572acd08d378362"
zaszyfrowana = "2e2e3f9dabbcfc16c5f0fb5ee00b"

code = int(klucz, 16) ^ int(zaszyfrowana, 16)
h = hex(code)[2:].upper()#pozbywam się 0x z początku i zmieniam znaki na wielkie
print(base64.b16decode(h).decode())

