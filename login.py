USERNAME='1livesfin@gmail.com'
PASSWORD='1234567'

username=input("Masukan username\t: ")
password=input("Masukan password\t: ")

if username!=USERNAME:
    print('Username tidak tersedia')
elif username==USERNAME and password != PASSWORD:
    print('Password salah')
else:
    print("Selamat datang!", username)