from tee import *
from Crypto.Cipher import ARC2
from datetime import datetime as dt
from random import randbytes
import sys

tee_print("\nRunning " + sys.argv[0])
tee_print("-" * 64)

with open('random_data.bin', 'rb') as f:
    buffer = f.read()
FS = len(buffer) / (1024 ** 2)

try:
    TRIALS = int(sys.argv[1])
    tee_print(f"Setting TRIALS = {sys.argv[1]}")
except Exception:
    TRIALS = 15
    tee_print(f"Invalid TRIALS Argument\nDefaulting to TRIALS = 15")

tee_print("\nENCRYPT")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-40:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(5), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-40:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-128:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(16), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-128:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-192:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(24), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-192:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-256:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(32), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-256:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-1024:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(128), ARC2.MODE_ECB)
    arc2.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-1024:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

tee_print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-40:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(5), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-40:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-128:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(16), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-128:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-192:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(24), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-192:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-256:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(32), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-256:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rARC2-ECB-1024:\t#{_+1}", end='')
    arc2 = ARC2.new(randbytes(128), ARC2.MODE_ECB)
    arc2.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rARC2-ECB-1024:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

tee_print("-" * 64)
