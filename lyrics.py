import sys
import time

def lirik_lagu ():
    lirik = [
        ("That's the reason I'm afraid", 0.09),
        ("You're the thoughts that can't be tamed", 0.08),
        ("And I'm trying to be sane", 0.09),
        ("And I'm trying to be sane", 0.09),
        ("And I'm trying to be sane", 0.09),
    ]

    delay = [1.2, 0.9, 5.0, 4.8, 4.7]
    print("\n - Welcome and Goodbye - ")
    time.sleep(1)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for char in baris_lagu:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("// By 1livesfin")

lirik_lagu()