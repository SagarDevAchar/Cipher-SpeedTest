from tee import *
from Crypto.Cipher import DES
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
    tee_print(f"\rDES-ECB-64:\t#{_+1}", end='')
    des = DES.new(randbytes(DES.key_size), DES.MODE_ECB)
    des.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rDES-ECB-64:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

tee_print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rDES-ECB-64:\t#{_+1}", end='')
    des = DES.new(randbytes(DES.key_size), DES.MODE_ECB)
    des.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rDES-ECB-64:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} Mbps")

tee_print("-" * 64)
