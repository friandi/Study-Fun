"""
Python 3.25 - Mini Project Cari Angka Genap/Ganjil
Gabungkan for, %, if, dan continue.
"""

print("=== VERSI 1: TAMPILKAN GENAP SAJA ===")
angka = [2, 5, 6, 9]

print("Angka genap:")
for n in angka:
    if n % 2 != 0:
        continue
    print(n)

print("\n=== VERSI 2: TAMPILKAN GANJIL SAJA ===")
print("Angka ganjil:")
for n in angka:
    if n % 2 == 0:
        continue
    print(n)

print("\n=== VERSI 3: LABEL GENAP / GANJIL ===")
for n in angka:
    if n % 2 == 0:
        print(n, "Genap")
    else:
        print(n, "Ganjil")

print("\n=== VERSI 4: RANGE 1 SAMPAI 10, GENAP SAJA ===")
for n in range(1, 11):
    if n % 2 != 0:
        continue
    print(n)

print("\n=== VERSI 5: HITUNG JUMLAH ANGKA GENAP ===")
angka = [2, 5, 6, 9, 10, 12, 13]
jumlah_genap = 0

for n in angka:
    if n % 2 != 0:
        continue
    jumlah_genap += 1

print("Jumlah angka genap:", jumlah_genap)

print("\n=== VERSI 6: SIMPAN ANGKA GENAP KE LIST BARU ===")
hasil_genap = []

for n in angka:
    if n % 2 != 0:
        continue
    hasil_genap.append(n)

print("List genap:", hasil_genap)

print("\n=== CATATAN: 0 ADALAH GENAP ===")
print("0 % 2 =", 0 % 2)
print("Jadi 0 termasuk angka genap.")

print("\n=== LATIHAN ===")
for n in range(1, 21):
    if n % 2 != 0:
        continue
    print(n)
