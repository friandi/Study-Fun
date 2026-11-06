"""
Python 3.9 - Perkenalan for
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: FOR PADA LIST BUAH ===")
buah = ["Apel", "Jeruk", "Mangga"]

for item in buah:
    print(item)

print("\n=== CONTOH 2: FOR PADA NAMA ===")
nama = ["Ani", "Budi", "Cici"]

for orang in nama:
    print("Halo", orang)

print("\n=== CONTOH 3: FOR PADA ANGKA ===")
angka = [10, 20, 30]

for n in angka:
    print(n * 2)

print("\n=== CONTOH 4: FOR PADA STRING ===")
kata = "PYTHON"

for huruf in kata:
    print(huruf)

print("\n=== CONTOH 5: MENGHITUNG TOTAL ===")
harga = [10000, 20000, 15000]
total = 0

for nilai in harga:
    total = total + nilai

print("Total:", total)

print("\n=== CONTOH 6: FOR + IF ===")
angka = [1, 2, 3, 4, 5]

for n in angka:
    if n % 2 == 0:
        print(n, "genap")

print("\n=== CONTOH 7: SETELAH LOOP ===")
for buah in ["Apel", "Jeruk"]:
    print(buah)

print("Selesai")

print("\n=== LATIHAN 1: CETAK NAMA ===")
daftar_nama = ["Andi", "Budi", "Citra"]

for nama in daftar_nama:
    print("Halo", nama)

print("\n=== LATIHAN 2: KALI 10 ===")
angka_latihan = [1, 2, 3, 4]

for n in angka_latihan:
    print(n * 10)
