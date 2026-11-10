"""
Python 3.20 - Nested Loop
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: NESTED LOOP DASAR ===")
for i in range(2):
    for j in range(3):
        print(i, j)

print("\n=== CONTOH 2: GRID 3 x 3 ===")
for baris in range(3):
    for kolom in range(3):
        print("Posisi:", baris, kolom)

print("\n=== CONTOH 3: TABEL PERKALIAN 1-3 ===")
for a in range(1, 4):
    for b in range(1, 4):
        print(a, "x", b, "=", a * b)

print("\n=== CONTOH 4: NESTED LIST ===")
data = [[1, 2], [3, 4], [5, 6]]

for baris in data:
    for nilai in baris:
        print(nilai)

print("\n=== CONTOH 5: KOMBINASI NAMA DAN HARI ===")
nama = ["Ani", "Budi"]
hari = ["Senin", "Selasa", "Rabu"]

for orang in nama:
    for h in hari:
        print(orang, "-", h)

print("\n=== CONTOH 6: NESTED LOOP + IF ===")
for i in range(3):
    for j in range(3):
        if i == j:
            print(i, j)

print("\n=== CONTOH 7: POLA BINTANG ===")
for baris in range(1, 5):
    for kolom in range(baris):
        print("*", end="")
    print()

print("\n=== CONTOH 8: POSISI PRINT ===")
for i in range(2):
    for j in range(3):
        print(i, j)
    print("Satu outer selesai")

print("\n=== CONTOH 9: TIGA LEVEL ===")
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k)

print("\n=== LATIHAN ===")
for baris in range(3):
    for kolom in range(4):
        print("Grid:", baris, kolom)
