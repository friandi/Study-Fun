"""
Python 6.2 - Standard Modules
Module Bawaan Python

Demo dibuat cross-platform sejauh mungkin.
winreg hanya di-import ketika berjalan di Windows.
"""

from pathlib import Path
import math
import os
import random
import sys


# =========================================================
# 6.2.1 STANDARD LIBRARY
# =========================================================
def demo_standard_library():
    print("=" * 70)
    print("STANDARD LIBRARY")
    print("=" * 70)

    print("Contoh module:")
    print("- sys")
    print("- math")
    print("- random")
    print("- os")
    print("- pathlib")


# =========================================================
# 6.2.2 BUILT-IN MODULE VS MODULE FILE
# =========================================================
def demo_builtin_module():
    print("\n" + "=" * 70)
    print("BUILT-IN MODULE")
    print("=" * 70)

    print("'sys' built-in:", "sys" in sys.builtin_module_names)
    print("Jumlah built-in names:", len(sys.builtin_module_names))

    # pathlib biasanya mempunyai file Python yang bisa dilihat.
    import pathlib
    print("pathlib.__file__:", pathlib.__file__)


# =========================================================
# 6.2.3 / 6.2.4 MODULE sys
# =========================================================
def demo_sys():
    print("\n" + "=" * 70)
    print("MODULE sys")
    print("=" * 70)

    print("sys.version:")
    print(sys.version)

    print("\nsys.version_info:")
    print(sys.version_info)

    print("\nsys.executable:")
    print(sys.executable)

    print("\nsys.platform:")
    print(sys.platform)


# =========================================================
# 6.2.5 sys.path
# =========================================================
def demo_sys_path():
    print("\n" + "=" * 70)
    print("sys.path")
    print("=" * 70)

    for nomor, folder in enumerate(sys.path):
        print(f"{nomor:>2}: {folder}")


# =========================================================
# 6.2.6 sys.ps1 / sys.ps2
# =========================================================
def demo_prompts():
    print("\n" + "=" * 70)
    print("INTERACTIVE PROMPTS")
    print("=" * 70)

    if hasattr(sys, "ps1"):
        print("sys.ps1:", repr(sys.ps1))
    else:
        print("sys.ps1 tidak tersedia karena program ini bukan interactive shell.")

    if hasattr(sys, "ps2"):
        print("sys.ps2:", repr(sys.ps2))
    else:
        print("sys.ps2 tidak tersedia karena program ini bukan interactive shell.")


# =========================================================
# 6.2.7 math
# =========================================================
def demo_math():
    print("\n" + "=" * 70)
    print("MODULE math")
    print("=" * 70)

    print("sqrt(25)   =", math.sqrt(25))
    print("pi         =", math.pi)
    print("ceil(4.2)  =", math.ceil(4.2))
    print("floor(4.8) =", math.floor(4.8))
    print("factorial(5) =", math.factorial(5))

    radius = 7
    luas = math.pi * radius ** 2
    print("Luas lingkaran r=7:", luas)


# =========================================================
# 6.2.8 random
# =========================================================
def demo_random():
    print("\n" + "=" * 70)
    print("MODULE random")
    print("=" * 70)

    print("Dadu:", random.randint(1, 6))
    print("Pilihan:", random.choice(["A", "B", "C"]))

    data = [1, 2, 3, 4]
    random.shuffle(data)
    print("Shuffle:", data)

    print("\nCATATAN:")
    print("Module random bukan pilihan untuk token/password security.")
    print("Untuk security, pelajari module secrets.")


# =========================================================
# 6.2.9 os dan pathlib
# =========================================================
def demo_os_pathlib():
    print("\n" + "=" * 70)
    print("os dan pathlib")
    print("=" * 70)

    print("os.getcwd():", os.getcwd())
    print("os.name:", os.name)

    current = Path.cwd()
    target = current / "data.txt"

    print("Path.cwd():", current)
    print("Contoh target:", target)
    print("Target exists:", target.exists())


# =========================================================
# 6.2.10 winreg
# =========================================================
def demo_winreg():
    print("\n" + "=" * 70)
    print("MODULE PLATFORM-SPECIFIC")
    print("=" * 70)

    if sys.platform == "win32":
        import winreg
        print("Windows terdeteksi.")
        print("HKEY_CURRENT_USER =", winreg.HKEY_CURRENT_USER)
    else:
        print("Platform:", sys.platform)
        print("winreg tidak di-import karena bukan Windows.")


# =========================================================
# MINI PROJECT - STANDARD LIBRARY EXPLORER
# =========================================================
def standard_library_explorer():
    while True:
        print("\n" + "=" * 40)
        print("STANDARD LIBRARY EXPLORER")
        print("=" * 40)
        print("1. Info Python")
        print("2. Hitung akar")
        print("3. Lempar dadu")
        print("4. Info folder")
        print("5. Cek platform")
        print("6. Keluar")

        pilihan = input("Pilih: ").strip()

        match pilihan:
            case "1":
                print("Version   :", sys.version_info)
                print("Executable:", sys.executable)

            case "2":
                try:
                    angka = float(input("Angka: "))
                    if angka < 0:
                        print("Untuk contoh real math.sqrt, angka harus >= 0.")
                    else:
                        print("Akar:", math.sqrt(angka))
                except ValueError:
                    print("Input harus berupa angka.")

            case "3":
                print("Dadu:", random.randint(1, 6))

            case "4":
                print("Current folder:", Path.cwd())

            case "5":
                print("Platform:", sys.platform)

                if sys.platform == "win32":
                    print("winreg tersedia pada Windows ini.")
                else:
                    print("winreg tidak digunakan pada platform ini.")

            case "6":
                print("Selesai.")
                break

            case _:
                print("Pilihan tidak valid.")


def main():
    demo_standard_library()
    demo_builtin_module()
    demo_sys()
    demo_sys_path()
    demo_prompts()
    demo_math()
    demo_random()
    demo_os_pathlib()
    demo_winreg()

    # Aktifkan untuk mencoba mini project interaktif:
    # standard_library_explorer()


if __name__ == "__main__":
    main()
