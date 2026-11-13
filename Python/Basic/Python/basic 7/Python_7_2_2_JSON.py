"""
Python 7.2.2 - Saving Structured Data with JSON
"""

import json
from pathlib import Path
from datetime import datetime


def demo_dumps():
    data = {
        "nama": "Budi",
        "umur": 30,
        "aktif": True,
        "alamat": None,
    }

    teks = json.dumps(
        data,
        ensure_ascii=False,
    )

    print(teks)
    print(type(teks))


def demo_dump():
    data = {
        "nama": "José",
        "kota": "東京",
        "umur": 30,
    }

    with open(
        "contoh.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False,
        )


def demo_load():
    with open(
        "contoh.json",
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    print(data)
    print(type(data))


def demo_loads():
    teks = """
    {
      "nama": "Budi",
      "umur": 30
    }
    """

    data = json.loads(teks)

    print(data["nama"])
    print(type(data))


def demo_nested():
    data = {
        "pelanggan": [
            {
                "id": 1,
                "nama": "Budi",
                "telepon": [
                    "0811",
                    "0812",
                ],
                "alamat": {
                    "kota": "Jakarta",
                    "kode_pos": "12345",
                },
            }
        ]
    }

    print(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        )
    )


def demo_unsupported_type():
    data = {
        "tag": {
            "python",
            "json",
        }
    }

    try:
        json.dumps(data)
    except TypeError as error:
        print(
            "TypeError:",
            error,
        )

    data_benar = {
        "tag": list(
            data["tag"]
        )
    }

    print(
        json.dumps(
            data_benar,
            ensure_ascii=False,
        )
    )


def demo_datetime_conversion():
    data = {
        "waktu": (
            datetime.now()
            .isoformat()
        )
    }

    print(
        json.dumps(
            data,
            indent=2,
        )
    )


def demo_json_decode_error():
    teks_salah = """
    {
      "nama": "Budi",
    }
    """

    try:
        json.loads(
            teks_salah
        )

    except json.JSONDecodeError as error:
        print(
            "JSON tidak valid:"
        )
        print(error)


def simpan_data(
    data,
    path="pelanggan.json",
):
    with open(
        path,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False,
        )


def muat_data(
    path="pelanggan.json",
):
    try:
        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(
                file
            )

        if not isinstance(
            data,
            list,
        ):
            raise ValueError(
                "Format root JSON "
                "harus berupa List"
            )

        return data

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print(
            "File JSON rusak."
        )
        return []


def tambah_pelanggan(
    data,
    pelanggan_baru,
):
    if any(
        item.get("id")
        == pelanggan_baru["id"]
        for item in data
    ):
        raise ValueError(
            "ID sudah ada"
        )

    data.append(
        pelanggan_baru
    )


def cari_pelanggan(
    data,
    id_pelanggan,
):
    for item in data:
        if (
            item.get("id")
            == id_pelanggan
        ):
            return item

    return None


def tampilkan_semua(
    data,
):
    if not data:
        print(
            "Belum ada pelanggan."
        )
        return

    for item in data:
        print(
            f'{item.get("id")} | '
            f'{item.get("nama")} | '
            f'{item.get("email")}'
        )


def mini_project_pelanggan():
    path = "pelanggan.json"

    data = muat_data(
        path
    )

    pelanggan_baru = {
        "id": 1,
        "nama": "Budi",
        "email": "budi@example.com",
        "aktif": True,
        "alamat": {
            "kota": "Jakarta",
            "kode_pos": "12345",
        },
    }

    try:
        tambah_pelanggan(
            data,
            pelanggan_baru,
        )
    except ValueError as error:
        print(
            "Info:",
            error,
        )

    simpan_data(
        data,
        path,
    )

    print(
        "\n=== SEMUA PELANGGAN ==="
    )

    tampilkan_semua(
        data
    )

    print(
        "\n=== CARI ID 1 ==="
    )

    hasil = cari_pelanggan(
        data,
        1,
    )

    print(
        json.dumps(
            hasil,
            indent=2,
            ensure_ascii=False,
        )
        if hasil
        else "Tidak ditemukan"
    )


def main():
    print(
        "Python 7.2.2 - "
        "Saving Structured Data with JSON"
    )

    demo_dumps()
    demo_dump()
    demo_load()
    demo_loads()
    demo_nested()
    demo_unsupported_type()
    demo_datetime_conversion()
    demo_json_decode_error()
    mini_project_pelanggan()

    print(
        "\nPERINGATAN:"
    )
    print(
        "Jangan unpickle data "
        "dari sumber yang tidak tepercaya."
    )


if __name__ == "__main__":
    main()
