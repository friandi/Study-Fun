"""
Python 3.27 - Perkenalan match
Pattern matching: mirip switch secara permukaan, tetapi lebih kuat.
Butuh Python 3.10 atau lebih baru.
"""

print("=== CONTOH 1: STRING LITERAL ===")
command = "start"

match command:
    case "start":
        print("Mulai")
    case "stop":
        print("Berhenti")
    case _:
        print("Perintah tidak dikenal")

print("\n=== CONTOH 2: INTEGER LITERAL ===")
hari = 2

match hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case _:
        print("Hari lain")

print("\n=== CONTOH 3: OR PATTERN ===")
hari = 6

match hari:
    case 6 | 7:
        print("Weekend")
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case _:
        print("Nilai tidak valid")

print("\n=== CONTOH 4: COMMAND ALIAS ===")
cmd = "quit"

match cmd:
    case "quit" | "exit":
        print("Keluar")
    case "help":
        print("Bantuan")
    case _:
        print("Tidak dikenal")

print("\n=== CONTOH 5: SEQUENCE PATTERN ===")
titik = [10, 20]

match titik:
    case [x, y]:
        print("x =", x)
        print("y =", y)
    case _:
        print("Bukan pasangan dua nilai")

print("\n=== CONTOH 6: GUARD ===")
nilai = 85

match nilai:
    case n if n >= 90:
        print("A")
    case n if n >= 80:
        print("B")
    case _:
        print("C")

print("\n=== PERBANDINGAN DENGAN IF/ELIF/ELSE ===")
status = "ok"

if status == "ok":
    print("Berhasil")
elif status == "error":
    print("Gagal")
else:
    print("Tidak dikenal")

match status:
    case "ok":
        print("Berhasil")
    case "error":
        print("Gagal")
    case _:
        print("Tidak dikenal")

# Catatan penting:
# case _ adalah wildcard/default.
# case pertama yang cocok akan dipilih.
# match/case tersedia mulai Python 3.10.
