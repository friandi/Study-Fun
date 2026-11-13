"""
Python 8.8 - Predefined Clean-up Actions
Menggunakan with
"""


def siapkan_laporan():
    with open(
        "laporan.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            "Penjualan: 100\n"
        )
        file.write(
            "Biaya: 40\n"
        )
        file.write(
            "ERROR: contoh baris error\n"
        )
        file.write(
            "Laba: 60\n"
        )


def demo_read_with():
    print(
        "\n=== READ WITH ==="
    )

    with open(
        "laporan.txt",
        "r",
        encoding="utf-8",
    ) as file:
        isi = file.read()

    print(isi)
    print(
        "File closed:",
        file.closed,
    )


def demo_write_with():
    print(
        "\n=== WRITE WITH ==="
    )

    with open(
        "hasil.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(
            "Baris 1\n"
        )
        file.write(
            "Baris 2\n"
        )

    print(
        "hasil.txt selesai ditulis"
    )


def demo_append_with():
    print(
        "\n=== APPEND WITH ==="
    )

    with open(
        "hasil.txt",
        "a",
        encoding="utf-8",
    ) as file:
        file.write(
            "Baris tambahan\n"
        )


def demo_error_inside_with():
    print(
        "\n=== ERROR DI DALAM WITH ==="
    )

    file_ref = None

    try:
        with open(
            "laporan.txt",
            "r",
            encoding="utf-8",
        ) as file:
            file_ref = file

            print(
                file.readline().strip()
            )

            1 / 0

    except ZeroDivisionError:
        print(
            "ZeroDivisionError ditangani"
        )

    print(
        "File tetap closed:",
        file_ref.closed,
    )


def demo_try_finally_comparison():
    print(
        "\n=== TRY-FINALLY ==="
    )

    file = open(
        "laporan.txt",
        "r",
        encoding="utf-8",
    )

    try:
        isi = file.read()

    finally:
        file.close()

    print(
        "Closed:",
        file.closed,
    )

    print(
        "Panjang isi:",
        len(isi),
    )


class DemoContext:
    def __enter__(self):
        print(
            "Masuk context"
        )

        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        print(
            "Keluar context"
        )

        if exc_type is not None:
            print(
                "Ada exception:",
                exc_type.__name__,
            )

        return False


def demo_context_manager():
    print(
        "\n=== CUSTOM CONTEXT MANAGER ==="
    )

    with DemoContext():
        print(
            "Di dalam block with"
        )


def baca_laporan(path):
    try:
        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            return file.read()

    except FileNotFoundError:
        return None


def hitung_baris(path):
    try:
        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            return sum(
                1
                for _ in file
            )

    except FileNotFoundError:
        return 0


def cari_error(path):
    hasil = []

    try:
        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            for no, line in enumerate(
                file,
                start=1,
            ):
                if "ERROR" in line:
                    hasil.append(
                        (
                            no,
                            line.rstrip(),
                        )
                    )

    except FileNotFoundError:
        pass

    return hasil


def demo_studi_kasus():
    print(
        "\n=== STUDI KASUS LAPORAN ==="
    )

    laporan = baca_laporan(
        "laporan.txt"
    )

    if laporan is None:
        print(
            "File laporan tidak ditemukan"
        )

        return

    print(
        "ISI LAPORAN:"
    )
    print(
        laporan
    )

    print(
        "Jumlah baris:",
        hitung_baris(
            "laporan.txt"
        ),
    )

    print(
        "Baris ERROR:"
    )

    for no, line in cari_error(
        "laporan.txt"
    ):
        print(
            no,
            line,
        )


def main():
    print(
        "Python 8.8 - "
        "Predefined Clean-up Actions"
    )

    siapkan_laporan()
    demo_read_with()
    demo_write_with()
    demo_append_with()
    demo_error_inside_with()
    demo_try_finally_comparison()
    demo_context_manager()
    demo_studi_kasus()


if __name__ == "__main__":
    main()
