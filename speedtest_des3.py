from Crypto.Cipher import DES3
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
    print(f"\rDES3-ECB-112: {_}", end='')
    des3 = DES3.new(DES3.adjust_key_parity(randbytes(16)), DES3.MODE_ECB)
    des3.encrypt(buffer)
end = dt.now()
print(f"\rDES3-ECB-112: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rDES3-ECB-168: {_}", end='')
    des3 = DES3.new(DES3.adjust_key_parity(randbytes(24)), DES3.MODE_ECB)
    des3.encrypt(buffer)
end = dt.now()
print(f"\rDES3-ECB-168: {(end - start).total_seconds() / TRIALS:f} s")

print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rDES3-ECB-112: {_}", end='')
    des3 = DES3.new(DES3.adjust_key_parity(randbytes(16)), DES3.MODE_ECB)
    des3.decrypt(buffer)
end = dt.now()
print(f"\rDES3-ECB-112: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rDES3-ECB-168: {_}", end='')
    des3 = DES3.new(DES3.adjust_key_parity(randbytes(24)), DES3.MODE_ECB)
    des3.decrypt(buffer)
end = dt.now()
print(f"\rDES3-ECB-168: {(end - start).total_seconds() / TRIALS:f} s")
