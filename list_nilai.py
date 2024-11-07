nilai = []
jml = int(input('Jumlah data yang akan diinput: '))

for i in range(jml):
    nilai.append(float(input(f'Nilai ke-{i+1}: ')))
    
#perhitungan data di list
total = rata2 =  max =  min = 0
for data in nilai:
    total += data
    if data > max:
        max = data
      
    if data < min:
        min = data

print(nilai)
print(f'Rata-rata : {total/jml}')
print(f'Nilai terbesar : {max}')
print(f'Nilai terkecil : {min}')