# Cipher-SpeedTest
Python Codebase to test the speed of Block and Stream Ciphers on your PC

## Info

This testkit runs on [`PyCryptoDome`](https://www.pycryptodome.org/). The following ciphers will be tested:

| Cipher | Type | Key Size (bits) |
|---|---|---|
| AES | Block | 128 / 192 / 256 |
| DES | Block | 64 |

All Ciphers are tested for encryption and decryption of a `64 MB` (megabytes) random data sequence. The average of 15 iterations is produced.

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
