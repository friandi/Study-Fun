"""
Python 7.1.1 - Formatted String Literals - f-Strings
"""

def demo_variable():
    nama = "Budi"
    umur = 30

    print(f"Halo {nama}")
    print(f"Nama: {nama}, Umur: {umur}")


def demo_expression():
    a = 10
    b = 5

    print(f"{a + b=}")
    print(f"Kuadrat 7 = {7 ** 2}")

    nama = "budi"
    print(f"Nama kapital: {nama.upper()}")


def demo_braces():
    nilai = 10
    print(f"Data: {{nilai}} = {nilai}")


def demo_decimal():
    pi = 3.14159265

    print(f"2 desimal: {pi:.2f}")
    print(f"3 desimal: {pi:.3f}")


def demo_alignment():
    nama = "Budi"

    print(f"|{nama:<10}|")
    print(f"|{nama:>10}|")
    print(f"|{nama:^10}|")

    print(f"{'Produk':<15}{'Qty':>5}{'Harga':>12}")
    print(f"{'Mouse':<15}{2:>5}{85000:>12,}")


def demo_ribuan_persen():
    harga = 1_250_000
    rasio = 0.375

    print(f"Rp{harga:,}")
    print(f"Rp{harga:,.0f}")
    print(f"{rasio:.1%}")


def demo_conversion():
    teks = "Halo\nDunia"

    print(f"!s: {teks!s}")
    print(f"!r: {teks!r}")

    unicode_text = "café"
    print(f"!a: {unicode_text!a}")


def demo_debugging():
    harga = 10_000
    jumlah = 3
    total = harga * jumlah

    print(f"{harga=}")
    print(f"{jumlah=}")
    print(f"{total=}")
    print(f"{total=:,.0f}")
    print(f"{harga + jumlah=}")


def laporan_penjualan():
    penjualan = [
        {
            "produk": "Buku",
            "qty": 3,
            "harga": 25_000,
        },
        {
            "produk": "Pensil",
            "qty": 5,
            "harga": 5_000,
        },
        {
            "produk": "Penghapus",
            "qty": 2,
            "harga": 7_500,
        },
    ]

    total = sum(
        item["qty"] * item["harga"]
        for item in penjualan
    )

    print()
    print("=" * 52)
    print("LAPORAN PENJUALAN")
    print("=" * 52)

    print(
        f"{'Produk':<15}"
        f"{'Qty':>5}"
        f"{'Harga':>12}"
        f"{'Subtotal':>15}"
    )

    print("-" * 47)

    for item in penjualan:
        subtotal = (
            item["qty"]
            * item["harga"]
        )

        print(
            f"{item['produk']:<15}"
            f"{item['qty']:>5}"
            f"{item['harga']:>12,.0f}"
            f"{subtotal:>15,.0f}"
        )

    print("-" * 47)

    print(
        f"{'TOTAL':<32}"
        f"{total:>15,.0f}"
    )

    print()
    print("KONTRIBUSI")

    for item in penjualan:
        subtotal = (
            item["qty"]
            * item["harga"]
        )

        kontribusi = (
            subtotal / total
            if total
            else 0
        )

        print(
            f"{item['produk']:<15}"
            f"{kontribusi:>10.1%}"
        )


def main():
    print(
        "Python 7.1.1 - "
        "Formatted String Literals"
    )

    demo_variable()
    demo_expression()
    demo_braces()
    demo_decimal()
    demo_alignment()
    demo_ribuan_persen()
    demo_conversion()
    demo_debugging()
    laporan_penjualan()


if __name__ == "__main__":
    main()
