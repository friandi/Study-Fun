"""
Python 3.30 - Mini Project Menu Sederhana dengan match
Butuh Python 3.10 atau lebih baru.
"""

print("=== VERSI 1: MENU SATU KALI ===")
print("=== MENU DATA ===")
print("1. Tambah Data")
print("2. Lihat Data")
print("3. Keluar")

pilihan = input("Pilih menu (1/2/3): ")

match pilihan:
    case "1":
        print("Tambah Data")
    case "2":
        print("Lihat Data")
    case "3":
        print("Keluar")
    case _:
        print("Pilihan tidak valid")


print("\n=== VERSI 2: MENU BERULANG ===")
while True:
    print("\n=== MENU DATA ===")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    match pilihan:
        case "1":
            print("Tambah Data")
        case "2":
            print("Lihat Data")
        case "3":
            print("Keluar dari program")
            break
        case _:
            print("Pilihan tidak valid")


print("\n=== VERSI 3: MINI PROJECT FINAL ===")
data = []

while True:
    print("\n=== MENU DATA ===")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Keluar")

    pilihan = input("Pilih: ")

    match pilihan:
        case "1":
            nama = input("Masukkan nama: ")
            data.append(nama)
            print("Data ditambahkan")

        case "2":
            if len(data) == 0:
                print("Belum ada data")
            else:
                print("Isi data:")
                for item in data:
                    print("-", item)

        case "3":
            print("Program selesai")
            break

        case _:
            print("Pilihan tidak valid")
