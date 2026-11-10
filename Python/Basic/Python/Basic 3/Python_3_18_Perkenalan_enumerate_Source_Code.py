"""
Python 3.18 - Perkenalan enumerate()
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: DASAR ENUMERATE ===")
nama = ["Ani", "Budi", "Cici"]

for i, item in enumerate(nama):
    print(i, item)

print("\n=== CONTOH 2: MELIHAT OBJECT ENUMERATE ===")
print(list(enumerate(nama)))

print("\n=== CONTOH 3: MULAI DARI 1 ===")
for nomor, item in enumerate(nama, start=1):
    print(nomor, item)

print("\n=== CONTOH 4: LIST HARGA ===")
harga = [10000, 20000, 15000]

for i, nilai in enumerate(harga):
    print("Index", i, "harga", nilai)

print("\n=== CONTOH 5: ENUMERATE + IF ===")
nilai = [80, 60, 90, 70]

for i, n in enumerate(nilai):
    if n >= 75:
        print(i, n, "Lulus")

print("\n=== CONTOH 6: STRING ===")
kata = "PYTHON"

for i, huruf in enumerate(kata):
    print(i, huruf)

print("\n=== CONTOH 7: STRING MULAI 1 ===")
kata = "CAT"

for nomor, huruf in enumerate(kata, start=1):
    print("Huruf ke-", nomor, ":", huruf)

print("\n=== CONTOH 8: MODIFIKASI LIST DENGAN INDEX ===")
angka = [1, 2, 3]

for i, nilai in enumerate(angka):
    angka[i] = nilai * 10

print(angka)

print("\n=== CONTOH 9: PERBANDINGAN DENGAN range(len()) ===")
nama = ["Ani", "Budi", "Cici"]

print("Cara range(len()):")
for i in range(len(nama)):
    print(i, nama[i])

print("Cara enumerate():")
for i, item in enumerate(nama):
    print(i, item)

print("\n=== LATIHAN ===")
data = ["A", "B", "C"]

for i, item in enumerate(data, start=1):
    print(i, item)
