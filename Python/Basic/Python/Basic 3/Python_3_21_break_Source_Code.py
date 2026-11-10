"""
Python 3.21 - break
Menghentikan loop lebih cepat.
"""

print("=== CONTOH 1: BREAK PADA FOR ===")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("\n=== CONTOH 2: PROGRAM LANJUT SETELAH BREAK ===")
for i in range(1, 6):
    if i == 3:
        break
    print(i)
print("Loop selesai")

print("\n=== CONTOH 3: MENCARI DATA ===")
data = [10, 20, 30, 40]
target = 30

for n in data:
    if n == target:
        print("Ditemukan")
        break

print("\n=== CONTOH 4: BREAK PADA WHILE ===")
i = 1

while True:
    print(i)
    if i == 3:
        break
    i += 1

print("\n=== CONTOH 5: MENU SEDERHANA ===")
# Aktifkan untuk mencoba input manual:
# while True:
#     pilihan = input("Ketik q untuk keluar: ")
#     if pilihan == "q":
#         break
#     print("Anda memilih:", pilihan)

print("\n=== CONTOH 6: NESTED LOOP ===")
for i in range(2):
    for j in range(3):
        if j == 1:
            break
        print(i, j)

print("\n=== CONTOH 7: VALIDASI INPUT ===")
# Aktifkan untuk mencoba:
# while True:
#     nilai = int(input("Nilai 0-100: "))
#     if 0 <= nilai <= 100:
#         break
#     print("Nilai tidak valid")
# print("Nilai valid:", nilai)

print("\n=== LATIHAN 1 ===")
for i in range(5):
    if i == 2:
        break
    print(i)

print("\n=== LATIHAN 2: CARI ANGKA 7 ===")
angka = [2, 4, 7, 9, 12]

for n in angka:
    print("Mengecek:", n)
    if n == 7:
        print("7 ditemukan")
        break

# Catatan:
# break di luar for/while akan menghasilkan SyntaxError.
