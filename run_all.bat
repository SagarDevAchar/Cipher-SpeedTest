@echo off
echo %date% %time% > output.log
wmic /append:output.log cpu get /format:list

python data_gen.py %1%
python speedtest_aes.py %2%
python speedtest_blowfish.py %2%
python speedtest_des3.py %2%
python speedtest_des.py %2%
python speedtest_rc2.py %2%
python speedtest_chacha20.py %2%
python speedtest_salsa20.py %2%
python speedtest_rc4.py %2%
@echo on
