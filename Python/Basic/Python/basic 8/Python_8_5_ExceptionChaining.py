"""
Python 8.5 - Exception Chaining
Menghubungkan Kesalahan
"""


def demo_automatic_chaining():
    print("\n=== AUTOMATIC CHAINING ===")

    try:
        int("abc")

    except ValueError:
        try:
            1 / 0

        except ZeroDivisionError as error:
            print(
                "Jenis exception baru:",
                type(error).__name__,
            )
            print(
                "Context:",
                type(
                    error.__context__
                ).__name__,
            )


def demo_explicit_cause():
    print("\n=== EXPLICIT CAUSE ===")

    try:
        int("abc")

    except ValueError as old:
        try:
            raise RuntimeError(
                "Gagal memproses input"
            ) from old

        except RuntimeError as new:
            print(
                "Exception baru:",
                new,
            )
            print(
                "Cause:",
                type(
                    new.__cause__
                ).__name__,
            )


def demo_from_none():
    print("\n=== FROM NONE ===")

    try:
        int("abc")

    except ValueError:
        try:
            raise RuntimeError(
                "Format input salah"
            ) from None

        except RuntimeError as error:
            print(
                "Pesan:",
                error,
            )
            print(
                "Suppress context:",
                error.__suppress_context__,
            )


def baca_file(path):
    try:
        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            return file.read()

    except OSError as error:
        raise RuntimeError(
            f"Gagal membaca file: {path}"
        ) from error


def fake_db_insert(data):
    raise ConnectionError(
        "Database tidak dapat dihubungi"
    )


def simpan_database(data):
    try:
        fake_db_insert(
            data
        )

    except ConnectionError as error:
        raise RuntimeError(
            "Gagal menyimpan ke database"
        ) from error


def proses_data(path):
    try:
        data = baca_file(
            path
        )

        simpan_database(
            data
        )

    except RuntimeError as error:
        raise RuntimeError(
            "Proses sinkronisasi data gagal"
        ) from error


def demo_file_case():
    print("\n=== FILE CASE ===")

    try:
        baca_file(
            "tidak_ada.txt"
        )

    except RuntimeError as error:
        print(
            "Error aplikasi:",
            error,
        )

        print(
            "Root cause:",
            type(
                error.__cause__
            ).__name__,
        )


def demo_database_case():
    print("\n=== DATABASE CASE ===")

    try:
        simpan_database(
            "contoh data"
        )

    except RuntimeError as error:
        print(
            "Error aplikasi:",
            error,
        )

        print(
            "Root cause:",
            type(
                error.__cause__
            ).__name__,
        )


def demo_multilevel_chain():
    print("\n=== MULTI-LEVEL CHAIN ===")

    try:
        proses_data(
            "tidak_ada.txt"
        )

    except RuntimeError as error:
        print(
            "Level teratas:",
            error,
        )

        current = error
        level = 1

        while current is not None:
            print(
                f"Level {level}:",
                type(
                    current
                ).__name__,
                "-",
                current,
            )

            current = (
                current.__cause__
                or current.__context__
            )

            level += 1


def main():
    print(
        "Python 8.5 - "
        "Exception Chaining"
    )

    demo_automatic_chaining()
    demo_explicit_cause()
    demo_from_none()
    demo_file_case()
    demo_database_case()
    demo_multilevel_chain()


if __name__ == "__main__":
    main()
