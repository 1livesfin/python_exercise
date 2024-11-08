import calendar

# Program Menampilkan Kalender
tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan bulan (1-12): "))

print(calendar.month(tahun, bulan))