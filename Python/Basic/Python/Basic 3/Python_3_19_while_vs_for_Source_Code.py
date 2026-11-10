"""
Python 3.19 - while vs for
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: FOR 0-4 ===")
for i in range(5):
    print(i)

print("\n=== CONTOH 2: WHILE 0-4 ===")
i = 0
while i < 5:
    print(i)
    i += 1

print("\n=== CONTOH 3: FOR PADA LIST ===")
nama = ["Ani", "Budi", "Cici"]
for orang in nama:
    print("Halo", orang)

print("\n=== CONTOH 4: WHILE DENGAN KONDISI ===")
i = 1
while i <= 5:
    print(i)
    i += 1

print("\n=== CONTOH 5: VALIDASI INPUT ===")
nilai = -1
while nilai < 0 or nilai > 100:
    nilai = int(input("Masukkan nilai 0-100: "))
print("Nilai valid:", nilai)

print("\n=== CONTOH 6: PASSWORD ===")
password = ""
while password != "rahasia":
    password = input("Password: ")
print("Login berhasil")

print("\n=== CONTOH 7: FOR + IF ===")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print("\n=== CONTOH 8: WHILE + IF ===")
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

print("\n=== CONTOH 9: COUNTDOWN DENGAN WHILE ===")
i = 5
while i > 0:
    print(i)
    i -= 1
print("Mulai!")

print("\n=== CONTOH 10: COUNTDOWN DENGAN FOR ===")
for i in range(5, 0, -1):
    print(i)
print("Mulai!")

print("\n=== LATIHAN: UBAH WHILE MENJADI FOR ===")
i = 1
while i <= 5:
    print(i * 10)
    i += 1

print("Versi for:")
for i in range(1, 6):
    print(i * 10)

# HATI-HATI INFINITE LOOP:
# i = 0
# while i < 5:
#     print(i)
#     # lupa i += 1
