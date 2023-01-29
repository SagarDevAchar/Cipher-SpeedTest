from Crypto.Cipher import ChaCha20
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
    print(f"\rChaCha20-256: {_}", end='')
    chacha20 = ChaCha20.new(key=randbytes(ChaCha20.key_size))
    chacha20.encrypt(buffer)
end = dt.now()
print(f"\rChaCha20-256: {(end - start).total_seconds() / TRIALS:f} s")

print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    print(f"\rChaCha20-256: {_}", end='')
    chacha20 = ChaCha20.new(key=randbytes(ChaCha20.key_size))
    chacha20.decrypt(buffer)
end = dt.now()
print(f"\rChaCha20-256: {(end - start).total_seconds() / TRIALS:f} s")
