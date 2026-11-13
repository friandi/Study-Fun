"""
Python 8.4 - Raising Exceptions
Membuat Kesalahan Secara Sengaja
"""


def validasi_umur(umur):
    if umur < 17:
        raise ValueError(
            f"Umur minimal 17 tahun. "
            f"Diterima: {umur}"
        )

    return umur


def validasi_qty(qty):
    if qty <= 0:
        raise ValueError(
            "Qty harus lebih dari 0"
        )

    return qty


def validasi_nilai(nilai):
    if not 0 <= nilai <= 100:
        raise ValueError(
            f"Nilai tidak valid: {nilai}. "
            "Nilai harus 0-100."
        )

    return nilai


def validasi_harga(harga):
    if harga <= 0:
        raise ValueError(
            "Harga harus lebih dari 0"
        )

    return harga


def validasi_transaksi(
    saldo,
    harga,
):
    if saldo < 0:
        raise ValueError(
            "Saldo tidak boleh negatif"
        )

    if harga <= 0:
        raise ValueError(
            "Harga harus lebih dari 0"
        )

    if saldo < harga:
        raise ValueError(
            f"Saldo tidak cukup. "
            f"Saldo: {saldo}, "
            f"Harga: {harga}"
        )

    return True


def proses_transaksi(
    umur,
    saldo,
    harga,
):
    validasi_umur(
        umur
    )

    validasi_transaksi(
        saldo,
        harga,
    )

    return (
        saldo
        - harga
    )


def demo_raise_vs_print():
    print(
        "\n=== PRINT SAJA ==="
    )

    saldo = 10_000
    harga = 25_000

    if saldo < harga:
        print(
            "Saldo tidak cukup"
        )

    print(
        "Dengan print, flow "
        "tetap bisa lanjut."
    )

    print(
        "\n=== RAISE ==="
    )

    try:
        if saldo < harga:
            raise ValueError(
                "Saldo tidak cukup"
            )

        print(
            "Baris ini tidak akan "
            "dijalankan bila raise terjadi."
        )

    except ValueError as error:
        print(
            "Ditangkap:",
            error,
        )


def demo_catch_raise():
    try:
        validasi_nilai(
            150
        )

    except ValueError as error:
        print(
            "Validasi gagal:",
            error,
        )


def demo_reraise():
    print(
        "\n=== RE-RAISE ==="
    )

    try:
        try:
            int(
                "abc"
            )

        except ValueError:
            print(
                "Layer bawah mencatat error."
            )

            raise

    except ValueError as error:
        print(
            "Layer atas menerima lagi:",
            error,
        )


def demo_studi_kasus():
    print(
        "\n=== STUDI KASUS ==="
    )

    skenario = [
        {
            "umur": 16,
            "saldo": 100_000,
            "harga": 30_000,
        },
        {
            "umur": 20,
            "saldo": 20_000,
            "harga": 50_000,
        },
        {
            "umur": 25,
            "saldo": 100_000,
            "harga": 30_000,
        },
    ]

    for no, data in enumerate(
        skenario,
        start=1,
    ):
        print(
            f"\nSkenario {no}:",
            data,
        )

        try:
            sisa = proses_transaksi(
                umur=data["umur"],
                saldo=data["saldo"],
                harga=data["harga"],
            )

        except ValueError as error:
            print(
                "Transaksi gagal:",
                error,
            )

        else:
            print(
                "Transaksi berhasil."
            )

            print(
                "Sisa saldo:",
                sisa,
            )


def main():
    print(
        "Python 8.4 - "
        "Raising Exceptions"
    )

    demo_raise_vs_print()
    demo_catch_raise()
    demo_reraise()
    demo_studi_kasus()


if __name__ == "__main__":
    main()
