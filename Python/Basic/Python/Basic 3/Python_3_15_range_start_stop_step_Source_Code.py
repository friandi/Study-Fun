"""
Python 3.15 - range(start, stop, step)
Fokus: memahami step positif, step negatif, dan arah range.
"""

print("=== CONTOH 1: STEP POSITIF ===")
print(list(range(1, 10, 2)))

print("\n=== CONTOH 2: ANGKA GANJIL ===")
for i in range(1, 10, 2):
    print(i)

print("\n=== CONTOH 3: ANGKA GENAP ===")
for i in range(2, 11, 2):
    print(i)

print("\n=== CONTOH 4: LOMPAT 5 ===")
for i in range(0, 21, 5):
    print(i)

print("\n=== CONTOH 5: MENGHITUNG MUNDUR ===")
for i in range(5, 0, -1):
    print(i)

print("\n=== CONTOH 6: MUNDUR DUA-DUA ===")
for i in range(10, 0, -2):
    print(i)

print("\n=== CONTOH 7: ARAH SALAH - HASIL KOSONG ===")
print(list(range(5, 0, 1)))
print(list(range(0, 5, -1)))

print("\n=== CONTOH 8: KELIPATAN 5 ===")
for i in range(5, 51, 5):
    print(i)

print("\n=== CONTOH 9: COUNTDOWN ===")
for detik in range(5, 0, -1):
    print(detik)
print("Mulai!")

print("\n=== CONTOH 10: SETIAP 2 TAHUN ===")
for tahun in range(2020, 2031, 2):
    print(tahun)

print("\n=== LATIHAN ===")
print("2,4,6,8,10 =", list(range(2, 11, 2)))
print("1,4,7,10 =", list(range(1, 11, 3)))
print("10,8,6,4,2 =", list(range(10, 0, -2)))

# Catatan:
# range(1, 10, 0) akan menghasilkan ValueError
# karena step tidak boleh 0.
