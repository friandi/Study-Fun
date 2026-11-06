"""
Python 3.10 - for dengan List
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: CETAK SEMUA ELEMEN ===")
buah = ["Apel", "Jeruk", "Mangga"]

for item in buah:
    print(item)

print("\n=== CONTOH 2: PROSES ANGKA ===")
angka = [10, 20, 30]

for n in angka:
    print(n * 2)

print("\n=== CONTOH 3: SAPA NAMA ===")
nama = ["Ani", "Budi", "Cici"]

for orang in nama:
    print("Halo", orang)

print("\n=== CONTOH 4: FOR + IF ===")
angka = [1, 2, 3, 4, 5, 6]

for n in angka:
    if n % 2 == 0:
        print(n)

print("\n=== CONTOH 5: HITUNG TOTAL ===")
harga = [10000, 20000, 15000]
total = 0

for nilai in harga:
    total = total + nilai

print("Total:", total)

print("\n=== CONTOH 6: HITUNG JUMLAH LULUS ===")
nilai_siswa = [80, 60, 90, 70]
jumlah_lulus = 0

for nilai in nilai_siswa:
    if nilai >= 75:
        jumlah_lulus = jumlah_lulus + 1

print("Jumlah lulus:", jumlah_lulus)

print("\n=== CONTOH 7: CARI DATA ===")
buah = ["Apel", "Jeruk", "Mangga"]

for item in buah:
    if item == "Jeruk":
        print("Jeruk ditemukan")

print("\n=== CONTOH 8: BUAT LIST BARU ===")
angka = [1, 2, 3]
hasil = []

for n in angka:
    hasil.append(n * 10)

print(hasil)

print("\n=== CONTOH 9: FILTER AMAN ===")
angka = [1, 2, 3, 4]
hasil_ganjil = []

for n in angka:
    if n % 2 != 0:
        hasil_ganjil.append(n)

print(hasil_ganjil)

print("\n=== CONTOH 10: LIST KOSONG ===")
data = []

for item in data:
    print(item)

print("Selesai")

print("\n=== LATIHAN ===")
angka_latihan = [5, 10, 15]
total_latihan = 0

for n in angka_latihan:
    total_latihan = total_latihan + n

print("Total latihan:", total_latihan)
