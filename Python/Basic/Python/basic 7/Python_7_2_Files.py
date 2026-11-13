"""
Python 7.2 - Reading and Writing Files
Membaca dan Menulis File
"""

from pathlib import Path


def demo_path():
    print("Current working directory:")
    print(Path.cwd())

    path = Path("data") / "produk.txt"
    print("Contoh relative path:", path)


def demo_write():
    with open(
        "hasil.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write("Baris 1\n")
        file.write("Baris 2\n")

    print("hasil.txt sudah ditulis.")


def demo_read():
    try:
        with open(
            "hasil.txt",
            "r",
            encoding="utf-8",
        ) as file:
            isi = file.read()

        print(isi)

    except FileNotFoundError:
        print("hasil.txt belum ada.")


def demo_append():
    with open(
        "log.txt",
        "a",
        encoding="utf-8",
    ) as file:
        file.write("Log baru\n")

    print("Data ditambahkan ke log.txt.")


def demo_rplus():
    path = Path("rplus_demo.txt")

    if not path.exists():
        path.write_text(
            "ABCDE",
            encoding="utf-8",
        )

    with open(
        path,
        "r+",
        encoding="utf-8",
    ) as file:
        awal = file.read()
        print("Isi awal:", awal)

        file.seek(0)
        file.write("XYZ")

    print(
        "Isi setelah r+:",
        path.read_text(
            encoding="utf-8"
        ),
    )


def demo_binary():
    data = bytes(
        [65, 66, 67, 68]
    )

    with open(
        "data.bin",
        "wb",
    ) as file:
        file.write(data)

    with open(
        "data.bin",
        "rb",
    ) as file:
        isi = file.read()

    print("Binary:", isi)
    print("Type  :", type(isi))


def demo_utf8():
    text = "Halo, café, 日本語"

    with open(
        "utf8.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(text)

    with open(
        "utf8.txt",
        "r",
        encoding="utf-8",
    ) as file:
        print(file.read())


def demo_newline():
    with open(
        "baris.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            "Baris 1\n"
            "Baris 2\n"
            "Baris 3\n"
        )

    with open(
        "baris.txt",
        "r",
        encoding="utf-8",
    ) as file:
        print(file.read())


def demo_close_manual():
    file = open(
        "hasil.txt",
        "r",
        encoding="utf-8",
    )

    print(
        "Sebelum close:",
        file.closed,
    )

    file.close()

    print(
        "Sesudah close:",
        file.closed,
    )


def demo_with_closed():
    with open(
        "hasil.txt",
        "r",
        encoding="utf-8",
    ) as file:
        print(
            "Di dalam with:",
            file.closed,
        )

    print(
        "Setelah with:",
        file.closed,
    )


def demo_file_not_found():
    try:
        with open(
            "tidak_ada.txt",
            "r",
            encoding="utf-8",
        ) as file:
            print(file.read())

    except FileNotFoundError:
        print(
            "File tidak ditemukan."
        )


def demo_permission(path):
    try:
        with open(
            path,
            "w",
            encoding="utf-8",
        ) as file:
            file.write("Data")

    except PermissionError:
        print(
            "Tidak punya izin "
            "menulis ke path tersebut."
        )


def buku_tamu():
    print("=== BUKU TAMU ===")

    nama = input(
        "Nama: "
    ).strip()

    pesan = input(
        "Pesan: "
    ).strip()

    if not nama:
        print("Nama wajib diisi.")
        return

    with open(
        "buku_tamu.txt",
        "a",
        encoding="utf-8",
    ) as file:
        file.write(
            nama
            + " | "
            + pesan
            + "\n"
        )

    print(
        "\nData tersimpan."
    )

    print(
        "\n=== ISI BUKU TAMU ==="
    )

    try:
        with open(
            "buku_tamu.txt",
            "r",
            encoding="utf-8",
        ) as file:
            print(file.read())

    except FileNotFoundError:
        print(
            "Belum ada buku tamu."
        )


def main():
    print(
        "Python 7.2 - "
        "Reading and Writing Files"
    )
    print()

    demo_path()
    demo_write()
    demo_read()
    demo_append()
    demo_rplus()
    demo_binary()
    demo_utf8()
    demo_newline()
    demo_close_manual()
    demo_with_closed()
    demo_file_not_found()

    # Aktifkan untuk latihan interaktif:
    # buku_tamu()


if __name__ == "__main__":
    main()
