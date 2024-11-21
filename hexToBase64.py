#!/usr/bin/env python3

import sys
import base64

ords = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

print("Here is your flag:")
#from heks to bytes
byte= (bytes.fromhex(ords))
#from heks to bytes
print(base64.b64encode(byte))