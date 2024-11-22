from pwn import xor
#decode from hex

string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
toByte = (bytes.fromhex(string))

for key in range(256):
    result = xor(toByte,key)
    if b"crypto" in result:
        print(result)
