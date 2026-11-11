# Python 6.4.1 - Importing * From a Package
# Salin template berikut ke file/folder terpisah sesuai judulnya.

TEMPLATES = {
    'STRUKTUR': 'project/\n├── main.py\n└── myapp/\n    ├── __init__.py\n    ├── calculator.py\n    ├── report.py\n    └── internal.py\n',
    'calculator.py': 'def tambah(a, b):\n    return a + b\n\ndef total():\n    return "TOTAL DARI CALCULATOR"\n',
    'report.py': 'def buat_laporan():\n    return "Laporan dibuat"\n\ndef total():\n    return "TOTAL DARI REPORT"\n',
    '__init__.py tanpa __all__': 'APP_NAME = "Demo Package"\n\n# File calculator.py memang ada,\n# tetapi import * tidak otomatis memindai semua file package.\n',
    '__init__.py dengan import submodule': 'from . import calculator\nfrom . import report\n\nAPP_NAME = "Demo Package"\n',
    '__init__.py dengan __all__': '__all__ = [\n    "calculator",\n    "report",\n]\n',
    '__init__.py export function': 'from .calculator import tambah\nfrom .report import buat_laporan\n\n__all__ = [\n    "tambah",\n    "buat_laporan",\n]\n',
    'main.py import star': 'from myapp import *\n\nprint(calculator.tambah(2, 3))\nprint(report.buat_laporan())\n',
    'explicit import 1': 'import myapp.calculator\n\nprint(myapp.calculator.tambah(10, 5))\n',
    'explicit import 2': 'from myapp import calculator\n\nprint(calculator.tambah(10, 5))\n',
    'explicit import 3': 'from myapp.calculator import tambah\n\nprint(tambah(10, 5))\n',
    'collision concept': 'def total():\n    return "TOTAL LOCAL"\n\n# Setelah import * dari package yang juga mengekspor total,\n# binding bernama total dapat berubah tergantung nama yang diimpor.\n',
    'refactor before': 'from toko import *\nfrom laporan import *\n\ntotal = hitung_total(10000, 2)\ncetak(total)\n',
    'refactor after': 'from toko import transaksi\nfrom laporan import printer\n\ntotal = transaksi.hitung_total(10000, 2)\nprinter.cetak(total)\n',
}

def tampilkan_template(nama, isi):
    print("\n" + "=" * 70)
    print(nama)
    print("=" * 70)
    print(isi)

def main():
    for nama, isi in TEMPLATES.items():
        tampilkan_template(nama, isi)

if __name__ == "__main__":
    main()
