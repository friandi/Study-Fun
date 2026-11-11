"""
Python 6.1.2 - The Module Search Path
Cara Python Mencari Module.

Jalankan file ini untuk melihat environment Python Anda sendiri.
"""

from pathlib import Path
import importlib.util
import os
import site
import sys


def tampilkan_info_python():
    print("=" * 70)
    print("PYTHON / ENVIRONMENT")
    print("=" * 70)

    print("Executable :", sys.executable)
    print("Version    :", sys.version.split()[0])
    print("CWD        :", Path.cwd())
    print("File       :", Path(__file__).resolve())
    print("File folder:", Path(__file__).resolve().parent)


def tampilkan_sys_path():
    print("\n" + "=" * 70)
    print("sys.path")
    print("=" * 70)

    for nomor, path in enumerate(sys.path):
        print(f"{nomor:>2}: {path}")


def tampilkan_pythonpath():
    print("\n" + "=" * 70)
    print("PYTHONPATH")
    print("=" * 70)

    value = os.environ.get("PYTHONPATH")
    print("PYTHONPATH =", value)


def tampilkan_site_packages():
    print("\n" + "=" * 70)
    print("SITE-PACKAGES")
    print("=" * 70)

    try:
        print("getsitepackages():")
        for path in site.getsitepackages():
            print(" -", path)
    except AttributeError:
        print("site.getsitepackages() tidak tersedia di environment ini.")

    print("User site:")
    print(" -", site.getusersitepackages())


def cek_module(nama_module):
    print("\n" + "=" * 70)
    print("CEK MODULE")
    print("=" * 70)

    try:
        spec = importlib.util.find_spec(nama_module)
    except (ModuleNotFoundError, ValueError) as error:
        print(f"{nama_module!r}: error saat pencarian:", error)
        return

    if spec is None:
        print(f"{nama_module!r}: TIDAK DITEMUKAN")
        return

    print(f"{nama_module!r}: DITEMUKAN")
    print("Origin :", spec.origin)
    print("Loader :", spec.loader)

    locations = spec.submodule_search_locations
    if locations is not None:
        print("Package locations:")
        for location in locations:
            print(" -", location)


def contoh_sys_path_append():
    """
    Contoh EDUKASI saja.

    Pada project nyata, lebih baik gunakan struktur package/project
    yang benar daripada bergantung pada sys.path.append() sembarangan.
    """
    shared_folder = Path(__file__).resolve().parent / "shared"

    print("\nContoh path tambahan:")
    print(shared_folder)

    # Untuk benar-benar menambahkan:
    # sys.path.append(str(shared_folder))


def main():
    tampilkan_info_python()
    tampilkan_sys_path()
    tampilkan_pythonpath()
    tampilkan_site_packages()

    # Cek module standard library.
    cek_module("json")

    # Cek contoh package pihak ketiga.
    cek_module("requests")

    # Contoh module yang kemungkinan tidak ada.
    cek_module("module_yang_tidak_ada_xyz")

    contoh_sys_path_append()


if __name__ == "__main__":
    main()
