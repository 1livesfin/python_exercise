kalimat = input("Tulis Sebuah Kalimat: ")
 
kata = kalimat.split()
kata.sort()
print("Berikut Urutan Kata-Kata:")
for urut in kata:
   print(urut)