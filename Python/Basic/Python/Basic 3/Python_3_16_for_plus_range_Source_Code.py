"""
Python 3.16 - for + range()
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: range(stop) ===")
for i in range(5):
    print(i)

print("\n=== CONTOH 2: range(start, stop) ===")
for i in range(1, 6):
    print(i)

print("\n=== CONTOH 3: range(start, stop, step) ===")
for i in range(2, 11, 2):
    print(i)

print("\n=== CONTOH 4: ULANGI PESAN 3 KALI ===")
for i in range(3):
    print("Belajar Python")

print("\n=== CONTOH 5: NOMOR URUT ===")
for nomor in range(1, 6):
    print("Nomor", nomor)

print("\n=== CONTOH 6: PERHITUNGAN ===")
for i in range(1, 6):
    print(i, "x 2 =", i * 2)

print("\n=== CONTOH 7: TABEL PERKALIAN 5 ===")
angka = 5

for i in range(1, 11):
    print(angka, "x", i, "=", angka * i)

print("\n=== CONTOH 8: HITUNG TOTAL 1-5 ===")
total = 0

for i in range(1, 6):
    total = total + i

print("Total:", total)

print("\n=== CONTOH 9: FOR + IF ===")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print("\n=== CONTOH 10: COUNTDOWN ===")
for i in range(5, 0, -1):
    print(i)
print("Mulai!")

print("\n=== CONTOH 11: POLA BINTANG ===")
for i in range(1, 6):
    print("*" * i)

print("\n=== CONTOH 12: MEMBUAT LIST KUADRAT ===")
hasil = []

for i in range(1, 6):
    hasil.append(i * i)

print(hasil)

print("\n=== LATIHAN ===")
for i in range(1, 4):
    print(i * 10)
