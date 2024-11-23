#menghitung frekuensi karakter dalam sebuah string

string = "python"
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Frekuensi karakter:", frequency)