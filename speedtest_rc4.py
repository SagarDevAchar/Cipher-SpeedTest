from tee import *
from Crypto.Cipher import ARC4
from datetime import datetime as dt
from random import randbytes
import sys

tee_print("\nRunning " + sys.argv[0])
tee_print("=" * 50)

with open('random_data.bin', 'rb') as f:
    buffer = f.read()
FS = len(buffer) / (1024 ** 2)

try:
    TRIALS = int(sys.argv[1])
    tee_print(f"Setting TRIALS = {sys.argv[1]}")
except Exception:
    TRIALS = 15
    tee_print(f"Invalid Argument Received\nDefaulting to TRIALS = 15")

tee_print("\nENCRYPT")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-40: {_}", end='')
    arc4 = ARC4.new(randbytes(5))
    arc4.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-40:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-128: {_}", end='')
    arc4 = ARC4.new(randbytes(16))
    arc4.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-128:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-192: {_}", end='')
    arc4 = ARC4.new(randbytes(24))
    arc4.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-192:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-256: {_}", end='')
    arc4 = ARC4.new(randbytes(32))
    arc4.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-256:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-2048: {_}", end='')
    arc4 = ARC4.new(randbytes(256))
    arc4.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-2048:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

tee_print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-40: {_}", end='')
    arc4 = ARC4.new(randbytes(5))
    arc4.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-40:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-128: {_}", end='')
    arc4 = ARC4.new(randbytes(16))
    arc4.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-128:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-192: {_}", end='')
    arc4 = ARC4.new(randbytes(24))
    arc4.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-192:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-256: {_}", end='')
    arc4 = ARC4.new(randbytes(32))
    arc4.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-256:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC4-2048: {_}", end='')
    arc4 = ARC4.new(randbytes(256))
    arc4.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC4-2048:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")
