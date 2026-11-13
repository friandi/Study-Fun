"""
Python 8.0 - Pengenalan Errors and Exceptions
"""

def demo_syntax_error():
    contoh = """
if nilai >= 75
    print("Lulus")
"""
    print("Contoh SyntaxError (tidak dieksekusi):")
    print(contoh)
    print("Masalah: kurang tanda ':' setelah kondisi if.")


def demo_logic_error():
    harga = 100_000
    diskon = 10

    total_salah = harga - diskon

    potongan = harga * diskon / 100
    total_benar = harga - potongan

    print("Total salah :", total_salah)
    print("Total benar :", total_benar)


def demo_debugging():
    harga = 100_000
    diskon = 10

    print(f"{harga=}")
    print(f"{diskon=}")

    potongan = harga * diskon / 100
    print(f"{potongan=}")

    total = harga - potongan
    print(f"{total=}")


def demo_name_error():
    print("\nContoh NameError tidak dijalankan.")
    # Aktifkan untuk latihan:
    # print(total)


def demo_type_error():
    umur = "30"

    print("\nContoh TypeError tidak dijalankan.")
    # Salah:
    # print(umur + 1)

    # Benar:
    print(int(umur) + 1)


def demo_zero_division():
    angka = 10
    pembagi = 0

    print("\nContoh ZeroDivisionError tidak dijalankan.")
    # Aktifkan untuk melihat traceback:
    # print(angka / pembagi)

    if pembagi == 0:
        print("Pembagi tidak boleh 0.")
    else:
        print(angka / pembagi)


def demo_file_not_found():
    print("\nContoh FileNotFoundError tidak dijalankan.")
    # Aktifkan untuk latihan:
    # with open(
    #     "tidak_ada.txt",
    #     "r",
    #     encoding="utf-8",
    # ) as file:
    #     print(file.read())


def latihan_klasifikasi():
    contoh = [
        ("if x > 5 tanpa ':'", "Syntax Error"),
        ("10 / 0", "Runtime Exception"),
        ("diskon 10% dihitung sebagai -10", "Logic Error"),
        ("variable dipakai sebelum dibuat", "Runtime Exception / NameError"),
    ]

    print("\n=== LATIHAN KLASIFIKASI ===")

    for kasus, jenis in contoh:
        print(f"{kasus:<40} -> {jenis}")


def main():
    print("Python 8.0 - Pengenalan Errors and Exceptions")
    print()

    demo_syntax_error()
    demo_logic_error()
    demo_debugging()
    demo_name_error()
    demo_type_error()
    demo_zero_division()
    demo_file_not_found()
    latihan_klasifikasi()


if __name__ == "__main__":
    main()
