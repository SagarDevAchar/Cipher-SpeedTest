from random import randbytes
import sys

print("\nRunning " + sys.argv[0])
print("=" * 75)

with open('64MB.bin', 'wb') as f:
    f.write(randbytes(64 * 1024 ** 2))