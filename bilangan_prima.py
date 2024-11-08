# Program memeriksa apakah bilangan prima
def cek_prima(angka):
    if angka > 1:
        for i in range(2, int(angka**0.5) + 1):
            if angka % i == 0:
                return False
        return True
    return False

angka = int(input("Masukkan sebuah angka: "))
if cek_prima(angka):
    print(f"{angka} adalah bilangan prima.")
else:
    print(f"{angka} bukan bilangan prima.")