# Cipher-SpeedTest
Python Codebase to test the speed of Block and Stream Ciphers on your PC

## Info

This testkit runs on [`PyCryptoDome`](https://www.pycryptodome.org/). The following ciphers will be tested with the following key sizes:

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

All Ciphers are tested for **encryption** and **decryption** of a `64 MB` (megabytes) file containing random data. The average of 15 iterations is produced.

This process will take time, so please be patient!

**NOTE:** On Intel CPUs which operate on successors of the Nehalem Microarchitecture, AES runs exceptionally fast compared to other ciphers. This is due to the introduction of the [AES-NI Instruction Set](https://en.wikipedia.org/wiki/AES_instruction_set) by Intel. 

## Usage

This repository contains the following files:
- `requirements.txt`: Contains the Python Dependencies
- `data_gen.py`: Generators a `.bin` file in the working directory of 64MB Size
- `tee.py`: A very primitive version of the Linux [`tee`](https://en.wikipedia.org/wiki/Tee_(command)) to log and print parallelly
- `speedtest_X.py`: Speedtest Code for Cipher `X`

The outputs generated are available in a file named `output.log`

For Windows users

```
  > run_windows.bat
```

For Linux users

```
  $ sh run_linux.sh
```
