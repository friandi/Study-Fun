"""
Python 7.1.2 - The String format() Method
"""

def demo_dasar():
    print("Halo {}".format("Budi"))
    print("Nama: {}, Nilai: {}".format("Budi", 85))


def demo_positional():
    print(
        "{0} lulus dengan nilai {1}".format(
            "Budi",
            85,
        )
    )

    print(
        "Nilai {1} milik {0}".format(
            "Budi",
            85,
        )
    )

    print(
        "{0} + {0} = {1}".format(
            5,
            10,
        )
    )


def demo_keyword():
    print(
        "Nama: {nama}, Nilai: {nilai}".format(
            nama="Budi",
            nilai=85,
        )
    )

    print(
        "{nama} tinggal di {kota}".format(
            kota="Jakarta",
            nama="Budi",
        )
    )


def demo_positional_keyword():
    print(
        "{} ({umur} tahun)".format(
            "Budi",
            umur=30,
        )
    )

    print(
        "{0} tinggal di {kota}".format(
            "Budi",
            kota="Jakarta",
        )
    )


def demo_dictionary():
    data = {
        "nama": "Budi",
        "nilai": 85,
    }

    print(
        "Nama: {0[nama]}, "
        "Nilai: {0[nilai]}".format(
            data
        )
    )


def demo_dictionary_unpacking():
    data = {
        "nama": "Budi",
        "nilai": 85,
    }

    print(
        "Nama: {nama}, "
        "Nilai: {nilai}".format(
            **data
        )
    )


def demo_alignment():
    nama = "Budi"

    print("|{:<10}|".format(nama))
    print("|{:>10}|".format(nama))
    print("|{:^10}|".format(nama))

    print(
        "{:<15} {:>5} {:>12}".format(
            "Produk",
            "Qty",
            "Harga",
        )
    )

    print(
        "{:<15} {:>5} {:>12,.0f}".format(
            "Mouse",
            2,
            85000,
        )
    )


def tabel_angka():
    print()
    print("TABEL ANGKA")

    template = (
        "{:<4} {:>7} {:>9} {:>9}"
    )

    print(
        template.format(
            "No",
            "Nilai",
            "Kuadrat",
            "Kubik",
        )
    )

    print("-" * 32)

    for i in range(1, 6):
        print(
            template.format(
                i,
                i,
                i ** 2,
                i ** 3,
            )
        )


def tabel_produk():
    rows = [
        ("Mouse", 2, 85000),
        ("Keyboard", 1, 150000),
        ("Monitor", 2, 2_250_000),
    ]

    print()
    print("TABEL PRODUK")

    print(
        "{:<15} {:>5} {:>15}".format(
            "Produk",
            "Qty",
            "Harga",
        )
    )

    print("-" * 37)

    for nama, qty, harga in rows:
        print(
            "{:<15} {:>5} {:>15,.0f}"
            .format(
                nama,
                qty,
                harga,
            )
        )


def contoh_error():
    print()
    print("CONTOH ERROR (tidak dijalankan):")
    print(
        '# "{} {1}".format("A", "B") '
        "# ValueError: tidak boleh campur "
        "automatic dengan manual numbering"
    )

    print(
        '# "{nama}".format(data) '
        "# KeyError karena data tidak di-unpack"
    )


def main():
    print(
        "Python 7.1.2 - "
        "The String format() Method"
    )

    demo_dasar()
    demo_positional()
    demo_keyword()
    demo_positional_keyword()
    demo_dictionary()
    demo_dictionary_unpacking()
    demo_alignment()
    tabel_angka()
    tabel_produk()
    contoh_error()


if __name__ == "__main__":
    main()
