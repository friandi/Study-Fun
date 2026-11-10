"""
Python 5.2 - The del Statement
Menghapus data dengan del.
"""

# =========================================================
# 5.2.1 APA ITU del?
# =========================================================
data = [10, 20, 30, 40]
print("Awal:", data)


# =========================================================
# 5.2.2 HAPUS BERDASARKAN INDEX
# =========================================================
data = [10, 20, 30, 40]
del data[1]
print("del index 1:", data)

data = ["A", "B", "C"]
del data[-1]
print("del -1:", data)


# =========================================================
# 5.2.3 HAPUS DENGAN SLICING
# =========================================================
data = [10, 20, 30, 40, 50, 60]
del data[1:4]
print("del [1:4]:", data)

data = [0, 1, 2, 3, 4, 5, 6, 7]
del data[::2]
print("del [::2]:", data)


# =========================================================
# 5.2.4 KOSONGKAN LIST
# =========================================================
data = [1, 2, 3]
del data[:]
print("Setelah del data[:]:", data)

data.append(99)
print("Masih bisa dipakai:", data)


# =========================================================
# 5.2.5 HAPUS NAMA VARIABLE
# =========================================================
nama = "Budi"
print(nama)
del nama

# Jangan aktifkan tanpa try/except:
# print(nama)  # NameError

nama = "Baru"
print(nama)


# =========================================================
# 5.2.6 PERBANDINGAN
# =========================================================
data = [10, 20, 30, 40]

# del berdasarkan index
del data[1]
print("del:", data)

# remove berdasarkan nilai
data.remove(30)
print("remove:", data)

# pop menghapus dan mengembalikan nilai
item = data.pop()
print("pop result:", item)
print("setelah pop:", data)

# clear mengosongkan List
data.clear()
print("clear:", data)


# =========================================================
# 5.2.7 ERROR DAN VALIDASI
# =========================================================
data = [10, 20, 30]
index = 5

if 0 <= index < len(data):
    del data[index]
else:
    print("Index tidak valid:", index)

# Contoh menangkap IndexError
try:
    del data[10]
except IndexError as error:
    print("IndexError:", error)

# Contoh menangkap NameError
pesan = "Halo"
del pesan

try:
    print(pesan)
except NameError as error:
    print("NameError:", error)


# =========================================================
# 5.2.8 STUDI KASUS PELANGGAN
# =========================================================
pelanggan = ["Andi", "Budi", "Cici", "Deni"]

print("\nDaftar pelanggan:")
for nomor, nama in enumerate(pelanggan, start=1):
    print(nomor, nama)

pilihan = 2
index = pilihan - 1

if 0 <= index < len(pelanggan):
    del pelanggan[index]
    print("Pelanggan dihapus")
else:
    print("Pilihan tidak valid")

print("Setelah hapus:", pelanggan)


# =========================================================
# MINI PROJECT: MENU HAPUS PELANGGAN
# =========================================================
# Aktifkan untuk latihan interaktif.
#
# pelanggan = ["Andi", "Budi", "Cici"]
#
# while True:
#     print("\n1. Lihat pelanggan")
#     print("2. Hapus berdasarkan nomor")
#     print("3. Kosongkan daftar")
#     print("4. Keluar")
#
#     pilihan = input("Pilih: ")
#
#     match pilihan:
#         case "1":
#             if not pelanggan:
#                 print("Daftar kosong")
#             else:
#                 for nomor, nama in enumerate(pelanggan, start=1):
#                     print(nomor, nama)
#
#         case "2":
#             try:
#                 nomor = int(input("Nomor pelanggan: "))
#             except ValueError:
#                 print("Nomor harus berupa angka")
#                 continue
#
#             index = nomor - 1
#
#             if 0 <= index < len(pelanggan):
#                 del pelanggan[index]
#                 print("Pelanggan dihapus")
#             else:
#                 print("Nomor tidak valid")
#
#         case "3":
#             konfirmasi = input("Kosongkan semua data? (y/n): ")
#             if konfirmasi.lower() == "y":
#                 del pelanggan[:]
#                 print("Daftar dikosongkan")
#
#         case "4":
#             break
#
#         case _:
#             print("Pilihan tidak valid")
