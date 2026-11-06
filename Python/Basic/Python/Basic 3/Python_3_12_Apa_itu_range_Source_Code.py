"""
Python 3.12 - Apa itu range()
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: range(stop) ===")
print(list(range(5)))

print("\n=== CONTOH 2: range() + for ===")
for i in range(5):
    print(i)

print("\n=== CONTOH 3: ULANGI 3 KALI ===")
for i in range(3):
    print("Belajar Python")

print("\n=== CONTOH 4: range(start, stop) ===")
print(list(range(2, 6)))

print("\n=== CONTOH 5: CETAK 2 SAMPAI 5 ===")
for i in range(2, 6):
    print(i)

print("\n=== CONTOH 6: range(start, stop, step) ===")
print(list(range(1, 10, 2)))

print("\n=== CONTOH 7: ANGKA GANJIL ===")
for i in range(1, 10, 2):
    print(i)

print("\n=== CONTOH 8: MENGHITUNG MUNDUR ===")
for i in range(5, 0, -1):
    print(i)

print("\n=== CONTOH 9: NOMOR URUT 1-5 ===")
for nomor in range(1, 6):
    print("Nomor", nomor)

print("\n=== CONTOH 10: TOTAL 1-5 ===")
total = 0

for i in range(1, 6):
    total = total + i

print("Total:", total)

print("\n=== LATIHAN ===")
print("0-9:", list(range(10)))
print("1-10:", list(range(1, 11)))
print("Genap 2-10:", list(range(2, 11, 2)))
print("Mundur 10-1:", list(range(10, 0, -1)))
