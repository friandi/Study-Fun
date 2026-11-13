"""
Python 8.6 - User-defined Exceptions
Membuat Jenis Exception
"""


class DataTidakValidError(Exception):
    """Custom exception sederhana."""
    pass


class StokHabisError(Exception):
    def __init__(
        self,
        pesan,
        stok,
        permintaan,
    ):
        super().__init__(
            pesan
        )
        self.stok = stok
        self.permintaan = permintaan


class SaldoTidakCukupError(Exception):
    def __init__(
        self,
        pesan,
        saldo,
        kebutuhan,
    ):
        super().__init__(
            pesan
        )

        self.pesan = pesan
        self.saldo = saldo
        self.kebutuhan = kebutuhan
        self.selisih = (
            kebutuhan
            - saldo
        )


def validasi_data(nilai):
    if nilai is None:
        raise DataTidakValidError(
            "Data tidak boleh None"
        )

    return nilai


def ambil_stok(
    stok,
    permintaan,
):
    if stok < 0:
        raise ValueError(
            "Stok tidak boleh negatif"
        )

    if permintaan <= 0:
        raise ValueError(
            "Permintaan harus > 0"
        )

    if permintaan > stok:
        raise StokHabisError(
            "Stok tidak mencukupi",
            stok,
            permintaan,
        )

    return (
        stok
        - permintaan
    )


def transaksi(
    saldo,
    kebutuhan,
):
    if saldo < 0:
        raise ValueError(
            "Saldo tidak boleh negatif"
        )

    if kebutuhan <= 0:
        raise ValueError(
            "Kebutuhan harus > 0"
        )

    if saldo < kebutuhan:
        raise SaldoTidakCukupError(
            "Saldo tidak cukup",
            saldo,
            kebutuhan,
        )

    return (
        saldo
        - kebutuhan
    )


def demo_custom_simple():
    print(
        "\n=== CUSTOM SEDERHANA ==="
    )

    try:
        validasi_data(
            None
        )

    except DataTidakValidError as error:
        print(
            "Custom exception:",
            error,
        )


def demo_stok():
    print(
        "\n=== STOK ==="
    )

    try:
        sisa = ambil_stok(
            stok=5,
            permintaan=10,
        )

    except StokHabisError as error:
        print(
            "Transaksi stok gagal:",
            error,
        )

        print(
            "Stok:",
            error.stok,
        )

        print(
            "Permintaan:",
            error.permintaan,
        )

    else:
        print(
            "Sisa stok:",
            sisa,
        )


def demo_saldo_gagal():
    print(
        "\n=== SALDO GAGAL ==="
    )

    try:
        sisa = transaksi(
            saldo=50_000,
            kebutuhan=75_000,
        )

    except SaldoTidakCukupError as error:
        print(
            error.pesan
        )

        print(
            "Saldo:",
            error.saldo,
        )

        print(
            "Kebutuhan:",
            error.kebutuhan,
        )

        print(
            "Kekurangan:",
            error.selisih,
        )

    else:
        print(
            "Sisa saldo:",
            sisa,
        )


def demo_saldo_berhasil():
    print(
        "\n=== SALDO BERHASIL ==="
    )

    try:
        sisa = transaksi(
            saldo=100_000,
            kebutuhan=30_000,
        )

    except SaldoTidakCukupError as error:
        print(
            "Gagal:",
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
        "Python 8.6 - "
        "User-defined Exceptions"
    )

    demo_custom_simple()
    demo_stok()
    demo_saldo_gagal()
    demo_saldo_berhasil()


if __name__ == "__main__":
    main()
