"""
Python 5.6 - Looping Techniques
Teknik Perulangan Data.
"""

# =========================================================
# 5.6.1 PERULANGAN PADA KOLEKSI
# =========================================================
for x in [10, 20, 30]:
    print(x)

for x in ("A", "B"):
    print(x)

for x in {"merah", "biru"}:
    print(x)

for x in "Python":
    print(x)


# =========================================================
# 5.6.2 DICTIONARY.items()
# =========================================================
produk = {
    "Mouse": 85000,
    "Keyboard": 150000,
}

for nama, harga in produk.items():
    print(nama, harga)


# =========================================================
# 5.6.3 enumerate()
# =========================================================
nama_list = ["Andi", "Budi", "Cici"]

for index, nama in enumerate(nama_list):
    print(index, nama)

for nomor, nama in enumerate(nama_list, start=1):
    print(nomor, nama)


# =========================================================
# 5.6.4 zip()
# =========================================================
nilai_list = [80, 90, 75]

for nama, nilai in zip(nama_list, nilai_list):
    print(nama, nilai)

a = [1, 2, 3]
b = ["A", "B"]
print(list(zip(a, b)))


# =========================================================
# 5.6.5 reversed()
# =========================================================
data = [1, 2, 3, 4]

for x in reversed(data):
    print(x)

print("Asli:", data)


# =========================================================
# 5.6.6 sorted()
# =========================================================
data = [3, 1, 2]
hasil = sorted(data)

print("Asli :", data)
print("Urut :", hasil)

produk_data = [
    ("Mouse", 85000),
    ("Keyboard", 150000),
    ("Monitor", 2000000),
]

produk_urut = sorted(
    produk_data,
    key=lambda item: item[1],
)

print(produk_urut)


# =========================================================
# 5.6.7 set() UNTUK DUPLIKAT
# =========================================================
data = [1, 2, 2, 3, 3, 3]
unik = set(data)

print(unik)


# =========================================================
# 5.6.8 sorted(set())
# =========================================================
data = [3, 1, 2, 2, 3, 1]
unik_urut = sorted(set(data))

print(unik_urut)


# =========================================================
# 5.6.9 FILTER DENGAN for + if
# =========================================================
nilai = [60, 85, 70, 90, 55]
lulus = []

for n in nilai:
    if n >= 75:
        lulus.append(n)

print("Lulus:", lulus)

for n in nilai:
    if n < 75:
        continue

    print("Lulus:", n)


# =========================================================
# 5.6.10 JANGAN UBAH LIST SAAT ITERASI
# =========================================================
data = [1, 2, 3, 4, 5, 6]

# Cara aman 1: buat List baru
hasil = []

for x in data:
    if x % 2 != 0:
        hasil.append(x)

data_baru = hasil
print("List baru:", data_baru)

# Cara aman 2: iterasi copy
data = [1, 2, 3, 4, 5, 6]

for x in data.copy():
    if x % 2 == 0:
        data.remove(x)

print("Setelah remove aman:", data)


# =========================================================
# 5.6.11 DATA NUMERIK
# =========================================================
nilai = [80, 90, 70, 85]

total = 0

for n in nilai:
    total += n

rata = total / len(nilai)

print("Total:", total)
print("Rata-rata:", rata)

terbesar = nilai[0]
terkecil = nilai[0]
jumlah_lulus = 0

for n in nilai:
    if n > terbesar:
        terbesar = n

    if n < terkecil:
        terkecil = n

    if n >= 75:
        jumlah_lulus += 1

print("Terbesar:", terbesar)
print("Terkecil:", terkecil)
print("Jumlah lulus:", jumlah_lulus)


# =========================================================
# 5.6.12 STUDI KASUS NILAI SISWA
# =========================================================
nama_list = ["Andi", "Budi", "Cici", "Deni"]
nilai_list = [85, 70, 90, 85]

print("\nDaftar Nilai")
print("=" * 40)

for no, (nama, nilai) in enumerate(
    zip(nama_list, nilai_list),
    start=1,
):
    status = "Lulus" if nilai >= 75 else "Tidak Lulus"
    print(no, nama, nilai, status)

print("\nAnalisis:")
print("Nilai unik terurut:", sorted(set(nilai_list)))
print("Rata-rata:", sum(nilai_list) / len(nilai_list))
print("Tertinggi:", max(nilai_list))
print("Terendah:", min(nilai_list))

lulus = [
    nilai
    for nilai in nilai_list
    if nilai >= 75
]

print("Nilai lulus:", lulus)


# =========================================================
# LATIHAN TAMBAHAN
# =========================================================
harga = {
    "Mouse": 85000,
    "Monitor": 2000000,
    "Keyboard": 150000,
}

print("\nProduk terurut:")
for nama in sorted(harga):
    print(nama, harga[nama])

kota = [
    "Jakarta",
    "Bandung",
    "Jakarta",
    "Bogor",
    "Bandung",
]

print("Kota unik terurut:", sorted(set(kota)))
