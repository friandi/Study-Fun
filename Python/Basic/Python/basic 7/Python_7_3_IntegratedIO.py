"""
Python 7.3 - Latihan dan Studi Kasus Terpadu
Input, f-string, TXT, JSON, dan project transaksi.
"""

import json


def format_pelanggan(p):
    return (
        f"ID    : {p['id']}\n"
        f"Nama  : {p['nama']}\n"
        f"Email : {p['email']}\n"
        f"Kota  : {p['kota']}\n"
        f"Umur  : {p['umur']}\n"
    )


def simpan_txt(data, path="pelanggan.txt"):
    with open(path, "w", encoding="utf-8") as file:
        for p in data:
            file.write(format_pelanggan(p))
            file.write("-" * 30 + "\n")


def baca_txt(path="pelanggan.txt"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def append_txt(pelanggan, path="pelanggan.txt"):
    with open(path, "a", encoding="utf-8") as file:
        file.write(format_pelanggan(pelanggan))
        file.write("-" * 30 + "\n")


def simpan_pelanggan_json(data, path="pelanggan.json"):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False,
        )


def muat_pelanggan_json(path="pelanggan.json"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File JSON rusak.")
        return []


def update_pelanggan(data, id_pelanggan, **perubahan):
    for p in data:
        if p["id"] == id_pelanggan:
            p.update(perubahan)
            return True
    return False


def kode_transaksi(no):
    return "TRX" + str(no).zfill(5)


def buat_transaksi(no, pelanggan, produk, qty, harga):
    if not pelanggan.strip():
        raise ValueError("Pelanggan wajib diisi")
    if not produk.strip():
        raise ValueError("Produk wajib diisi")
    if qty <= 0:
        raise ValueError("Qty harus > 0")
    if harga < 0:
        raise ValueError("Harga tidak valid")

    return {
        "kode": kode_transaksi(no),
        "pelanggan": pelanggan.strip(),
        "produk": produk.strip(),
        "qty": qty,
        "harga": harga,
        "total": qty * harga,
    }


def simpan_json(data, path="transaksi.json"):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=2,
            ensure_ascii=False,
        )


def muat_json(path="transaksi.json"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("transaksi.json rusak.")
        return []


def cari_transaksi(data, kode):
    for item in data:
        if item["kode"] == kode:
            return item
    return None


def total_penjualan(data):
    return sum(item["total"] for item in data)


def format_transaksi(item):
    return (
        f"{item['kode']:<12}"
        f"{item['pelanggan']:<15}"
        f"{item['produk']:<15}"
        f"{item['qty']:>5}"
        f"{item['harga']:>12,.0f}"
        f"{item['total']:>15,.0f}"
    )


def tampilkan_transaksi(data):
    if not data:
        print("Belum ada transaksi.")
        return

    print(
        f"{'Kode':<12}"
        f"{'Pelanggan':<15}"
        f"{'Produk':<15}"
        f"{'Qty':>5}"
        f"{'Harga':>12}"
        f"{'Total':>15}"
    )
    print("-" * 74)

    for item in data:
        print(format_transaksi(item))


def buat_laporan(data, path="laporan.txt"):
    with open(path, "w", encoding="utf-8") as file:
        file.write("LAPORAN PENJUALAN\n")
        file.write("=" * 74 + "\n")
        file.write(
            f"{'Kode':<12}"
            f"{'Pelanggan':<15}"
            f"{'Produk':<15}"
            f"{'Qty':>5}"
            f"{'Harga':>12}"
            f"{'Total':>15}\n"
        )
        file.write("-" * 74 + "\n")

        for item in data:
            file.write(format_transaksi(item) + "\n")

        file.write("-" * 74 + "\n")
        file.write(
            f"Total Penjualan: Rp{total_penjualan(data):,.0f}\n"
        )


def menu():
    print("\n=== APLIKASI TRANSAKSI ===")
    print("1. Tambah transaksi")
    print("2. Lihat transaksi")
    print("3. Cari transaksi")
    print("4. Total penjualan")
    print("5. Export TXT")
    print("6. Keluar")


def input_transaksi(no):
    pelanggan = input("Pelanggan: ")
    produk = input("Produk: ")

    while True:
        try:
            qty = int(input("Qty: "))
            break
        except ValueError:
            print("Qty harus integer.")

    while True:
        try:
            harga = float(input("Harga: "))
            break
        except ValueError:
            print("Harga harus angka.")

    return buat_transaksi(
        no,
        pelanggan,
        produk,
        qty,
        harga,
    )


def main_transaksi():
    data = muat_json()

    while True:
        menu()
        pilihan = input("Pilih: ").strip()

        match pilihan:
            case "1":
                try:
                    transaksi = input_transaksi(len(data) + 1)
                    data.append(transaksi)
                    simpan_json(data)
                    print("Tersimpan:", transaksi["kode"])
                except ValueError as error:
                    print("Error:", error)

            case "2":
                tampilkan_transaksi(data)

            case "3":
                kode = input("Kode: ").strip()
                hasil = cari_transaksi(data, kode)
                print(format_transaksi(hasil) if hasil else "Tidak ditemukan")

            case "4":
                print(
                    "Total penjualan:",
                    f"Rp{total_penjualan(data):,.0f}",
                )

            case "5":
                buat_laporan(data)
                print("laporan.txt dibuat.")

            case "6":
                print("Program selesai.")
                break

            case _:
                print("Pilihan tidak valid.")


def main():
    print("Python 7.3 - Latihan dan Studi Kasus Terpadu")
    print("Aktifkan main_transaksi() untuk menjalankan mini project.")
    # main_transaksi()


if __name__ == "__main__":
    main()
