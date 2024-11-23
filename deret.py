n = int(input("Berapa jumlah karakter yang ingin dimasukkan? "))


arr = []
for _ in range(0,n):
  arr.append(input("Masukkan karakter apapun, termasuk kata: "))


karakter_yang_dicari = input("Karakter apa yang kamu cari dari deret diatas? ")
jumlah_kemunculan = arr.count(karakter_yang_dicari)


print(f"Karakter {karakter_yang_dicari} muncul {jumlah_kemunculan} kali")