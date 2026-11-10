"""
Python 3.23 - pass
Placeholder/no operation untuk blok yang belum diimplementasikan.
"""

print("=== CONTOH 1: PASS DASAR ===")
print("Mulai")
pass
print("Selesai")

print("\n=== CONTOH 2: PASS DI IF ===")
nilai = 90

if nilai >= 80:
    pass

print("Program lanjut")

print("\n=== CONTOH 3: PASS DI FOR ===")
for i in range(3):
    pass

print("Loop selesai")

print("\n=== CONTOH 4: PASS DI WHILE ===")
i = 0

while i < 3:
    pass
    i += 1

print("While selesai")

print("\n=== CONTOH 5: FUNCTION PLACEHOLDER ===")
def hitung_total():
    pass

print("Function berhasil didefinisikan")

print("\n=== CONTOH 6: CLASS PLACEHOLDER ===")
class Pelanggan:
    pass

p = Pelanggan()
print(p)

print("\n=== CONTOH 7: PASS VS CONTINUE ===")
print("PASS:")
for i in range(3):
    if i == 1:
        pass
    print(i)

print("CONTINUE:")
for i in range(3):
    if i == 1:
        continue
    print(i)

print("\n=== CONTOH 8: PASS VS BREAK ===")
print("PASS:")
for i in range(3):
    if i == 1:
        pass
    print(i)

print("BREAK:")
for i in range(3):
    if i == 1:
        break
    print(i)

print("\n=== CONTOH 9: FUNCTION YANG BELUM SELESAI ===")
def validasi_umur(umur):
    pass

hasil = validasi_umur(15)
print("Hasil:", hasil)   # None

print("\n=== LATIHAN ===")
for i in range(3):
    if i == 1:
        pass
    print(i)

# Catatan:
# pass tidak menghentikan program.
# pass tidak skip iteration.
# pass tidak keluar dari loop.
# pass hanya tidak melakukan apa-apa.
