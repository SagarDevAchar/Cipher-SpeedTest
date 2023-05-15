from tee import *
from Crypto.Cipher import DES3
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
    tee_print(f"\rDES3-ECB-112:\t#{_+1}", end='')
    des3 = DES3.new(DES3.adjust_key_parity(randbytes(16)), DES3.MODE_ECB)
    des3.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rDES3-ECB-112:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} MB/s")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rDES3-ECB-168:\t#{_+1}", end='')
    des3 = DES3.new(DES3.adjust_key_parity(randbytes(24)), DES3.MODE_ECB)
    des3.encrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rDES3-ECB-168:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} MB/s")

tee_print("\nDECRYPT")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rDES3-ECB-112:\t#{_+1}", end='')
    des3 = DES3.new(DES3.adjust_key_parity(randbytes(16)), DES3.MODE_ECB)
    des3.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rDES3-ECB-112:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} MB/s")

start = dt.now()
for _ in range(TRIALS):
    tee_print(f"\rDES3-ECB-168:\t#{_+1}", end='')
    des3 = DES3.new(DES3.adjust_key_parity(randbytes(24)), DES3.MODE_ECB)
    des3.decrypt(buffer)
end = dt.now()
T = (end - start).total_seconds() / TRIALS
tee_print(f"\rDES3-ECB-168:\t{(end - start).total_seconds() / TRIALS:f} s\t{FS / T:f} MB/s")

tee_print("-" * 64)
