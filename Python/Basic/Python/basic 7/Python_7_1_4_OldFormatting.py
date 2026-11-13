"""
Python 7.1.4 - Old String Formatting - Operator %
"""

def demo_string():
    nama = "Budi"
    print("Halo %s" % nama)

    umur = 30
    print("Umur: %s" % umur)


def demo_integer():
    umur = 30
    print("Umur: %d" % umur)

    angka = 42
    print("|%5d|" % angka)


def demo_float():
    pi = 3.14159

    print("Pi default: %f" % pi)
    print("Pi 2 desimal: %.2f" % pi)
    print("Pi 3 desimal: %.3f" % pi)
    print("Width + precision: |%10.2f|" % pi)


def demo_multiple_values():
    nama = "Budi"
    umur = 30
    nilai = 87.456

    print(
        "Nama: %s, Umur: %d, Nilai: %.2f"
        % (nama, umur, nilai)
    )


def demo_mapping():
    data = {
        "nama": "Budi",
        "nilai": 85,
    }

    print(
        "%(nama)s: %(nilai)d"
        % data
    )


def perbandingan():
    nama = "Budi"
    nilai = 85.25

    print("%s %.2f" % (nama, nilai))
    print("{} {:.2f}".format(nama, nilai))
    print(f"{nama} {nilai:.2f}")


def latihan_baca_kode():
    nama = "Andi"
    umur = 25
    print("%s berumur %d tahun" % (nama, umur))

    nilai = 87.456
    print("Nilai: %.1f" % nilai)


def refactor_demo():
    nama = "Budi"
    qty = 3
    total = 125000.75

    lama = "%s membeli %d barang, total %.2f" % (
        nama,
        qty,
        total,
    )

    modern = (
        f"{nama} membeli {qty} "
        f"barang, total {total:.2f}"
    )

    print("Lama  :", lama)
    print("Modern:", modern)
    print("Output sama:", lama == modern)


def contoh_error():
    print()
    print("Contoh error yang tidak dijalankan:")
    print('# "%s %d" % ("Budi",)  # nilai kurang')
    print('# "%s" % ("Budi", 30)   # struktur nilai tidak cocok')


def main():
    print("Python 7.1.4 - Old String Formatting")
    demo_string()
    demo_integer()
    demo_float()
    demo_multiple_values()
    demo_mapping()
    perbandingan()
    latihan_baca_kode()
    refactor_demo()
    contoh_error()


if __name__ == "__main__":
    main()
