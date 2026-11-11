"""
Python 6.1.3 - Compiled Python Files
Mengenal File .pyc

File ini dapat dijalankan untuk mengamati beberapa konsep.
Beberapa eksperimen perlu dilakukan dari terminal.
"""

from pathlib import Path
import compileall
import dis
import importlib.util
import sys


# =========================================================
# 6.1.3.1 BYTECODE
# =========================================================
def tambah(a, b):
    """Menjumlahkan dua angka."""
    return a + b


def demo_bytecode():
    print("=" * 70)
    print("BYTECODE DENGAN dis")
    print("=" * 70)
    dis.dis(tambah)


# =========================================================
# 6.1.3.3 / 6.1.3.7 CACHE TAG
# =========================================================
def demo_cache_tag():
    print("\n" + "=" * 70)
    print("CACHE TAG")
    print("=" * 70)

    print("sys.implementation.cache_tag =", sys.implementation.cache_tag)

    contoh_source = "hitung.py"
    print(
        "Contoh cache path:",
        importlib.util.cache_from_source(contoh_source)
    )


# =========================================================
# 6.1.3.8 COMPILEALL
# =========================================================
def demo_compileall():
    print("\n" + "=" * 70)
    print("COMPILEALL")
    print("=" * 70)

    folder = Path(__file__).resolve().parent
    print("Compile folder:", folder)

    # quiet=1 mengurangi output.
    ok = compileall.compile_dir(
        str(folder),
        quiet=1,
    )

    print("Berhasil:", ok)


# =========================================================
# 6.1.3.9 -O / -OO
# =========================================================
def fungsi_dengan_docstring():
    """Docstring ini hilang saat Python dijalankan dengan -OO."""
    return "Halo"


def demo_optimization():
    print("\n" + "=" * 70)
    print("OPTIMIZATION")
    print("=" * 70)

    print("__debug__ =", __debug__)
    print("Docstring  =", fungsi_dengan_docstring.__doc__)

    # CATATAN:
    # assert dihilangkan saat Python dijalankan dengan -O / -OO.
    nilai = 10
    assert nilai > 0, "Nilai harus positif"
    print("Assert lolos pada mode saat ini.")


# =========================================================
# EKSPERIMEN __pycache__
# =========================================================
INSTRUKSI = r"""
EKSPERIMEN MANUAL
=================

1. Buat hitung.py:

   def tambah(a, b):
       return a + b

2. Buat main.py:

   import hitung
   print(hitung.tambah(2, 3))

3. Jalankan:

   python main.py

4. Lihat folder:

   __pycache__/

5. Lihat nama cache, misalnya:

   hitung.cpython-315.pyc

   Tag aktual tergantung interpreter Anda.

6. Hapus __pycache__, lalu jalankan lagi.
   Jika caching diizinkan, cache akan dibuat kembali.

7. Coba compileall:

   python -m compileall .

8. Coba optimization level:

   python -O -m compileall .
   python -OO -m compileall .

9. Periksa nama cache:

   *.opt-1.pyc
   *.opt-2.pyc


PENTING
=======

- Menjalankan top-level script langsung, misalnya:

  python hitung.py

  tidak otomatis membuat .pyc untuk script itu hanya karena dijalankan.

- .pyc terutama merupakan cached bytecode untuk module yang di-import
  atau source yang diprecompile menggunakan tool seperti compileall.

- .pyc bukan .exe.

- Jangan gunakan assert untuk validasi bisnis/security yang wajib selalu
  dijalankan, karena assert dihilangkan pada mode -O dan -OO.
"""


def main():
    demo_bytecode()
    demo_cache_tag()
    demo_compileall()
    demo_optimization()

    print("\n" + INSTRUKSI)


if __name__ == "__main__":
    main()
