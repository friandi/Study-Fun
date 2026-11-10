"""
Python 3.22 - continue
Melewati satu iteration dan melanjutkan loop.
"""

print("=== CONTOH 1: LEWATI ANGKA 3 ===")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n=== CONTOH 2: LEWATI JERUK ===")
buah = ["Apel", "Jeruk", "Mangga"]

for item in buah:
    if item == "Jeruk":
        continue
    print(item)

print("\n=== CONTOH 3: LEWATI ANGKA GENAP ===")
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print(i)

print("\n=== CONTOH 4: LEWATI SPASI ===")
teks = "A B C"

for c in teks:
    if c == " ":
        continue
    print(c)

print("\n=== CONTOH 5: CONTINUE VS BREAK ===")
print("continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("break:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("\n=== CONTOH 6: WHILE + CONTINUE ===")
i = 0
while i < 3:
    i += 1
    if i == 2:
        continue
    print(i)

print("\n=== CONTOH 7: NESTED LOOP ===")
for i in range(2):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)

print("\n=== LATIHAN 1 ===")
for i in range(5):
    if i == 2:
        continue
    print(i)

print("\n=== LATIHAN 2: LEWATI ANGKA 5 ===")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# HATI-HATI:
# i = 0
# while i < 3:
#     if i == 1:
#         continue
#     print(i)
#     i += 1
#
# Kode di atas infinite loop karena saat i == 1,
# continue dijalankan sebelum i berubah.
