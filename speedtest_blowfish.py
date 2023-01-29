from Crypto.Cipher import Blowfish
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
    print(f"\rBlowfish-ECB-64: {_}", end='')
    blowfish = Blowfish.new(randbytes(8), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-64: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rBlowfish-ECB-128: {_}", end='')
    blowfish = Blowfish.new(randbytes(16), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rBlowfish-ECB-192: {_}", end='')
    blowfish = Blowfish.new(randbytes(24), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-192: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rBlowfish-ECB-256: {_}", end='')
    blowfish = Blowfish.new(randbytes(32), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-256: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rBlowfish-ECB-448: {_}", end='')
    blowfish = Blowfish.new(randbytes(56), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-448: {(end - start).total_seconds() / TRIALS:f} s")

print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rBlowfish-ECB-64: {_}", end='')
    blowfish = Blowfish.new(randbytes(8), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-64: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rBlowfish-ECB-128: {_}", end='')
    blowfish = Blowfish.new(randbytes(16), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rBlowfish-ECB-192: {_}", end='')
    blowfish = Blowfish.new(randbytes(24), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-192: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rBlowfish-ECB-256: {_}", end='')
    blowfish = Blowfish.new(randbytes(32), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-256: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rBlowfish-ECB-448: {_}", end='')
    blowfish = Blowfish.new(randbytes(56), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
print(f"\rBlowfish-ECB-448: {(end - start).total_seconds() / TRIALS:f} s")
