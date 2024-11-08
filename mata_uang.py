# Program konversi mata uang dari USD ke IDR
usd = float(input("Masukkan jumlah dalam USD: "))
kurs = 15000  # Kurs tetap 1 USD = 15000 IDR
idr = usd * kurs
print(f"${usd:.2f} sama dengan Rp{idr:.2f}")