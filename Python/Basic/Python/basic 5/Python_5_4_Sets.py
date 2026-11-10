"""
Python 5.4 - Sets
Kumpulan data unik dan operasi himpunan.
"""

# =========================================================
# 5.4.1 APA ITU SET?
# =========================================================
angka = {1, 2, 3}
buah = {"apel", "mangga", "jeruk"}

print(angka)
print(buah)


# =========================================================
# 5.4.2 SET VS LIST
# =========================================================
data_list = [1, 2, 2, 3]
data_set = {1, 2, 2, 3}

print("List:", data_list)
print("Set :", data_set)


# =========================================================
# 5.4.3 MEMBUAT SET DENGAN {}
# =========================================================
warna = {"merah", "hijau", "biru"}
print(warna)


# =========================================================
# 5.4.4 SET KOSONG
# =========================================================
a = {}
b = set()

print(type(a))  # dict
print(type(b))  # set


# =========================================================
# 5.4.5 MENGHILANGKAN DUPLIKAT
# =========================================================
data = [1, 2, 2, 3, 3, 3]
unik = set(data)

print("Unik:", unik)

# Jika urutan harus dipertahankan:
data_teks = ["A", "B", "A", "C", "B"]
unik_berurutan = list(dict.fromkeys(data_teks))
print("Unik berurutan:", unik_berurutan)


# =========================================================
# 5.4.6 MEMBERSHIP DENGAN in
# =========================================================
allowed = {"admin", "user", "guest"}

print("admin" in allowed)
print("root" in allowed)
print("root" not in allowed)


# =========================================================
# 5.4.7 UNION
# =========================================================
A = {1, 2, 3}
B = {3, 4, 5}

print("Union operator:", A | B)
print("Union method  :", A.union(B))


# =========================================================
# 5.4.8 INTERSECTION
# =========================================================
print("Intersection operator:", A & B)
print("Intersection method  :", A.intersection(B))


# =========================================================
# 5.4.9 DIFFERENCE
# =========================================================
print("A - B:", A - B)
print("B - A:", B - A)


# =========================================================
# 5.4.10 SYMMETRIC DIFFERENCE
# =========================================================
print("A ^ B:", A ^ B)
print("Method:", A.symmetric_difference(B))


# =========================================================
# 5.4.11 SET COMPREHENSION
# =========================================================
kuadrat = {x * x for x in range(6)}
print("Kuadrat:", kuadrat)

genap = {
    x
    for x in range(1, 11)
    if x % 2 == 0
}
print("Genap:", genap)

kata = ["apel", "ayam", "anggur", "bola"]
huruf_awal = {item[0] for item in kata}
print("Huruf awal:", huruf_awal)


# =========================================================
# 5.4.12 UNPACKING DALAM SET COMPREHENSION
# =========================================================
data_orang = [
    ("Andy", "Jakarta"),
    ("Budi", "Bandung"),
    ("Cici", "Jakarta"),
]

kota_unik = {
    kota
    for nama, kota in data_orang
}

print("Kota unik:", kota_unik)

records = [
    ("P001", "Mouse", 85000),
    ("P002", "Keyboard", 150000),
]

kode_set = {
    kode
    for kode, *sisa in records
}

print("Kode unik:", kode_set)


# =========================================================
# 5.4.13 STUDI KASUS - MINAT PELANGGAN
# =========================================================
tag_a = {"elektronik", "gaming", "buku"}
tag_b = {"gaming", "musik", "fashion"}

semua_tag = tag_a | tag_b
tag_bersama = tag_a & tag_b
unik_a = tag_a - tag_b
unik_b = tag_b - tag_a
hanya_salah_satu = tag_a ^ tag_b

print("\nSemua tag:", semua_tag)
print("Tag bersama:", tag_bersama)
print("Unik A:", unik_a)
print("Unik B:", unik_b)
print("Hanya salah satu:", hanya_salah_satu)


# =========================================================
# STUDI KASUS - EMAIL UNIK
# =========================================================
email = [
    "a@mail.com",
    "b@mail.com",
    "a@mail.com",
    "c@mail.com",
]

email_unik = set(email)

print("\nEmail unik:")
for item in email_unik:
    print(item)


# =========================================================
# LATIHAN
# =========================================================
X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}

print("\nLatihan:")
print("X | Y =", X | Y)
print("X & Y =", X & Y)
print("X - Y =", X - Y)
print("Y - X =", Y - X)
print("X ^ Y =", X ^ Y)

hasil = {
    x * x
    for x in range(1, 11)
    if x % 2 == 0
}

print("Kuadrat angka genap:", hasil)
