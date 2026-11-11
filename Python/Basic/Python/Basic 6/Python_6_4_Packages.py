
# Python 6.4 - Packages
# File ini berisi template beberapa file.
# Salin setiap bagian ke file/folder sesuai judulnya.

STRUKTUR_MYAPP = r'''
project/
├── main.py
└── myapp/
    ├── __init__.py
    ├── calculator.py
    ├── report.py
    └── utils/
        ├── __init__.py
        ├── validator.py
        └── formatter.py
'''

CALCULATOR_PY = r'''
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan 0")
    return a / b
'''

REPORT_PY = r'''
def buat_laporan(judul):
    return f"Laporan: {judul}"
'''

VALIDATOR_PY = r'''
def cek_positif(angka):
    return angka > 0

def cek_tidak_kosong(teks):
    return bool(teks.strip())
'''

FORMATTER_PY = r'''
def format_rupiah(angka):
    return f"Rp{angka:,.0f}"
'''

INIT_PY = r'''
# myapp/__init__.py
# Boleh kosong, atau ekspor API:
from .calculator import tambah
'''

MAIN_FULL_IMPORT = r'''
import myapp.calculator
import myapp.utils.validator

print(myapp.calculator.tambah(10, 5))
print(myapp.utils.validator.cek_positif(10))
'''

MAIN_FROM_PACKAGE = r'''
from myapp import calculator

print(calculator.tambah(2, 3))
print(calculator.kali(4, 5))
'''

MAIN_DIRECT_FUNCTION = r'''
from myapp.calculator import tambah
from myapp.utils.validator import cek_positif

print(tambah(10, 20))
print(cek_positif(5))
'''

MAIN_ALIAS = r'''
import myapp.calculator as calc
from myapp.utils.validator import cek_positif as is_positive

print(calc.tambah(10, 5))
print(is_positive(100))
'''

NAMESPACE_PACKAGE_NOTE = r'''
Python modern mendukung namespace package tanpa __init__.py.

Contoh konsep:

location_A/
└── mycompany/
    └── finance/
        └── tax.py

location_B/
└── mycompany/
    └── hr/
        └── payroll.py

Jika kedua lokasi tersedia pada module search path,
namespace mycompany dapat mencakup keduanya.

Untuk belajar dasar, regular package dengan __init__.py
lebih sederhana.
'''

TOKO_STRUCTURE = r'''
toko_app/
├── main.py
└── toko/
    ├── __init__.py
    ├── produk.py
    ├── transaksi.py
    └── utils/
        ├── __init__.py
        └── validator.py
'''

TOKO_PRODUK_PY = r'''
produk = {
    "P001": {"nama": "Mouse", "harga": 85000},
    "P002": {"nama": "Keyboard", "harga": 150000},
}

def cari_produk(kode):
    return produk.get(kode)
'''

TOKO_TRANSAKSI_PY = r'''
def hitung_total(harga, jumlah):
    return harga * jumlah
'''

TOKO_VALIDATOR_PY = r'''
def validasi_jumlah(jumlah):
    return isinstance(jumlah, int) and jumlah > 0
'''

TOKO_INIT_PY = r'''
from .produk import cari_produk
'''

TOKO_MAIN_PY = r'''
from toko import cari_produk
from toko import transaksi
from toko.utils.validator import validasi_jumlah

kode = "P001"
jumlah = 2

item = cari_produk(kode)

if item is None:
    print("Produk tidak ditemukan")
elif not validasi_jumlah(jumlah):
    print("Jumlah tidak valid")
else:
    total = transaksi.hitung_total(item["harga"], jumlah)
    print("Produk:", item["nama"])
    print("Jumlah:", jumlah)
    print("Total :", total)
'''

def tampilkan_template(nama, isi):
    print("\n" + "=" * 70)
    print(nama)
    print("=" * 70)
    print(isi.strip())

if __name__ == "__main__":
    tampilkan_template("STRUKTUR myapp", STRUKTUR_MYAPP)
    tampilkan_template("myapp/calculator.py", CALCULATOR_PY)
    tampilkan_template("myapp/report.py", REPORT_PY)
    tampilkan_template("myapp/utils/validator.py", VALIDATOR_PY)
    tampilkan_template("myapp/__init__.py", INIT_PY)
    tampilkan_template("main.py - full import", MAIN_FULL_IMPORT)
    tampilkan_template("main.py - from package import module", MAIN_FROM_PACKAGE)
    tampilkan_template("main.py - direct function import", MAIN_DIRECT_FUNCTION)
    tampilkan_template("main.py - alias", MAIN_ALIAS)
    tampilkan_template("namespace package note", NAMESPACE_PACKAGE_NOTE)
    tampilkan_template("mini project structure", TOKO_STRUCTURE)
    tampilkan_template("mini project main.py", TOKO_MAIN_PY)
