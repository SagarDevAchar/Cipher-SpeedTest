date
lscpu
python3 data_gen.py ${1}
python3 speedtest_aes.py ${2}
python3 speedtest_blowfish.py ${2}
python3 speedtest_des3.py ${2}
python3 speedtest_des.py ${2}
python3 speedtest_rc2.py ${2}
python3 speedtest_chacha20.py ${2}
python3 speedtest_salsa20.py ${2}
python3 speedtest_rc4.py ${2}
