[![speed-test](https://github.com/SagarDevAchar/Cipher-SpeedTest/actions/workflows/run-shell.yml/badge.svg)](https://github.com/SagarDevAchar/Cipher-SpeedTest/actions/workflows/run-shell.yml)

# Cipher-SpeedTest
Python Codebase to test the speed of Block and Stream Ciphers on your PC

## Functional Specification

This testkit runs on [`pycryptodome`](https://www.pycryptodome.org/). The following ciphers will be tested with the following key sizes:

| Cipher   | Type   | Key Size (bits)             |
| -------- | ------ | --------------------------- |
| AES      | Block  | 128 / 192 / 256             |
| Blowfish | Block  | 64 / 128 / 192 / 256 / 448  |
| 3DES     | Block  | 112 / 168                   |
| DES      | Block  | 64                          |
| RC2      | Block  | 40 / 128 / 192 / 256 / 1024 |
| ChaCha20 | Stream | 256                         |
| Salsa20  | Stream | 128 / 256                   |
| RC4      | Stream | 40 / 128 / 192 / 256 / 2048 | 

All Ciphers are tested for **encryption** and **decryption** of a file containing random data. The average of multiple runs is produced. This process will take time, so please be patient!

**NOTE:** On Intel CPUs which operate on successors of the Nehalem Microarchitecture, AES runs exceptionally fast compared to other ciphers. This is due to the introduction of the [AES-NI Instruction Set](https://en.wikipedia.org/wiki/AES_instruction_set) by Intel. To perform accurate computational analysis, please turn off the AES-NI feature in your BIOS/UEFI Settings.

## Usage Instructions

This repository contains the following files:
- `requirements.txt`: Contains the Python Dependencies
- `data_gen.py`: Generators a `.bin` file in the working directory of 64MB Size
- `tee.py`: A very primitive version of the Linux [`tee`](https://en.wikipedia.org/wiki/Tee_(command)) to log and print parallelly
- `speedtest_x.py`: Speedtest Code for Cipher `X`
- `run_all.sh`: Shell Script to run all tests (Linux)
- `run_all.bat`: Batch Script to run all tests (Windows)

The outputs generated are available in a file named `output.log`

Further steps can be found below:
- [Usage Guide for Linux Users](https://github.com/SagarDevAchar/Cipher-SpeedTest/blob/main/USAGE_LINUX.md)
- [Usage Guide for Windows Users](https://github.com/SagarDevAchar/Cipher-SpeedTest/blob/main/USAGE_WINDOWS.md)
