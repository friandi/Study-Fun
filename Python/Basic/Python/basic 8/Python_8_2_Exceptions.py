"""
Python 8.2 - Exceptions
Kesalahan Saat Program Berjalan

Contoh yang benar-benar menghentikan program
diletakkan di function terpisah atau komentar.
"""


def contoh_zero_division():
    angka = 10
    pembagi = 0

    print("ZeroDivisionError")
    print("Aktifkan baris berikut untuk latihan:")
    print("# print(angka / pembagi)")

    if pembagi == 0:
        print("Pembagi tidak boleh 0.")


def contoh_name_error():
    print("\nNameError")
    print("Aktifkan:")
    print("# print(total)")


def contoh_type_error():
    umur = "30"

    print("\nTypeError")
    print("Contoh salah:")
    print('# print(umur + 1)')

    print("Contoh benar:")
    print(int(umur) + 1)


def contoh_value_error():
    print("\nValueError")
    print("Aktifkan:")
    print('# angka = int("sepuluh")')

    angka = int("10")
    print("Yang valid:", angka)


def contoh_index_error():
    data = [10, 20]

    print("\nIndexError")
    print("Data:", data)
    print("Index valid: 0 dan 1")
    print("# print(data[5])")


def contoh_key_error():
    data = {
        "nama": "Budi"
    }

    print("\nKeyError")
    print("Data:", data)
    print('# print(data["umur"])')

    print(
        "Aman dengan get():",
        data.get("umur"),
    )


def contoh_file_not_found():
    print("\nFileNotFoundError")
    print("Aktifkan:")
    print(
        '# open("tidak_ada.txt", "r")'
    )


def bagi(a, b):
    return a / b


def traceback_demo():
    print("\nTRACEBACK DEMO")
    print("Aktifkan:")
    print("# print(bagi(10, 0))")


def tabel_exception():
    data = [
        ("ZeroDivisionError", "pembagi nol"),
        ("NameError", "nama tidak ditemukan"),
        ("TypeError", "tipe tidak cocok"),
        ("ValueError", "nilai tidak valid"),
        ("IndexError", "index tidak ada"),
        ("KeyError", "key tidak ada"),
        ("FileNotFoundError", "file tidak ada"),
    ]

    print("\nEXCEPTION UMUM")
    for nama, penyebab in data:
        print(
            f"{nama:<22} -> {penyebab}"
        )


def main():
    print(
        "Python 8.2 - Exceptions"
    )

    contoh_zero_division()
    contoh_name_error()
    contoh_type_error()
    contoh_value_error()
    contoh_index_error()
    contoh_key_error()
    contoh_file_not_found()
    traceback_demo()
    tabel_exception()


if __name__ == "__main__":
    main()
