"""
Python 3.17 - range() + len() untuk index List
Materi latihan untuk pemula.
"""

print("=== CONTOH 1: INDEX + ITEM ===")
nama = ["Ani", "Budi", "Cici"]

for i in range(len(nama)):
    print("Index", i, "=", nama[i])

print("\n=== CONTOH 2: LIST HARGA ===")
harga = [10000, 20000, 15000]

for i in range(len(harga)):
    print("Item", i, "harga", harga[i])

print("\n=== CONTOH 3: UBAH ISI LIST LEWAT INDEX ===")
angka = [1, 2, 3]

for i in range(len(angka)):
    angka[i] = angka[i] * 10

print(angka)

print("\n=== CONTOH 4: DUA LIST DENGAN INDEX SAMA ===")
nama = ["Ani", "Budi", "Cici"]
nilai = [80, 90, 75]

for i in range(len(nama)):
    print(nama[i], nilai[i])

print("\n=== CONTOH 5: INDEX TERAKHIR ===")
data = ["A", "B", "C"]

print("Jumlah item:", len(data))
print("Index terakhir:", len(data) - 1)
print("Item terakhir:", data[len(data) - 1])

print("\n=== CONTOH 6: LIST KOSONG ===")
data_kosong = []

for i in range(len(data_kosong)):
    print(data_kosong[i])

print("Loop selesai")

print("\n=== CONTOH 7: INDEX DALAM KONDISI ===")
nama = ["Ani", "Budi", "Cici", "Dedi"]

for i in range(len(nama)):
    if i % 2 == 0:
        print(i, nama[i])

print("\n=== LATIHAN ===")
data = ["X", "Y", "Z"]

for i in range(len(data)):
    print("Posisi", i, "berisi", data[i])

# Contoh yang menghasilkan IndexError:
# print(data[len(data)])
# karena len(data) = 3, sedangkan index valid hanya 0,1,2.
