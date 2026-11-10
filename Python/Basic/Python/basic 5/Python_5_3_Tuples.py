"""
Python 5.3 - Tuples and Sequences
Contoh utama dari 13 submateri.
"""

# =========================================================
# 5.3.1 APA ITU SEQUENCE?
# =========================================================
list_data = [10, 20, 30]
tuple_data = (10, 20, 30)
text = "ABC"
angka = range(3)

print(list_data[0])
print(tuple_data[0])
print(text[0])
print(list(angka))


# =========================================================
# 5.3.2 APA ITU TUPLE?
# =========================================================
produk = ("P001", "Mouse", 85000)
print(produk)
print(type(produk))


# =========================================================
# 5.3.3 LIST VS TUPLE
# =========================================================
data_list = [1, 2, 3]
data_tuple = (1, 2, 3)

data_list[0] = 99
print(data_list)

# data_tuple[0] = 99  # TypeError


# =========================================================
# 5.3.4 MEMBUAT TUPLE
# =========================================================
a = (1, 2, 3)
b = 1, 2, 3

print(a)
print(b)
print(type(a))
print(type(b))


# =========================================================
# 5.3.5 INDEXING TUPLE
# =========================================================
t = (10, 20, 30, 40)

print(t[0])
print(t[2])
print(t[-1])
print(t[1:3])


# =========================================================
# 5.3.6 IMMUTABLE
# =========================================================
t = (10, 20, 30)

# t[0] = 99  # TypeError

temp = list(t)
temp[0] = 99
t = tuple(temp)

print(t)


# =========================================================
# 5.3.7 TUPLE KOSONG & SATU ELEMEN
# =========================================================
kosong = ()
satu = (5,)
bukan_tuple = (5)

print(type(kosong))
print(type(satu))
print(type(bukan_tuple))


# =========================================================
# 5.3.8 NESTED TUPLE
# =========================================================
nested = (
    (1, 2),
    (3, 4),
    (5, 6),
)

print(nested[0])
print(nested[1][0])


# =========================================================
# 5.3.9 TUPLE BERISI LIST
# =========================================================
t = ("A", [10, 20])

t[1].append(30)
t[1][0] = 99

print(t)

# t[1] = [1, 2, 3]  # TypeError


# =========================================================
# 5.3.10 TUPLE PACKING
# =========================================================
data = 10, 20, 30
produk = "P001", "Mouse", 85000

print(data)
print(produk)


# =========================================================
# 5.3.11 TUPLE UNPACKING
# =========================================================
produk = ("P001", "Mouse", 85000)

kode, nama, harga = produk

print(kode)
print(nama)
print(harga)


# =========================================================
# 5.3.12 SEQUENCE UNPACKING DAN *
# =========================================================
angka = (10, 20, 30, 40, 50)

pertama, *tengah, terakhir = angka

print("pertama:", pertama)
print("tengah:", tengah)
print("terakhir:", terakhir)

a, *sisa = angka
print(a, sisa)

*awal, z = angka
print(awal, z)


# =========================================================
# 5.3.13 STUDI KASUS PRODUK
# =========================================================
produk_list = [
    ("P001", "Mouse", 85000),
    ("P002", "Keyboard", 150000),
    ("P003", "Monitor", 2000000),
    ("P004", "Webcam", 450000),
    ("P005", "Headset", 300000),
]

print("\nDaftar Produk")
print("=" * 40)

for kode, nama, harga in produk_list:
    print(f"{kode} | {nama} | Rp{harga:,}")

produk_termahal = max(produk_list, key=lambda item: item[2])
print("\nProduk termahal:", produk_termahal)

total_harga = sum(harga for _, _, harga in produk_list)
print("Total harga:", total_harga)

produk_mahal = [
    produk
    for produk in produk_list
    if produk[2] > 100_000
]

print("Harga > 100000:")
for produk in produk_mahal:
    print(produk)
