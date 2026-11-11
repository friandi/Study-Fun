"""
Python 6.0 - Pengenalan Modules
File ini berisi contoh konsep dasar module.

CATATAN:
Untuk benar-benar mencoba import module buatan sendiri,
buat file calculator.py dan main.py secara terpisah
seperti contoh di bawah.
"""

# =========================================================
# CONTOH 1 - LOGIC YANG NANTI COCOK DIPINDAH KE MODULE
# =========================================================
def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        return "Error: tidak bisa dibagi 0"

    return a / b


print("Tanpa module:")
print(tambah(10, 5))
print(kurang(10, 5))
print(kali(10, 5))
print(bagi(10, 5))


# =========================================================
# PRAKTIK 2 FILE
# =========================================================
# Buat file calculator.py:
#
# def tambah(a, b):
#     return a + b
#
# def kurang(a, b):
#     return a - b
#
# def kali(a, b):
#     return a * b
#
# def bagi(a, b):
#     if b == 0:
#         return "Error: tidak bisa dibagi 0"
#
#     return a / b
#
#
# Lalu buat file main.py:
#
# import calculator
#
# print(calculator.tambah(10, 5))
# print(calculator.kurang(10, 5))
# print(calculator.kali(10, 5))
# print(calculator.bagi(10, 5))


# =========================================================
# PRAKTIK MODULE SALAM
# =========================================================
# Buat file salam.py:
#
# def sapa(nama):
#     return f"Halo {nama}"
#
#
# Buat file main_salam.py:
#
# import salam
#
# print(salam.sapa("Andy"))


# =========================================================
# CONTOH PEMBAGIAN TANGGUNG JAWAB
# =========================================================
# calculator.py
# - tambah
# - kurang
# - kali
# - bagi
#
# validator.py
# - validasi angka
# - validasi pembagian dengan 0
#
# main.py
# - menu
# - input user
# - memanggil function dari module lain


# =========================================================
# MINI PROJECT - STRUKTUR YANG DISARANKAN
# =========================================================
# kalkulator_app/
# ├── main.py
# ├── calculator.py
# └── validator.py
#
# Tujuan latihan:
# 1. Tulis function satu kali.
# 2. Gunakan dari file lain.
# 3. Hindari copy-paste logic.
# 4. Pisahkan tanggung jawab.
