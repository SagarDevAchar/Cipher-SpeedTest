# Usage Guide for Windows Users

## Installing dependencies

- Running this requires [`python3`](https://python.org) (version 3.7 or higher), you can install it using the following command:
```
  > winget install python3
```
- You can also manualla download and install `python3` from their [official website](https://python.org)
- You need to install `pycryptodome` for this to run. You can do this using the following steps:
```
  > pip install -r requirements.txt
```
- You can also install `pycryptodome` manually using `pip install pycryptodome`


## Generating the test data

- To generate the random data, run the `data_gen.py` script as shown below:
```
  > python data_gen.py [FILE_SIZE_IN_MEGABYTES]
```
- For example, the following command generates `16MB` of data:
```
  > python data_gen.py 16
```
- Failure to provide the `FILE_SIZE_IN_MEGABYTES` argument will default to producing `64MB` of data


## Testing a cipher

- To test a cipher `X`, run the `speedtest_x.py` script as shown below:
```
  > python speedtest_x.py [TRIALS]
```
- For example, the following command tests the `ChaCha20` Cipher for `10` trials:
```
  > python speedtest_chacha20.py 10
```
- Failure to provide the `TRIALS` argument will default to testing for `15` trials


## Running all tests

- To run all tests simultaneously, run the `run_all.bat` batch script as shown below:
```
  > run_all.bat [FILE_SIZE_IN_MEGABYTES] [TRIALS]
```
- For example, the following command tests all ciphers for `16MB` random data for `10` trials:
```
  > run_all.bat 16 10
```
- Failure to provide the `FILE_SIZE_IN_MEGABYTES` or `TRIALS` argument will default to `64MB` and `15` trials.

- `run_all.bat` also logs the Date and Time of execution along with information about your CPU architecture.

- **WARNING:** `run_all.bat` cleans your log file! Previous logs will be overwritten!
