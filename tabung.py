print("=====================================")
print("            RUMUS TABUNG             ")
print("=====================================")

PHI = 3.14

v = float(input('Masukan volume tabung \t:'))
t = float(input('Masukan tinggi tabung \t:'))
r = float(input('Masukan ruas \t:'))
lp = float(input('Masukan luas permukaan tabung \t:'))

volume = PHI*r*r*t
luas p = 2*PHI*r*(r+t)

print('Volume tabung \t:', volume, 'cm')
print('Luas permukaan tabung \t:', luas p, 'cm')