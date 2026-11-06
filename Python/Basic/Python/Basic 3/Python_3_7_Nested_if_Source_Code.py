"""
Python 3.7 - Nested if
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: UMUR + TIKET ===")
umur = 20
punya_tiket = True

if umur >= 17:
    if punya_tiket:
        print("Boleh masuk")

print("\n=== CONTOH 2: INNER ELSE ===")
umur = 20
punya_tiket = False

if umur >= 17:
    if punya_tiket:
        print("Boleh masuk")
    else:
        print("Perlu tiket dulu")

print("\n=== CONTOH 3: OUTER ELSE ===")
umur = 15
punya_tiket = True

if umur >= 17:
    if punya_tiket:
        print("Boleh masuk")
else:
    print("Belum cukup umur")

print("\n=== CONTOH 4: LENGKAP ===")
umur = 20
punya_tiket = False

if umur >= 17:
    if punya_tiket:
        print("Boleh masuk")
    else:
        print("Perlu tiket dulu")
else:
    print("Belum cukup umur")

print("\n=== CONTOH 5: LOGIN + ROLE ===")
login = True
role = "admin"

if login:
    if role == "admin":
        print("Menu Admin")
    else:
        print("Menu User")
else:
    print("Silakan login")

print("\n=== CONTOH 6: NILAI + KEHADIRAN ===")
nilai = 85
hadir = 90

if nilai >= 75:
    if hadir >= 80:
        print("Lulus")
    else:
        print("Nilai cukup, kehadiran kurang")
else:
    print("Nilai belum cukup")

print("\n=== CONTOH 7: SALDO + LIMIT ===")
saldo = 500000
jumlah = 200000
limit_transaksi = 300000

if saldo >= jumlah:
    if jumlah <= limit_transaksi:
        print("Transaksi boleh")
    else:
        print("Melebihi limit")
else:
    print("Saldo tidak cukup")

print("\n=== LATIHAN ===")
login = True
admin = False

if login:
    if admin:
        print("Admin")
    else:
        print("User")
else:
    print("Belum login")
