"""
Python 3.28 - match case sederhana
Contoh praktis: status HTTP dan pilihan menu.
Butuh Python 3.10 atau lebih baru.
"""

print("=== CONTOH 1: STATUS HTTP ===")
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Status lain")


print("\n=== CONTOH 2: STATUS HTTP DARI INPUT ===")
# Aktifkan jika ingin mencoba input manual.
# status = int(input("Masukkan status code: "))
#
# match status:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case 500:
#         print("Server Error")
#     case _:
#         print("Unknown")


print("\n=== CONTOH 3: MENU ANGKA ===")
pilihan = 2

match pilihan:
    case 1:
        print("Tambah Data")
    case 2:
        print("Lihat Data")
    case 3:
        print("Keluar")
    case _:
        print("Pilihan tidak valid")


print("\n=== CONTOH 4: MENU STRING ===")
pilihan_teks = "lihat"

match pilihan_teks:
    case "tambah":
        print("Tambah Data")
    case "lihat":
        print("Lihat Data")
    case "keluar":
        print("Keluar")
    case _:
        print("Perintah tidak dikenal")


print("\n=== CONTOH 5: BEBERAPA ALIAS DENGAN | ===")
command = "exit"

match command:
    case "keluar" | "exit" | "quit":
        print("Program ditutup")
    case "help":
        print("Bantuan")
    case _:
        print("Perintah lain")


print("\n=== CATATAN TIPE DATA ===")
status_text = "200"

match status_text:
    case 200:
        print("OK")
    case _:
        print('String "200" tidak sama dengan Integer 200')


print("\n=== LATIHAN HTTP ===")
status = 500

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown")


print("\n=== LATIHAN MENU ===")
pilihan = 9

match pilihan:
    case 1:
        print("Tambah")
    case 2:
        print("Lihat")
    case 3:
        print("Keluar")
    case _:
        print("Tidak valid")
