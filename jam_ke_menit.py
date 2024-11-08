def jam_to_menit_dan_detik(jam):
    # Menghitung menit dan detik
    menit = jam * 60
    detik = jam * 3600
    return menit, detik

# Input dari pengguna
jam_input = float(input("Masukkan jumlah jam: "))
menit_output, detik_output = jam_to_menit_dan_detik(jam_input)

print(f"{jam_input} jam sama dengan {menit_output} menit dan {detik_output} detik")