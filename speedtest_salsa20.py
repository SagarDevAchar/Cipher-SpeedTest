from Crypto.Cipher import Salsa20
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
    print(f"\rSalsa20-128: {_}", end='')
    salsa20 = Salsa20.new(key=randbytes(16))
    salsa20.encrypt(buffer)
end = dt.now()
print(f"\rSalsa20-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rSalsa20-256: {_}", end='')
    salsa20 = Salsa20.new(key=randbytes(32))
    salsa20.encrypt(buffer)
end = dt.now()
print(f"\rSalsa20-256: {(end - start).total_seconds() / TRIALS:f} s")

print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rSalsa20-128: {_}", end='')
    salsa20 = Salsa20.new(key=randbytes(16))
    salsa20.decrypt(buffer)
end = dt.now()
print(f"\rSalsa20-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rSalsa20-256: {_}", end='')
    salsa20 = Salsa20.new(key=randbytes(32))
    salsa20.decrypt(buffer)
end = dt.now()
print(f"\rSalsa20-256: {(end - start).total_seconds() / TRIALS:f} s")
