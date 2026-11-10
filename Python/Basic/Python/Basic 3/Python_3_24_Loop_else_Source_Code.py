"""
Python 3.24 - Loop else
else pada for/while berjalan jika loop selesai normal tanpa break.
"""

print("=== CONTOH 1: FOR ELSE - SELESAI NORMAL ===")
for i in range(3):
    print(i)
else:
    print("Loop selesai normal")

print("\n=== CONTOH 2: FOR ELSE - ADA BREAK ===")
for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("Ini tidak muncul")

print("\n=== CONTOH 3: PENCARIAN - DITEMUKAN ===")
angka = [10, 20, 30, 40]
target = 30

for n in angka:
    if n == target:
        print("Ditemukan")
        break
else:
    print("Tidak ditemukan")

print("\n=== CONTOH 4: PENCARIAN - TIDAK DITEMUKAN ===")
angka = [10, 20, 30, 40]
target = 99

for n in angka:
    if n == target:
        print("Ditemukan")
        break
else:
    print("Tidak ditemukan")

print("\n=== CONTOH 5: WHILE ELSE - SELESAI NORMAL ===")
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("while selesai normal")

print("\n=== CONTOH 6: WHILE ELSE - ADA BREAK ===")
i = 1

while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("Ini tidak muncul")

print("\n=== CONTOH 7: CONTINUE TIDAK MEMBATALKAN ELSE ===")
for i in range(4):
    if i == 1:
        continue
    print(i)
else:
    print("else tetap jalan")

print("\n=== CONTOH 8: PASS TIDAK MEMBATALKAN ELSE ===")
for i in range(3):
    if i == 1:
        pass
    print(i)
else:
    print("else jalan")

print("\n=== LATIHAN: CARI HURUF D ===")
data = ["A", "B", "C"]
target = "D"

for item in data:
    if item == target:
        print("Ketemu")
        break
else:
    print("Tidak ketemu")
