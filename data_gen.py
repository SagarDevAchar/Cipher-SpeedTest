from tee import *
from random import randbytes
import sys

tee_print("\nRunning " + sys.argv[0])
tee_print("-" * 64)

with open('random_data.bin', 'wb') as f:
    try:
        f.write(randbytes(int(sys.argv[1]) * 1024 ** 2))
        tee_print(f"Generated {str(sys.argv[1])}MB into 'random_data.bin'")
    except Exception:
        tee_print(f"Invalid FILE_SIZE_IN_MEGABYTES Argument\nDefaulting to 64MB")
        f.write(randbytes(64 * 1024 ** 2))
        tee_print(f"Generated 64MB into 'random_data.bin'")

tee_print("-" * 64)
