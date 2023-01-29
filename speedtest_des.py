from Crypto.Cipher import DES
from datetime import datetime as dt
from random import randbytes
import sys

print("\nRunning " + sys.argv[0])
print("=" * 75)

with open('64MB.bin', 'rb') as f:
    buffer = f.read()

TRIALS = 15

print("\nENCRYPT")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rDES-ECB-64: {_}", end='')
    des = DES.new(randbytes(DES.key_size), DES.MODE_ECB)
    des.encrypt(buffer)
end = dt.now()
print(f"\rDES-ECB-64: {(end - start).total_seconds() / TRIALS:f} s")

print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rDES-ECB-64: {_}", end='')
    des = DES.new(randbytes(DES.key_size), DES.MODE_ECB)
    des.decrypt(buffer)
end = dt.now()
print(f"\rDES-ECB-64: {(end - start).total_seconds() / TRIALS:f} s")
