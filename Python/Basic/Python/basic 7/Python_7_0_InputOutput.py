"""
Python 7.0 - Pengenalan Input dan Output
Contoh-contoh utama untuk pemula.
"""

from pathlib import Path
import sys


# =========================================================
# 7.0.1 INPUT DAN OUTPUT
# =========================================================
def demo_input_output():
    nama = input("Nama Anda: ").strip()
    print("Halo", nama)


# =========================================================
# 7.0.2 INPUT - PROCESS - OUTPUT
# =========================================================
def demo_ipo():
    # INPUT
    a = 10
    b = 5

    # PROCESS
    hasil = a + b

    # OUTPUT
    print("Hasil:", hasil)


# =========================================================
# 7.0.3 STDIN / STDOUT / STDERR
# =========================================================
def demo_standard_streams():
    print("stdin :", sys.stdin)
    print("stdout:", sys.stdout)
    print("stderr:", sys.stderr)

    print("Ini output normal")
    print(
        "Ini contoh pesan error",
        file=sys.stderr,
    )


# =========================================================
# 7.0.4 print()
# =========================================================
def demo_print():
    print("Halo Python")
    print("Nama:", "Andy")
    print("2026", "11", "12", sep="-")
    print("Loading", end="...")
    print("selesai")

    nama = "Andy"
    nilai = 87.5
    print(f"Nama: {nama}, Nilai: {nilai}")


# =========================================================
# 7.0.5 input()
# =========================================================
def demo_input_number():
    while True:
        try:
            umur = int(input("Umur: "))
            break
        except ValueError:
            print("Masukkan angka bulat.")

    print("Tahun depan umur:", umur + 1)


# =========================================================
# 7.0.6 OUTPUT LAYAR DAN FILE
# =========================================================
def demo_text_file():
    path = Path("hasil.txt")

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:
        print("Andy", 90, file=file)

    print("File dibuat:", path.resolve())


# =========================================================
# 7.0.7 TEXT DAN BINARY
# =========================================================
def demo_binary_file():
    path = Path("data.bin")

    data = bytes([65, 66, 67])

    with path.open("wb") as file:
        file.write(data)

    with path.open("rb") as file:
        isi = file.read()

    print("Binary:", isi)
    print("Type  :", type(isi))


def demo_encode_decode():
    teks = "Halo"

    data = teks.encode("utf-8")
    kembali = data.decode("utf-8")

    print("teks   :", teks, type(teks))
    print("bytes  :", data, type(data))
    print("decode :", kembali)


# =========================================================
# 7.0.8 STUDI KASUS TRANSAKSI
# =========================================================
def transaksi_sederhana():
    print("=== PROGRAM TRANSAKSI ===")

    nama = input(
        "Nama pelanggan: "
    ).strip()

    produk = input(
        "Nama produk: "
    ).strip()

    try:
        harga = float(
            input("Harga satuan: ")
        )

        jumlah = int(
            input("Jumlah beli: ")
        )

        diskon_persen = float(
            input("Diskon (%): ")
        )

    except ValueError:
        print(
            "Harga, jumlah, dan diskon "
            "harus berupa angka.",
            file=sys.stderr,
        )
        return

    if harga < 0:
        print(
            "Harga tidak boleh negatif.",
            file=sys.stderr,
        )
        return

    if jumlah < 0:
        print(
            "Jumlah tidak boleh negatif.",
            file=sys.stderr,
        )
        return

    if not 0 <= diskon_persen <= 100:
        print(
            "Diskon harus 0 sampai 100.",
            file=sys.stderr,
        )
        return

    # PROCESS
    subtotal = harga * jumlah
    diskon = subtotal * (
        diskon_persen / 100
    )
    total = subtotal - diskon

    # OUTPUT KE LAYAR
    print("\n=== STRUK ===")
    print("Pelanggan:", nama)
    print("Produk    :", produk)
    print(
        f"Subtotal  : Rp{subtotal:,.0f}"
    )
    print(
        f"Diskon    : Rp{diskon:,.0f}"
    )
    print(
        f"Total     : Rp{total:,.0f}"
    )

    # OUTPUT KE FILE
    path = Path("struk.txt")

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            "=== STRUK ===\n"
        )
        file.write(
            f"Pelanggan: {nama}\n"
        )
        file.write(
            f"Produk    : {produk}\n"
        )
        file.write(
            f"Subtotal  : "
            f"Rp{subtotal:,.0f}\n"
        )
        file.write(
            f"Diskon    : "
            f"Rp{diskon:,.0f}\n"
        )
        file.write(
            f"Total     : "
            f"Rp{total:,.0f}\n"
        )

    print(
        "\nStruk disimpan ke:",
        path.resolve(),
    )


def main():
    print("Python 7.0 - Input dan Output")
    print()
    print("Contoh tersedia:")
    print("- demo_input_output()")
    print("- demo_ipo()")
    print("- demo_standard_streams()")
    print("- demo_print()")
    print("- demo_input_number()")
    print("- demo_text_file()")
    print("- demo_binary_file()")
    print("- demo_encode_decode()")
    print("- transaksi_sederhana()")
    print()
    print(
        "Aktifkan function yang ingin "
        "dicoba di bagian main()."
    )

    # Contoh non-interaktif:
    demo_ipo()
    demo_standard_streams()
    demo_print()
    demo_encode_decode()

    # Aktifkan satu per satu untuk praktik:
    # demo_input_output()
    # demo_input_number()
    # demo_text_file()
    # demo_binary_file()
    # transaksi_sederhana()


if __name__ == "__main__":
    main()
