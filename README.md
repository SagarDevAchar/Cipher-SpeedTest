# Cipher-SpeedTest
Python Codebase to test the speed of Block and Stream Ciphers on your PC

## Info

This testkit runs on [`PyCryptoDome`](https://www.pycryptodome.org/). The following ciphers will be tested:

| Cipher | Type | Key Size (bits) |
|---|---|---|
| AES | Block | 128 / 192 / 256 |
| DES | Block | 64 |
| Blowfish | Block | 64 / 128 / 192 / 256 / 448 |
| 3DES | Block | 112 / 168 |
| RC2 | Block | 40 / 128 / 192 / 256 / 1024 |
| RC4 | Stream | 40 / 128 / 192 / 256 / 2048 |

All Ciphers are tested for **encryption** and **decryption** of a `64 MB` (megabytes) file containing random data. The average of 15 iterations is produced.

This process will take time, so please be patient!

**NOTE:** On Intel CPUs which operate on successors of the Nehalem Microarchitecture, AES runs exceptionally fast compared to other ciphers. This is due to the introduction of the [AES-NI Instruction Set](https://en.wikipedia.org/wiki/AES_instruction_set) by Intel. 

## Usage

For Windows users (to print output)

```
  > run_windows.bat
```

For Windows users (to log output)

```
  > run_windows.bat > output.log
```

For Linux users (to print output)

```
  $ sh run_linux.sh
```

For Linux users (to log output)

```
  $ sh run_linux.sh > output.log
```

For Linux users (to print and log output)

```
  $ sh run_linux.sh | tee output.log
```
