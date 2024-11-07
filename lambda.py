print("================================")
print("     LAMBDA RUMUS PERSEGI       ")
print("================================")


sisi = int(input('Sisi : '))

luas = lambda s: s * s
keliling = lambda s: 4 * s 

print('Luas\t\t: ',luas(sisi), 'cm2')
print('Keliling\t:',keliling(sisi), 'cm')
