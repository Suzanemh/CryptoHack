
from pwn import xor

label = b"label"
new_string = xor(label, 13).decode()
print(new_string)