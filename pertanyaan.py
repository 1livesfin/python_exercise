soal = [
    {'pertanyaan':''}
]

def tampilkan_soal(soal):
    for index, item in enumerate(soal):
        print(f"Soal {index + 1}: {item['pertanyaan']}")
        for pilihan in item['pilihan']:
            print(pilihan)
        
        # Input jawaban
        jawaban = input("Pilih jawaban (A/B/C/D): ").upper()
        
        # Cek apakah jawaban benar
        if jawaban == item['jawaban']:
            print("Jawaban Anda Benar!\n")
        else:
            print(f"Jawaban Anda Salah! Jawaban yang benar adalah {item['jawaban']}\n")
