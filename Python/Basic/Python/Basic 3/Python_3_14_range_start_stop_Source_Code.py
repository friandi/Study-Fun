"""
Python 3.14 - range(start, stop)
Fokus: menentukan angka awal sendiri.
"""

print("=== CONTOH 1: range(2, 6) ===")
print(list(range(2, 6)))

print("\n=== CONTOH 2: 1 SAMPAI 5 ===")
for i in range(1, 6):
    print(i)

print("\n=== CONTOH 3: 5 SAMPAI 9 ===")
for i in range(5, 10):
    print(i)

print("\n=== CONTOH 4: ANGKA NEGATIF ===")
for i in range(-3, 2):
    print(i)

print("\n=== CONTOH 5: START SAMA DENGAN STOP ===")
print(list(range(5, 5)))

print("\n=== CONTOH 6: START LEBIH BESAR DARI STOP ===")
print(list(range(6, 2)))

print("\n=== CONTOH 7: NOMOR 1 SAMPAI 10 ===")
for nomor in range(1, 11):
    print("Nomor", nomor)

print("\n=== CONTOH 8: TOTAL 5 SAMPAI 8 ===")
total = 0

for i in range(5, 9):
    total = total + i

print("Total:", total)

print("\n=== CONTOH 9: TAHUN 2024 SAMPAI 2027 ===")
for tahun in range(2024, 2028):
    print(tahun)

print("\n=== LATIHAN ===")
for i in range(3, 6):
    print(i * 10)
