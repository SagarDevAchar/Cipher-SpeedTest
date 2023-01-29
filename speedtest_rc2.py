from Crypto.Cipher import ARC2
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
    print(f"\rARC2-ECB-5: {_}", end='')
    arc2 = ARC2.new(randbytes(5), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-5: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC2-ECB-128: {_}", end='')
    arc2 = ARC2.new(randbytes(16), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC2-ECB-192: {_}", end='')
    arc2 = ARC2.new(randbytes(24), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-192: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC2-ECB-256: {_}", end='')
    arc2 = ARC2.new(randbytes(32), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-256: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC2-ECB-1024: {_}", end='')
    arc2 = ARC2.new(randbytes(128), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-1024: {(end - start).total_seconds() / TRIALS:f} s")

print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC2-ECB-5: {_}", end='')
    arc2 = ARC2.new(randbytes(5), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-5: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC2-ECB-128: {_}", end='')
    arc2 = ARC2.new(randbytes(16), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC2-ECB-192: {_}", end='')
    arc2 = ARC2.new(randbytes(24), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-192: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC2-ECB-256: {_}", end='')
    arc2 = ARC2.new(randbytes(32), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-256: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rARC2-ECB-1024: {_}", end='')
    arc2 = ARC2.new(randbytes(128), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
print(f"\rARC2-ECB-1024: {(end - start).total_seconds() / TRIALS:f} s")
