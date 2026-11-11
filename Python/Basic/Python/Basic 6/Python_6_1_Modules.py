
# Python 6.1 - More on Modules
# File ini berisi TEMPLATE beberapa file yang bisa disalin.

HITUNG_PY = r'''
print("Module hitung dimuat")

PI = 3.14159

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    return a % b

def pangkat(a, b):
    return a ** b

if __name__ == "__main__":
    print("Tes langsung hitung.py")
    print("2 + 3 =", tambah(2, 3))
'''

CONFIG_PY = r'''
APP_NAME = "Kalkulator Modular"
VERSION = "1.0"
MAX_RETRY = 3
'''

MAIN_IMPORT = r'''
import hitung
import config

print(config.APP_NAME)
print("Versi:", config.VERSION)

print(hitung.tambah(10, 5))
print(hitung.kurang(10, 5))
print(hitung.kali(10, 5))
print(hitung.bagi(10, 5))
'''

MAIN_FROM_IMPORT = r'''
from hitung import tambah, kurang, kali

print(tambah(5, 2))
print(kurang(5, 2))
print(kali(5, 2))
'''

MAIN_ALIAS = r'''
import hitung as h

print(h.tambah(10, 5))
print(h.kali(4, 3))
'''

MAIN_FROM_ALIAS = r'''
from hitung import tambah as tambah_angka

print(tambah_angka(2, 3))
'''

MAIN_IMPORT_STAR = r'''
from hitung import *

print(tambah(2, 3))

# Sebaiknya hindari import * pada kode normal.
'''

MAIN_GLOBAL = r'''
import config

print(config.MAX_RETRY)
config.MAX_RETRY = 5
print(config.MAX_RETRY)
'''

MAIN_FIRST_IMPORT = r'''
import hitung
import hitung

# Top-level module normalnya hanya dieksekusi pada import pertama
# dalam proses Python yang sama.
'''

APP1_PY = r'''
import hitung
print(hitung.tambah(1, 2))
'''

APP2_PY = r'''
import hitung
print(hitung.kali(4, 5))
'''

MAIN_RELOAD = r'''
import hitung
import importlib

# Setelah hitung.py diedit:
importlib.reload(hitung)

print(hitung.tambah(2, 3))
'''

RELOAD_NOTE = r'''
from hitung import tambah
import hitung
import importlib

importlib.reload(hitung)

# Binding lokal "tambah" tidak otomatis berubah.
# Import ulang bila ingin binding baru:
from hitung import tambah
'''

NAME_DEMO = r'''
print(__name__)

if __name__ == "__main__":
    print("File dijalankan langsung")
else:
    print("File sedang di-import")
'''

def tampilkan_template(nama, isi):
    print("\n" + "=" * 60)
    print(nama)
    print("=" * 60)
    print(isi.strip())

if __name__ == "__main__":
    tampilkan_template("hitung.py", HITUNG_PY)
    tampilkan_template("config.py", CONFIG_PY)
    tampilkan_template("main.py - import module", MAIN_IMPORT)
    tampilkan_template("main.py - from import", MAIN_FROM_IMPORT)
    tampilkan_template("main.py - alias", MAIN_ALIAS)
    tampilkan_template("reload example", MAIN_RELOAD)
    tampilkan_template("__name__ example", NAME_DEMO)
