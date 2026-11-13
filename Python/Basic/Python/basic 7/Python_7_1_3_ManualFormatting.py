"""
Python 7.1.3 - Manual String Formatting
"""

def demo_concatenation():
    nama = "Budi"
    umur = 30

    print(
        "Nama: "
        + nama
        + " | Umur: "
        + str(umur)
    )


def demo_rjust():
    print("|" + "42".rjust(6) + "|")
    print("|" + "125".rjust(6) + "|")
    print("|" + "7".rjust(6) + "|")

    print("42".rjust(6, "0"))


def demo_ljust():
    print("|" + "Budi".ljust(10) + "|")
    print("|" + "Mouse".ljust(15) + "|")
    print("BAB 1".ljust(15, "."))


def demo_center():
    print("TOTAL".center(20, "-"))
    print("LAPORAN".center(30, "="))


def demo_zfill():
    print("42".zfill(5))
    print("-42".zfill(6))
    print("+42".zfill(6))

    for i in range(1, 6):
        kode = (
            "INV"
            + str(i).zfill(5)
        )
        print(kode)


def row(nama, qty, harga):
    return (
        nama.ljust(15)
        + str(qty).rjust(5)
        + str(harga).rjust(12)
    )


def demo_tabel_sederhana():
    print()
    print("TABEL PRODUK")

    print(
        "Produk".ljust(15)
        + "Qty".rjust(5)
        + "Harga".rjust(12)
    )

    print("-" * 32)

    print(row("Mouse", 2, 85000))
    print(row("Keyboard", 1, 150000))
    print(row("Monitor", 2, 2250000))


def kode_transaksi(no):
    return (
        "TRX"
        + str(no).zfill(5)
    )


def tabel_transaksi():
    transaksi = [
        (1, "Mouse", 2, 170_000),
        (2, "Keyboard", 1, 150_000),
        (3, "Monitor", 2, 4_500_000),
    ]

    print()
    print(
        " LAPORAN TRANSAKSI "
        .center(52, "=")
    )

    header = (
        "No Transaksi".ljust(15)
        + "Produk".ljust(15)
        + "Qty".rjust(5)
        + "Total".rjust(15)
    )

    print(header)
    print("-" * len(header))

    for no, produk, qty, total in transaksi:
        kode = kode_transaksi(no)

        total_text = (
            "{:,}".format(total)
        )

        baris = (
            kode.ljust(15)
            + produk.ljust(15)
            + str(qty).rjust(5)
            + total_text.rjust(15)
        )

        print(baris)


def latihan_tabel_nilai():
    data = [
        ("Andi", 90, "Lulus"),
        ("Budi", 75, "Lulus"),
        ("Citra", 65, "Tidak Lulus"),
    ]

    print()
    print("TABEL NILAI")

    header = (
        "Nama".ljust(15)
        + "Nilai".rjust(8)
        + "Status".rjust(15)
    )

    print(header)
    print("-" * len(header))

    for nama, nilai, status in data:
        print(
            nama.ljust(15)
            + str(nilai).rjust(8)
            + status.rjust(15)
        )


def main():
    print(
        "Python 7.1.3 - "
        "Manual String Formatting"
    )

    demo_concatenation()
    demo_rjust()
    demo_ljust()
    demo_center()
    demo_zfill()
    demo_tabel_sederhana()
    tabel_transaksi()
    latihan_tabel_nilai()


if __name__ == "__main__":
    main()
