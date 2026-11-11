"""
Python 6.3 - The dir() Function
Melihat Isi Module

File latihan untuk eksplorasi dir(), getattr(), callable(), builtins, dan help().
"""

import builtins
import math
import sys


# =========================================================
# 6.3.1 APA ITU dir()?
# =========================================================
def demo_dir_math():
    print("=" * 70)
    print("dir(math)")
    print("=" * 70)

    hasil = dir(math)

    print("Tipe hasil:", type(hasil))
    print("Jumlah nama:", len(hasil))
    print("10 nama pertama:", hasil[:10])


# =========================================================
# 6.3.3 dir() TANPA PARAMETER
# =========================================================
def demo_dir_tanpa_parameter():
    print("\n" + "=" * 70)
    print("dir() TANPA PARAMETER")
    print("=" * 70)

    angka = 10
    nama = "Andy"

    def sapa():
        return "Halo"

    print("Nama lokal yang terlihat:")
    print(dir())

    # Supaya variable dianggap benar-benar digunakan:
    print(angka, nama, sapa())


# =========================================================
# 6.3.4 dir(module)
# =========================================================
def demo_public_names(module):
    print("\n" + "=" * 70)
    print(f"NAMA PUBLIK: {getattr(module, '__name__', module)}")
    print("=" * 70)

    public_names = [
        nama
        for nama in dir(module)
        if not nama.startswith("_")
    ]

    for nama in public_names:
        print(nama)

    print("Jumlah nama publik:", len(public_names))


# =========================================================
# 6.3.5 ATTRIBUTE DAN METHOD
# =========================================================
def demo_attribute():
    print("\n" + "=" * 70)
    print("ATTRIBUTE")
    print("=" * 70)

    for nama in ["pi", "sqrt"]:
        obj = getattr(math, nama)

        print("Nama     :", nama)
        print("Object   :", obj)
        print("Type     :", type(obj))
        print("Callable :", callable(obj))
        print("-" * 40)


# =========================================================
# 6.3.6 MELIHAT ISI sys
# =========================================================
def demo_sys():
    print("\n" + "=" * 70)
    print("DIR SYS")
    print("=" * 70)

    hasil = dir(sys)

    print("Jumlah nama:", len(hasil))

    print("\nNama yang mengandung 'path':")
    for nama in hasil:
        if "path" in nama.lower():
            print(nama)


# =========================================================
# 6.3.7 builtins
# =========================================================
def demo_builtins():
    print("\n" + "=" * 70)
    print("BUILTINS")
    print("=" * 70)

    for nama in ["print", "open", "len", "int", "list"]:
        ada = nama in dir(builtins)
        obj = getattr(builtins, nama)

        print(
            nama,
            "| ada:", ada,
            "| type:", type(obj),
            "| callable:", callable(obj),
        )


# =========================================================
# 6.3.8 help()
# =========================================================
def demo_help():
    print("\n" + "=" * 70)
    print("HELP")
    print("=" * 70)

    print("Contoh gunakan:")
    print("help(math.sqrt)")
    print("help(str.upper)")
    print("help(len)")

    # Uncomment satu per satu jika ingin membaca output bantuan:
    # help(math.sqrt)
    # help(str.upper)
    # help(len)


# =========================================================
# MODULE EXPLORER
# =========================================================
MODULES = {
    "1": math,
    "2": sys,
    "3": builtins,
}


def module_explorer():
    while True:
        print("\n" + "=" * 50)
        print("MODULE EXPLORER")
        print("=" * 50)
        print("1. math")
        print("2. sys")
        print("3. builtins")
        print("4. Keluar")

        pilihan = input("Pilih module: ").strip()

        if pilihan == "4":
            break

        module = MODULES.get(pilihan)

        if module is None:
            print("Pilihan tidak valid.")
            continue

        names = [
            nama
            for nama in dir(module)
            if not nama.startswith("_")
        ]

        print("\nNama publik:")
        for nama in names:
            print("-", nama)

        print("\nJumlah:", len(names))

        callable_names = []

        for nama in names:
            try:
                obj = getattr(module, nama)
            except Exception:
                continue

            if callable(obj):
                callable_names.append(nama)

        print("\nNama callable:")
        for nama in callable_names:
            print("-", nama)

        target = input(
            "\nKetik nama attribute untuk diperiksa "
            "(Enter untuk lewati): "
        ).strip()

        if not target:
            continue

        if target not in dir(module):
            print("Nama tidak ditemukan.")
            continue

        obj = getattr(module, target)

        print("Object   :", obj)
        print("Type     :", type(obj))
        print("Callable :", callable(obj))

        lihat_help = input("Tampilkan help()? (y/n): ").lower()

        if lihat_help == "y":
            help(obj)


def main():
    demo_dir_math()
    demo_dir_tanpa_parameter()
    demo_public_names(math)
    demo_attribute()
    demo_sys()
    demo_builtins()
    demo_help()

    # Aktifkan untuk mini project interaktif:
    # module_explorer()


if __name__ == "__main__":
    main()
