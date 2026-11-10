"""
Python 5.5 - Dictionaries
Penyimpanan Key dan Value.
"""

# =========================================================
# 5.5.1 APA ITU DICTIONARY?
# =========================================================
siswa = {
    "nama": "Budi",
    "umur": 16,
    "kelas": "X",
}

print(siswa)


# =========================================================
# 5.5.2 ANALOGI BUKU TELEPON
# =========================================================
telepon = {
    "Budi": "0812-1111-2222",
    "Siti": "0813-3333-4444",
    "Andi": "0857-5555-6666",
}

print(telepon["Siti"])


# =========================================================
# 5.5.3 KEY DAN VALUE
# =========================================================
produk = {
    "nama": "Mouse",
    "harga": 85000,
    "stok": 12,
    "aktif": True,
    "tag": ["gaming", "usb"],
}

print(produk)


# =========================================================
# 5.5.4 MEMBUAT DICTIONARY DENGAN {}
# =========================================================
kosong = {}
laptop = {
    "brand": "Lenovo",
    "ram": 16,
    "storage": 512,
    "harga": 12000000,
    "stok": True,
}

print(kosong)
print(laptop)


# =========================================================
# 5.5.5 MENGAMBIL DATA BERDASARKAN KEY
# =========================================================
print(siswa["nama"])
print(siswa["umur"])

user = {
    "nama": "Andy",
    "alamat": {
        "kota": "Jakarta",
        "kode_pos": "12730",
    },
}

print(user["alamat"]["kota"])


# =========================================================
# 5.5.6 MENAMBAHKAN KEY DAN VALUE
# =========================================================
produk = {"nama": "Mouse"}

produk["harga"] = 85000
produk["stok"] = 10

print(produk)


# =========================================================
# 5.5.7 MENGUBAH VALUE
# =========================================================
produk["harga"] = 90000
print(produk)

produk.update({
    "harga": 95000,
    "stok": 15,
})

print(produk)


# =========================================================
# 5.5.8 KEY HARUS UNIK
# =========================================================
data = {
    "a": 1,
    "a": 3,
}

print(data)  # {'a': 3}


# =========================================================
# 5.5.9 MENGHAPUS DENGAN del
# =========================================================
siswa = {
    "nama": "Budi",
    "umur": 16,
    "kelas": "X",
}

del siswa["kelas"]
print(siswa)


# =========================================================
# 5.5.10 KEYERROR
# =========================================================
try:
    print(siswa["email"])
except KeyError as error:
    print("KeyError:", error)


# =========================================================
# 5.5.11 get()
# =========================================================
print(siswa.get("nama"))
print(siswa.get("email"))
print(siswa.get("email", "-"))


# =========================================================
# 5.5.12 CEK KEY DENGAN in
# =========================================================
print("nama" in siswa)
print("Budi" in siswa)
print("Budi" in siswa.values())


# =========================================================
# 5.5.13 DAFTAR KEY
# =========================================================
print(siswa.keys())
print(list(siswa.keys()))

for key in siswa:
    print(key, "=", siswa[key])


# =========================================================
# 5.5.14 sorted() KEY
# =========================================================
data = {
    "umur": 16,
    "nama": "Budi",
    "alamat": "Jakarta",
}

print(sorted(data))

for key in sorted(data):
    print(key, "=", data[key])


# =========================================================
# 5.5.15 dict()
# =========================================================
a = dict(nama="Budi", umur=16)

b = dict([
    ("nama", "Budi"),
    ("umur", 16),
])

c = dict(zip(
    ["nama", "umur"],
    ["Budi", 16],
))

print(a)
print(b)
print(c)


# =========================================================
# 5.5.16 DICTIONARY COMPREHENSION
# =========================================================
kuadrat = {
    x: x * x
    for x in range(1, 6)
}

print(kuadrat)

genap = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}

print(genap)

label = {
    x: "genap" if x % 2 == 0 else "ganjil"
    for x in range(1, 11)
}

print(label)


# =========================================================
# 5.5.17 MERGE DENGAN **
# =========================================================
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

gabung = {
    **d1,
    **d2,
}

print(gabung)

# Python modern juga punya operator |
print(d1 | d2)


# =========================================================
# 5.5.18 STUDI KASUS PRODUK DAN HARGA
# =========================================================
harga_produk = {
    "Mouse": 85000,
    "Keyboard": 150000,
    "Monitor": 2000000,
}

print("Harga Mouse:", harga_produk["Mouse"])

harga_produk["Mouse"] = 90000
harga_produk["Webcam"] = 450000

print("Semua produk:")
for nama in sorted(harga_produk):
    print(nama, "=", harga_produk[nama])


# Nested Dictionary
produk_detail = {
    "P001": {
        "nama": "Mouse",
        "harga": 85000,
        "stok": 10,
    },
    "P002": {
        "nama": "Keyboard",
        "harga": 150000,
        "stok": 5,
    },
}

print(produk_detail["P001"]["harga"])

produk_detail["P001"]["stok"] -= 1

print(produk_detail)


# Lookup aman
nama_dicari = "Webcam"
harga = harga_produk.get(nama_dicari)

if harga is None:
    print("Produk tidak ditemukan")
else:
    print("Harga", nama_dicari, "=", harga)


# =========================================================
# MINI PROJECT - DATA PRODUK
# =========================================================
# Aktifkan blok berikut untuk latihan interaktif.
#
# produk = {}
#
# while True:
#     print("\n1. Tambah produk")
#     print("2. Lihat semua produk")
#     print("3. Cari produk")
#     print("4. Ubah harga")
#     print("5. Hapus produk")
#     print("6. Keluar")
#
#     pilihan = input("Pilih: ")
#
#     match pilihan:
#         case "1":
#             nama = input("Nama produk: ")
#             harga = int(input("Harga: "))
#             produk[nama] = harga
#             print("Produk disimpan")
#
#         case "2":
#             if not produk:
#                 print("Belum ada data")
#             else:
#                 for nama in sorted(produk):
#                     print(nama, "=", produk[nama])
#
#         case "3":
#             nama = input("Cari nama produk: ")
#             harga = produk.get(nama)
#
#             if harga is None:
#                 print("Produk tidak ditemukan")
#             else:
#                 print("Harga:", harga)
#
#         case "4":
#             nama = input("Nama produk: ")
#
#             if nama in produk:
#                 produk[nama] = int(input("Harga baru: "))
#                 print("Harga diperbarui")
#             else:
#                 print("Produk tidak ditemukan")
#
#         case "5":
#             nama = input("Nama produk: ")
#
#             if nama in produk:
#                 del produk[nama]
#                 print("Produk dihapus")
#             else:
#                 print("Produk tidak ditemukan")
#
#         case "6":
#             break
#
#         case _:
#             print("Pilihan tidak valid")
