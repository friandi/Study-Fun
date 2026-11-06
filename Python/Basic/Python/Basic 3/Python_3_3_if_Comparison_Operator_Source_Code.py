"""
Python 3.3 - if + Comparison Operator
Materi latihan untuk pemula.
Jalankan satu bagian demi satu bagian.
"""

print("=== CONTOH 1: >= ===")
nilai = 80
if nilai >= 75:
    print("Lulus")

print("\n=== CONTOH 2: < ===")
umur = 12
if umur < 17:
    print("Belum dewasa")

print("\n=== CONTOH 3: > ===")
suhu = 32
if suhu > 30:
    print("Cuaca panas")

print("\n=== CONTOH 4: == ===")
status = "aktif"
if status == "aktif":
    print("Akun aktif")

print("\n=== CONTOH 5: <= ===")
nilai_maks = 100
if nilai_maks <= 100:
    print("Nilai valid")

print("\n=== CONTOH 6: >= BATAS ===")
umur = 17
if umur >= 17:
    print("Memenuhi batas umur")

print("\n=== CONTOH 7: != ===")
status = "aktif"
if status != "blokir":
    print("Akun boleh digunakan")

print("\n=== CONTOH 8: SALDO VS HARGA ===")
saldo = 50000
harga = 30000
if saldo >= harga:
    print("Bisa beli")
print("Selesai")

print("\n=== CONTOH 9: STRING ===")
role = "admin"
if role == "admin":
    print("Menu admin")

print("\n=== CONTOH 10: EXPRESSION ===")
harga = 20000
jumlah = 3
if harga * jumlah >= 50000:
    print("Transaksi besar")

print("\n=== CONTOH 11: KONDISI FALSE BUKAN ERROR ===")
stok = 0
if stok > 0:
    print("Tersedia")
print("Selesai cek")

print("\n=== CONTOH 12: DUA IF BERDIRI SENDIRI ===")
umur = 25
saldo = 100000

if umur >= 17:
    print("Umur memenuhi")

if saldo >= 50000:
    print("Saldo memenuhi")

print("\n=== LATIHAN ===")
x = 10
print("10 < 20  =", x < 20)
print("10 > 20  =", x > 20)
print("10 == 10 =", x == 10)
print("10 <= 10 =", x <= 10)
print("10 >= 11 =", x >= 11)
print("10 != 11 =", x != 11)
