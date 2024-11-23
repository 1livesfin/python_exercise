import random

min_val = 1
max_val = 6

roll_again = "ya"

while roll_again == "ya" or roll_again == "y":
    print("Memutar Dadunya...")
    print("Nilainya adalah :")
    
    print(random.randint(min_val, max_val))

    roll_again = input("Putar Dadu lagi? ")