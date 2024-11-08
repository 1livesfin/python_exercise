# Program menghitung KPK dan FPB
import math

angka1 = int(input("Tulis angka pertama: "))
angka2 = int(input("Tulis angka kedua: "))

fpb = math.gcd(angka1, angka2)
kpk = (angka1 * angka2) // fpb

print(f"FPB dari {angka1} dan {angka2} = {fpb}")
print(f"KPK dari {angka1} dan {angka2} = {kpk}")