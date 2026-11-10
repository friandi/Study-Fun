"""
Python 3.29 - _ sebagai default / wildcard
Analogi else untuk pola yang tidak cocok.
Butuh Python 3.10 atau lebih baru.
"""

print("=== CONTOH 1: MENU ===")
pilihan = 9

match pilihan:
    case 1:
        print("Tambah Data")
    case 2:
        print("Lihat Data")
    case 3:
        print("Keluar")
    case _:
        print("Pilihan tidak valid")


print("\n=== CONTOH 2: STATUS HTTP ===")
status = 418

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Status lain")


print("\n=== CONTOH 3: COMMAND STRING ===")
cmd = "pause"

match cmd:
    case "start":
        print("Mulai")
    case "stop":
        print("Berhenti")
    case _:
        print("Command tidak dikenal")


print("\n=== CONTOH 4: OR PATTERN + DEFAULT ===")
cmd = "help"

match cmd:
    case "quit" | "exit":
        print("Keluar")
    case "start" | "run":
        print("Mulai")
    case _:
        print("Command lain")


print("\n=== CONTOH 5: CASE _ VS CASE x ===")
nilai = 99

match nilai:
    case _:
        print("Wildcard: nilainya tidak dipakai")

nilai = 99

match nilai:
    case x:
        print("Capture pattern, x =", x)


print("\n=== CONTOH 6: TANPA DEFAULT ===")
nilai = 9

match nilai:
    case 1:
        print("Satu")
    case 2:
        print("Dua")

print("Program tetap lanjut")


print("\n=== LATIHAN ===")
nilai = 5

match nilai:
    case 1:
        print("A")
    case 2:
        print("B")
    case _:
        print("C")
