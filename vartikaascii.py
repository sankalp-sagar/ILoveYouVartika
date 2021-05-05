import binascii
import sys
import os
from time import sleep

os.system('curl https://sankalpvartika.000webhostapp.com/binaryvartika.txt --output vb.txt')
os.system('cls')

print()
print("[+] I LOVE YOU VARTIKA")
print("\n\n")
sleep(1)

with open('vb.txt', 'r') as file:
    text = file.read()

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


print(text_from_bits(text))