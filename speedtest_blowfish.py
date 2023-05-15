from tee import *
from Crypto.Cipher import Blowfish
from datetime import datetime as dt
from random import randbytes
import sys

tee_print("\nRunning " + sys.argv[0])
tee_print("-" * 64)

with open('random_data.bin', 'rb') as f:
    buffer = f.read()
FS = 8 * len(buffer) / (1024 ** 2)

try:
    TRIALS = int(sys.argv[1])
    tee_print(f"Setting TRIALS = {sys.argv[1]}")
except Exception:
    TRIALS = 15
    tee_print(f"Invalid TRIALS Argument\nDefaulting to TRIALS = 15")

tee_print("\nENCRYPT")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-64:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(8), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-64:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-128:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(16), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-128:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-192:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(24), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-192:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-256:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(32), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-256:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-448:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(56), Blowfish.MODE_ECB)
    blowfish.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-448:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

tee_print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-64:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(8), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-64:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-128:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(16), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-128:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-192:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(24), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-192:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-256:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(32), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-256:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rBlowfish-ECB-448:\t#{_+1}", end='')
    blowfish = Blowfish.new(randbytes(56), Blowfish.MODE_ECB)
    blowfish.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rBlowfish-ECB-448:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

tee_print("-" * 64)
