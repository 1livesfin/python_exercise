print('\033[92m==========================')
print('       RUMUS KUBUS        ')
print('--------------------------')
rusuk = float(input("Rusuk\t: "))
luas = 6 * rusuk ** 2
volume = rusuk ** 3
print('\033[91mLuas\t:\033[1m', str(round(luas, 2)), '\033[0mcm2')
print('\033[92mVolume\t:\033[1m', str(volume), '\033[0mcm3')
print('--------------------------')

print('\033[92m==========================')
# Function to calculate average acceleration
def average_acceleration(velocity_initial, velocity_final, time):
    # Rumus percepatan rata-rata: a = (v_f - v_i) / t
    acceleration = (velocity_final - velocity_initial) / time
    return acceleration

# Input: kecepatan awal (m/s), kecepatan akhir (m/s), dan waktu (s)
velocity_initial = float(input("Masukkan kecepatan awal (dalam m/s): "))
velocity_final = float(input("Masukkan kecepatan akhir (dalam m/s): "))
time = float(input("Masukkan waktu yang ditempuh (dalam detik): "))

# Menghitung percepatan rata-rata
acceleration = average_acceleration(velocity_initial, velocity_final, time)

# Output: percepatan rata-rata (m/s^2)
print(f"Percepatan rata-rata adalah {acceleration} m/s^2.")