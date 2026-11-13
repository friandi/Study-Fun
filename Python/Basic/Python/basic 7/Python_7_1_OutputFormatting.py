"""
Python 7.1 - Fancier Output Formatting
Mengatur Tampilan Output
"""

from pathlib import Path
from string import Template


# =========================================================
# 7.1.0.1 OUTPUT FORMATTING
# =========================================================
def demo_formatting_dasar():
    nama = "Budi"
    nilai = 90
    harga = 1_500_000

    print("Raw:")
    print(nama, nilai, harga)

    print("\nFormatted:")
    print(f"Nama : {nama}")
    print(f"Nilai: {nilai}")
    print(f"Harga: Rp{harga:,.0f}")


# =========================================================
# 7.1.0.3 PRINT, EXPRESSION, WRITE
# =========================================================
def demo_print_write():
    print("print() menuju stdout secara default")

    path = Path("hasil_71.txt")

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:
        file.write("Baris 1\n")
        file.write("Baris 2\n")

    print("File dibuat:", path.resolve())


# =========================================================
# 7.1.0.4 STRING + VARIABLE
# =========================================================
def demo_gabung_string_variable():
    nama = "Budi"
    nilai = 90

    print("Nama:", nama, "Nilai:", nilai)

    print(
        "Nama: "
        + nama
        + ", Nilai: "
        + str(nilai)
    )

    print(
        f"Nama: {nama}, "
        f"Nilai: {nilai}"
    )


# =========================================================
# 7.1.0.5 str()
# =========================================================
def demo_str():
    angka = 100
    teks = str(angka)

    print("angka:", angka, type(angka))
    print("teks :", teks, type(teks))

    pesan = "Umur saya " + str(47)
    print(pesan)


# =========================================================
# 7.1.0.6 repr()
# =========================================================
def demo_repr():
    nama = "Budi"

    print("str :", str(nama))
    print("repr:", repr(nama))

    teks = "Halo\nPython"

    print("\nstr:")
    print(str(teks))

    print("\nrepr:")
    print(repr(teks))


# =========================================================
# 7.1.0.7 PERBANDINGAN str / repr
# =========================================================
def demo_str_vs_repr():
    data = [
        "A",
        "B",
        "C",
    ]

    print("str(data) :", str(data))
    print("repr(data):", repr(data))

    teks = "A\nB\tC"

    print("str(teks):")
    print(str(teks))

    print("repr(teks):")
    print(repr(teks))


# =========================================================
# 7.1.0.8 string.Template
# =========================================================
def demo_template():
    template = Template(
        "Halo, $nama"
    )

    print(
        template.substitute(
            nama="Budi"
        )
    )


def demo_template_mapping():
    data = {
        "nama": "Budi",
        "nilai": 90,
    }

    template = Template(
        "$nama mendapat nilai $nilai"
    )

    print(
        template.substitute(data)
    )


def demo_safe_substitute():
    template = Template(
        "Halo $nama, nilai $nilai"
    )

    print(
        template.safe_substitute(
            nama="Budi"
        )
    )


# =========================================================
# MINI PROJECT
# =========================================================
def laporan_nilai():
    nama = input(
        "Nama: "
    ).strip()

    try:
        nilai = float(
            input("Nilai: ")
        )
    except ValueError:
        print(
            "Nilai harus berupa angka."
        )
        return

    status = (
        "Lulus"
        if nilai >= 75
        else "Tidak Lulus"
    )

    # Versi f-string
    laporan = (
        f"Nama   : {nama}\n"
        f"Nilai  : {nilai}\n"
        f"Status : {status}"
    )

    print("\n=== LAPORAN ===")
    print(laporan)

    # Versi Template
    template = Template(
        "Nama   : $nama\n"
        "Nilai  : $nilai\n"
        "Status : $status"
    )

    laporan_template = (
        template.substitute(
            nama=nama,
            nilai=nilai,
            status=status,
        )
    )

    # Simpan ke file
    path = Path(
        "laporan_nilai.txt"
    )

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            laporan_template
            + "\n"
        )

    print(
        "\nDebug nama:",
        repr(nama),
    )

    print(
        "Laporan disimpan:",
        path.resolve(),
    )


def main():
    print(
        "Python 7.1 - "
        "Fancier Output Formatting"
    )
    print()

    demo_formatting_dasar()
    print()

    demo_print_write()
    print()

    demo_gabung_string_variable()
    print()

    demo_str()
    print()

    demo_repr()
    print()

    demo_str_vs_repr()
    print()

    demo_template()
    demo_template_mapping()
    demo_safe_substitute()

    # Aktifkan untuk mini project:
    # laporan_nilai()


if __name__ == "__main__":
    main()
