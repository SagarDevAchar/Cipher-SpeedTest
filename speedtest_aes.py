from Crypto.Cipher import AES
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
    print(f"\rAES-ECB-128: {_}", end='')
    aes = AES.new(randbytes(16), AES.MODE_ECB)
    aes.encrypt(buffer)
end = dt.now()
print(f"\rAES-ECB-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rAES-ECB-192: {_}", end='')
    aes = AES.new(randbytes(24), AES.MODE_ECB)
    aes.encrypt(buffer)
end = dt.now()
print(f"\rAES-ECB-192: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rAES-ECB-256: {_}", end='')
    aes = AES.new(randbytes(32), AES.MODE_ECB)
    aes.encrypt(buffer)
end = dt.now()
print(f"\rAES-ECB-256: {(end - start).total_seconds() / TRIALS:f} s")

print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rAES-ECB-128: {_}", end='')
    aes = AES.new(randbytes(16), AES.MODE_ECB)
    aes.decrypt(buffer)
end = dt.now()
print(f"\rAES-ECB-128: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rAES-ECB-192: {_}", end='')
    aes = AES.new(randbytes(24), AES.MODE_ECB)
    aes.decrypt(buffer)
end = dt.now()
print(f"\rAES-ECB-192: {(end - start).total_seconds() / TRIALS:f} s")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rAES-ECB-256: {_}", end='')
    aes = AES.new(randbytes(32), AES.MODE_ECB)
    aes.decrypt(buffer)
end = dt.now()
print(f"\rAES-ECB-256: {(end - start).total_seconds() / TRIALS:f} s")
