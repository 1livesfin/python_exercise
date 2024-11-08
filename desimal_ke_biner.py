# Program konversi Desimal ke Biner
desimal = int(input("Masukkan angka desimal: "))
biner = bin(desimal)
print(f"Angka {desimal} dalam biner adalah {biner[2:]}")