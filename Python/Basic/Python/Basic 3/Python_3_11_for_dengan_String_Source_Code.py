"""
Python 3.11 - for dengan String
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: CETAK SETIAP HURUF ===")
kata = "PYTHON"

for huruf in kata:
    print(huruf)

print("\n=== CONTOH 2: LABEL SETIAP HURUF ===")
kata = "CAT"

for huruf in kata:
    print("Huruf:", huruf)

print("\n=== CONTOH 3: HITUNG JUMLAH KARAKTER ===")
kata = "PYTHON"
jumlah = 0

for huruf in kata:
    jumlah = jumlah + 1

print("Jumlah karakter:", jumlah)

print("\n=== CONTOH 4: HITUNG HURUF A ===")
kata = "BANANA"
jumlah_a = 0

for huruf in kata:
    if huruf == "A":
        jumlah_a = jumlah_a + 1

print("Jumlah A:", jumlah_a)

print("\n=== CONTOH 5: TAMPILKAN VOKAL ===")
kata = "PYTHON"

for huruf in kata:
    if huruf in "AIUEO":
        print(huruf)

print("\n=== CONTOH 6: CASE-INSENSITIVE ===")
kata = "PyThOn"
jumlah_o = 0

for huruf in kata:
    if huruf.lower() == "o":
        jumlah_o = jumlah_o + 1

print("Jumlah o:", jumlah_o)

print("\n=== CONTOH 7: BUAT STRING BARU ===")
kata = "Python"
hasil = ""

for huruf in kata:
    hasil = hasil + huruf.upper()

print(hasil)

print("\n=== CONTOH 8: ABAIKAN SPASI ===")
kalimat = "Aku belajar Python"

for c in kalimat:
    if c != " ":
        print(c, end="")

print()

print("\n=== CONTOH 9: HITUNG DIGIT ===")
teks = "Order123A"
digit = 0

for c in teks:
    if c.isdigit():
        digit = digit + 1

print("Jumlah digit:", digit)

print("\n=== LATIHAN ===")
teks_latihan = "A1B2C3"
jumlah_digit = 0

for c in teks_latihan:
    if c.isdigit():
        jumlah_digit = jumlah_digit + 1

print("Jumlah digit latihan:", jumlah_digit)
