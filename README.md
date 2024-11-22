## hexToBase64.py
This exercise demonstrates the process of converting data encoded in one format (hexadecimal) into another widely used format (Base64).

## bytesAndBigIntegers.py
This exercise shows how to work with large numbers by converting them from a numeric format (long integer) into a byte sequence, emphasizing the connection between numeric and textual representations of data, a key concept in cryptography and data encoding.

## XOR.py
This exercise demonstrates how to use the `xor` function from the `pwn` library to apply the XOR operation on a byte string (`label`) with a numeric value (13), showcasing how XOR can be used to encode or decode data in cryptography.

## XORProperties.py
The purpose of this exercise is to understand and apply **XOR properties** to decrypt data (the flag) by combining information encoded with multiple keys, without directly knowing all the keys.

## FavouriteByte.py
The goal of this task is to use XOR with all possible single-byte keys (from 0 to 255) to decrypt the given hex-encoded string, and identify the correct key by checking for the presence of the word "crypto" in the resulting output.

## xorMultiByte.py
The goal of this script is to decrypt a hexadecimal-encoded, XOR-encrypted message (flag) by first deriving the encryption key using a known plaintext prefix (crypto), and then using the key to reveal the full decrypted message.