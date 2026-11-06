"""
Python 3.4 - if ... else
Dua kemungkinan: True atau False.
"""

print("=== CONTOH 1: NILAI ===")
nilai = 80
if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")

print("\n=== CONTOH 2: NILAI FALSE ===")
nilai = 60
if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")

print("\n=== CONTOH 3: UMUR ===")
umur = 17
if umur >= 17:
    print("Dewasa")
else:
    print("Belum dewasa")

print("\n=== CONTOH 4: STOK ===")
stok = 0
if stok > 0:
    print("Tersedia")
else:
    print("Habis")

print("\n=== CONTOH 5: SALDO VS HARGA ===")
saldo = 50000
harga = 75000
if saldo >= harga:
    print("Bisa beli")
else:
    print("Saldo tidak cukup")

print("\n=== CONTOH 6: SUHU ===")
suhu = 28
if suhu > 30:
    print("Panas")
else:
    print("Tidak terlalu panas")

print("\n=== CONTOH 7: STRING ===")
status = "aktif"
if status == "aktif":
    print("Akun aktif")
else:
    print("Akun tidak aktif")

print("\n=== CONTOH 8: BOOLEAN ===")
login = False
if login:
    print("Selamat datang")
else:
    print("Silakan login")

print("\n=== CONTOH 9: GENAP / GANJIL ===")
angka = 7
if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")

print("\n=== CONTOH 10: DISKON ===")
total = 85000
if total >= 100000:
    print("Dapat diskon")
else:
    print("Belum dapat diskon")

print("\n=== LATIHAN: UBAH NILAI DI BAWAH ===")
nilai_latihan = 70
if nilai_latihan >= 75:
    print("Latihan: Lulus")
else:
    print("Latihan: Tidak lulus")
