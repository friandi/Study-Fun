"""
Python 3.26 - Mini Project Tebak Angka / Validasi Input
Gabungkan while, if, dan break.
"""

print("=== VERSI 1: DASAR ===")
angka_rahasia = 7

while True:
    tebakan = int(input("Tebak: "))

    if tebakan < angka_rahasia:
        print("Terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Terlalu besar")
    else:
        print("Benar!")
        break


print("\n=== VERSI 2: VALIDASI RENTANG 1-10 ===")
angka_rahasia = 7

while True:
    tebakan = int(input("Tebak 1-10: "))

    if tebakan < 1 or tebakan > 10:
        print("Masukkan angka 1-10")
        continue

    if tebakan < angka_rahasia:
        print("Terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Terlalu besar")
    else:
        print("Benar!")
        break


print("\n=== VERSI 3: VALIDASI INPUT BUKAN ANGKA ===")
angka_rahasia = 7

while True:
    try:
        tebakan = int(input("Tebak 1-10: "))
    except ValueError:
        print("Input harus berupa angka")
        continue

    if tebakan < 1 or tebakan > 10:
        print("Masukkan angka antara 1 sampai 10")
        continue

    if tebakan < angka_rahasia:
        print("Terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Terlalu besar")
    else:
        print("Benar!")
        break


print("\n=== VERSI 4: HITUNG JUMLAH PERCOBAAN ===")
angka_rahasia = 7
jumlah_percobaan = 0

while True:
    tebakan = int(input("Tebak: "))
    jumlah_percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil")
    elif tebakan > angka_rahasia:
        print("Terlalu besar")
    else:
        print("Benar!")
        print("Jumlah percobaan:", jumlah_percobaan)
        break


print("\n=== VERSI 5: BONUS ANGKA RANDOM ===")
# Aktifkan blok berikut jika ingin angka rahasia acak.
#
# import random
#
# angka_rahasia = random.randint(1, 10)
#
# while True:
#     tebakan = int(input("Tebak 1-10: "))
#
#     if tebakan < angka_rahasia:
#         print("Terlalu kecil")
#     elif tebakan > angka_rahasia:
#         print("Terlalu besar")
#     else:
#         print("Benar!")
#         break
