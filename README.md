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

**NOTE:** On Intel CPUs which operate on successors of the Nehalem Microarchitecture, AES runs exceptionally fast compared to other ciphers. This is due to the introduction of the [AES-NI Instruction Set](https://en.wikipedia.org/wiki/AES_instruction_set) by Intel. To perform accurate computational analysis, please turn off the AES-NI feature.

## Usage

This repository contains the following files:
- `requirements.txt`: Contains the Python Dependencies
- `data_gen.py`: Generators a `.bin` file in the working directory of 64MB Size
- `tee.py`: A very primitive version of the Linux [`tee`](https://en.wikipedia.org/wiki/Tee_(command)) to log and print parallelly
- `speedtest_x.py`: Speedtest Code for Cipher `X`
- `run_all.sh`: Shell Script to run all tests

The outputs generated are available in a file named `output.log`

### Generating the test data

To generate the random data, run the `data_gen.py` script as shown below:
```
  $ python3 data_gen.py [FILE_SIZE_IN_MEGABYTES]
```
For example, the following command generates `16MB` of data:
```
  $ python3 data_gen.py 16
```
Failure to provide the `FILE_SIZE_IN_MEGABYTES` argument will default to producing `64MB` of data

### Testing a cipher

To test a cipher `X`, run the `speedtest_x.py` script as shown below:
```
  $ python3 speedtest_x.py [TRIALS]
```
For example, the following command tests the `ChaCha20` Cipher for `10` trials:
```
  $ python3 speedtest_chacha20.py 10
```
Failure to provide the `TRIALS` argument will default to testing for `15` trials

### Running all tests

To run all tests simultaneously, run the `run_all.sh` shell script as shown below:
```
  $ sh run_shell.sh [FILE_SIZE_IN_MEGABYTES] [TRIALS]
```
For example, the following command tests all ciphers for `16MB` random data for `10` trials:
```
  $ sh run_shell.sh 16 10
```
Failure to provide the `FILE_SIZE_IN_MEGABYTES` or `TRIALS` argument will default to `64MB` and `15` trials.
