#mil ke kilometer

def mil_to_kilometer(mil):
    # 1 mil = 1.60934 kilometer
    kilometer = mil * 1.60934
    return kilometer

# Input dari pengguna
mil_input = float(input("Masukkan jarak dalam mil: "))
kilometer_output = mil_to_kilometer(mil_input)

print(f"{mil_input} mil sama dengan {kilometer_output:.2f} kilometer")