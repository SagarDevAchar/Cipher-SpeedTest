from Crypto.Cipher import ARC4
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
    print(f"\rARC4-5: {_}", end='')
    arc4 = ARC4.new(randbytes(5))
    arc4.encrypt(buffer)
end = dt.now()
print(f"\rARC4-5: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC4-128: {_}", end='')
    arc4 = ARC4.new(randbytes(16))
    arc4.encrypt(buffer)
end = dt.now()
print(f"\rARC4-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC4-192: {_}", end='')
    arc4 = ARC4.new(randbytes(24))
    arc4.encrypt(buffer)
end = dt.now()
print(f"\rARC4-192: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC4-256: {_}", end='')
    arc4 = ARC4.new(randbytes(32))
    arc4.encrypt(buffer)
end = dt.now()
print(f"\rARC4-256: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC4-2048: {_}", end='')
    arc4 = ARC4.new(randbytes(256))
    arc4.encrypt(buffer)
end = dt.now()
print(f"\rARC4-2048: {(end - start).total_seconds() / TRIALS:f} s")

print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC4-5: {_}", end='')
    arc4 = ARC4.new(randbytes(5))
    arc4.decrypt(buffer)
end = dt.now()
print(f"\rARC4-5: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC4-128: {_}", end='')
    arc4 = ARC4.new(randbytes(16))
    arc4.decrypt(buffer)
end = dt.now()
print(f"\rARC4-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC4-192: {_}", end='')
    arc4 = ARC4.new(randbytes(24))
    arc4.decrypt(buffer)
end = dt.now()
print(f"\rARC4-192: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC4-256: {_}", end='')
    arc4 = ARC4.new(randbytes(32))
    arc4.decrypt(buffer)
end = dt.now()
print(f"\rARC4-256: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC4-2048: {_}", end='')
    arc4 = ARC4.new(randbytes(256))
    arc4.decrypt(buffer)
end = dt.now()
print(f"\rARC4-2048: {(end - start).total_seconds() / TRIALS:f} s")
