from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode()))
# This gives us the key
print(xor(flag, 'myXORkey'.encode()))

#resource: https://golamrabbany.medium.com/crypto-ctf-you-either-know-xor-you-dont-69ac9b8f4812 