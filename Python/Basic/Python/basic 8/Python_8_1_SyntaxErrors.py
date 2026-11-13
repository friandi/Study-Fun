"""
Python 8.1 - Syntax Errors
Contoh salah ditulis sebagai String agar file tetap dapat dijalankan.
"""

def tampilkan_contoh(judul, salah, benar):
    print("\n" + "=" * 60)
    print(judul)
    print("=" * 60)
    print("SALAH:")
    print(salah)
    print("\nBENAR:")
    print(benar)


def contoh_colon():
    salah = 'if nilai >= 75\n    print("Lulus")'
    benar = 'if nilai >= 75:\n    print("Lulus")'
    tampilkan_contoh("Tanda titik dua", salah, benar)


def contoh_parenthesis():
    salah = 'print(\n    "Halo"'
    benar = 'print(\n    "Halo"\n)'
    tampilkan_contoh("Kurung tidak ditutup", salah, benar)


def contoh_quote():
    salah = 'nama = "Budi'
    benar = 'nama = "Budi"'
    tampilkan_contoh("Quote tidak ditutup", salah, benar)


def contoh_keyword():
    salah = 'whille x < 5:\n    x += 1'
    benar = 'while x < 5:\n    x += 1'
    tampilkan_contoh("Keyword typo", salah, benar)


def contoh_indentation():
    salah = 'if aktif:\nprint("Ya")'
    benar = 'if aktif:\n    print("Ya")'
    tampilkan_contoh("IndentationError", salah, benar)


def contoh_unexpected_indent():
    salah = 'x = 10\n    print(x)'
    benar = 'x = 10\nprint(x)'
    tampilkan_contoh("Unexpected indent", salah, benar)


def contoh_nested():
    salah = 'if x > 0:\n    if x > 10:\n    print("Besar")'
    benar = 'if x > 0:\n    if x > 10:\n        print("Besar")'
    tampilkan_contoh("Nested indentation", salah, benar)


def daftar_keyword():
    import keyword
    print("\nKEYWORD PYTHON:")
    print(", ".join(keyword.kwlist))


def checklist():
    langkah = [
        "Baca pesan paling bawah",
        "Lihat nomor baris",
        "Periksa caret ^",
        "Cek baris sebelumnya",
        "Cek : () [] {} dan quote",
        "Cek keyword",
        "Cek indentation/tab/spasi",
        "Simpan lalu jalankan ulang",
    ]

    print("\nCHECKLIST:")
    for no, item in enumerate(langkah, start=1):
        print(f"{no}. {item}")


def main():
    print("Python 8.1 - Syntax Errors")
    contoh_colon()
    contoh_parenthesis()
    contoh_quote()
    contoh_keyword()
    contoh_indentation()
    contoh_unexpected_indent()
    contoh_nested()
    daftar_keyword()
    checklist()


if __name__ == "__main__":
    main()
