#program tebak angka!

import random

def guess(x):
    random_number = random.randint(1, x)
guess = 0
    while guess != random_number:
        guess = int(input('Ayo tebak angkanya diantara 1 dan {x}: '))
        if guess < random_number:
            print ('Maaf, coba lagi. Terlalu rendah.')
        elif guess > random_number:
            print ('Maaf, tebak lagi. Terlalu tinggi')
        
    print('Selamat! Kamu sudah menebak angka yang benar! Yaitu {random_number}')


guess(10)