"""
Python 7.2.1 - Methods of File Objects
"""

from datetime import datetime
from pathlib import Path
import sys


def siapkan_file_demo():
    Path("data.txt").write_text(
        "Baris 1: Python\n"
        "Baris 2: File Object\n"
        "Baris 3: ERROR contoh\n"
        "Baris 4: Selesai\n",
        encoding="utf-8",
    )


def demo_read():
    with open(
        "data.txt",
        "r",
        encoding="utf-8",
    ) as file:
        isi = file.read()
        print(isi)

        # Sudah EOF:
        print(
            "Read lagi:",
            repr(file.read()),
        )


def demo_read_size():
    with open(
        "data.txt",
        "r",
        encoding="utf-8",
    ) as file:
        while True:
            chunk = file.read(8)

            if chunk == "":
                break

            print(
                "chunk:",
                repr(chunk),
            )


def demo_readline():
    with open(
        "data.txt",
        "r",
        encoding="utf-8",
    ) as file:
        print(
            repr(file.readline())
        )
        print(
            repr(file.readline())
        )


def demo_readlines():
    with open(
        "data.txt",
        "r",
        encoding="utf-8",
    ) as file:
        lines = file.readlines()

    print(lines)

    for index, line in enumerate(
        lines,
        start=1,
    ):
        print(
            index,
            line.rstrip("\n"),
        )


def demo_for_line():
    jumlah_error = 0

    with open(
        "data.txt",
        "r",
        encoding="utf-8",
    ) as file:
        for line in file:
            if "ERROR" in line:
                jumlah_error += 1
                print(
                    "ERROR:",
                    line.rstrip(),
                )

    print(
        "Jumlah ERROR:",
        jumlah_error,
    )


def demo_write():
    nilai = 90

    with open(
        "nilai.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            "Nilai: "
            + str(nilai)
            + "\n"
        )

        jumlah = file.write(
            f"Nilai formatted: {nilai}\n"
        )

    print(
        "Karakter write kedua:",
        jumlah,
    )


def demo_append():
    with open(
        "append.log",
        "a",
        encoding="utf-8",
    ) as file:
        file.write(
            "Baris baru\n"
        )


def demo_tell_seek():
    with open(
        "data.txt",
        "rb",
    ) as file:
        print(
            "Posisi awal:",
            file.tell(),
        )

        print(
            "Baca 5 byte:",
            file.read(5),
        )

        pos = file.tell()

        print(
            "Posisi sekarang:",
            pos,
        )

        print(
            "Baca lagi:",
            file.read(5),
        )

        file.seek(pos)

        print(
            "Ulang dari posisi tadi:",
            file.read(5),
        )

        file.seek(0)

        print(
            "Kembali awal:",
            file.read(5),
        )


def demo_binary_copy():
    source = Path(
        "binary_source.bin"
    )

    source.write_bytes(
        bytes(
            range(32)
        )
    )

    with open(
        source,
        "rb",
    ) as src, open(
        "binary_copy.bin",
        "wb",
    ) as dst:

        while True:
            chunk = src.read(8)

            if not chunk:
                break

            dst.write(chunk)

    print(
        "Ukuran source:",
        source.stat().st_size,
    )

    print(
        "Ukuran copy:",
        Path(
            "binary_copy.bin"
        ).stat().st_size,
    )


def demo_flush():
    with open(
        "flush_demo.log",
        "a",
        encoding="utf-8",
    ) as file:
        file.write(
            "Data penting\n"
        )

        file.flush()

        print(
            "Buffer sudah di-flush."
        )


def demo_truncate():
    path = Path(
        "truncate_demo.txt"
    )

    path.write_text(
        "ABCDEFGHIJ",
        encoding="utf-8",
    )

    with open(
        path,
        "r+",
        encoding="utf-8",
    ) as file:
        file.seek(5)
        file.truncate()

    print(
        "Setelah truncate:",
        path.read_text(
            encoding="utf-8"
        ),
    )


def demo_isatty():
    print(
        "stdout isatty:",
        sys.stdout.isatty(),
    )


def tulis_log(
    pesan,
    level="INFO",
):
    waktu = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        "app.log",
        "a",
        encoding="utf-8",
    ) as file:
        file.write(
            f"{waktu} | "
            f"{level:<5} | "
            f"{pesan}\n"
        )


def baca_log():
    path = Path("app.log")

    if not path.exists():
        print(
            "Belum ada file log."
        )
        return

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:
        for line in file:
            print(
                line.rstrip()
            )


def filter_error():
    path = Path("app.log")

    if not path.exists():
        return

    print(
        "\n=== ERROR LOG ==="
    )

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:
        for line in file:
            if " | ERROR | " in line:
                print(
                    line.rstrip()
                )


def demo_logger():
    tulis_log(
        "Program mulai"
    )

    tulis_log(
        "File gagal dibuka",
        "ERROR",
    )

    tulis_log(
        "Program selesai"
    )

    baca_log()
    filter_error()


def main():
    print(
        "Python 7.2.1 - "
        "Methods of File Objects"
    )

    siapkan_file_demo()

    demo_read()
    demo_read_size()
    demo_readline()
    demo_readlines()
    demo_for_line()
    demo_write()
    demo_append()
    demo_tell_seek()
    demo_binary_copy()
    demo_flush()
    demo_truncate()
    demo_isatty()
    demo_logger()


if __name__ == "__main__":
    main()
