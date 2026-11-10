"""
Python 5.1 - More on Lists
Contoh utama dari 28 submateri.
"""

from collections import deque

# 5.1.1 - Apa itu List?
nama = ["Andy", "Budi", "Cici"]
angka = [10, 20, 30]
campur = ["Andy", 47, True]
print(nama, angka, campur)

# 5.1.2 - Mengapa List?
nilai = [80, 90, 75]
print("Rata-rata:", sum(nilai) / len(nilai))

# 5.1.3 - Membuat List
kosong = []
nested = [[1, 2], [3, 4]]
print(kosong, nested)

# 5.1.4 - Index
print(nama[0])
print(nama[-1])

# 5.1.5 - Mengubah isi
data = ["A", "B", "C"]
data[1] = "BARU"
print(data)

# 5.1.6 - append
data.append("D")
print(data)

# 5.1.7 - extend
data.extend(["E", "F"])
print(data)

# 5.1.8 - insert
data.insert(1, "X")
print(data)

# 5.1.9 - remove
data.remove("X")
print(data)

# 5.1.10 - pop
item = data.pop()
print("pop:", item, data)

# 5.1.11 - clear
tmp = [1, 2, 3]
tmp.clear()
print(tmp)

# 5.1.12 - index
print(nama.index("Budi"))

# 5.1.13 - count
nilai = [80, 90, 80, 70, 80]
print(nilai.count(80))

# 5.1.14 - sort
angka = [30, 10, 20]
angka.sort()
print(angka)
angka.sort(reverse=True)
print(angka)

# 5.1.15 - reverse
angka.reverse()
print(angka)

# 5.1.16 - copy
asli = [1, 2, 3]
salinan = asli.copy()
salinan.append(4)
print(asli, salinan)

# 5.1.17 - None pada method List
x = [2, 1]
y = x.sort()
print("x =", x)
print("y =", y)

# 5.1.18 - Stack
stack = []
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack pop:", stack.pop())

# 5.1.19 - Queue dengan List
queue = []
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue pop(0):", queue.pop(0))

# 5.1.20 - deque
q = deque(["A", "B"])
q.append("C")
print("Deque popleft:", q.popleft())

# 5.1.21 - Pengenalan List Comprehension
kuadrat = [x * x for x in range(5)]
print(kuadrat)

# 5.1.22 - List Comprehension dengan for
dua_kali = [x * 2 for x in range(5)]
print(dua_kali)

# 5.1.23 - List Comprehension dengan if
genap = [x for x in range(1, 11) if x % 2 == 0]
print(genap)

# 5.1.24 - Nested List Comprehension
pasangan = [(x, y) for x in [1, 2] for y in ["A", "B"]]
print(pasangan)

# 5.1.25 - Matrix dan transpose
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)

# 5.1.26 - Unpacking menggunakan *
data = [10, 20, 30, 40, 50]
pertama, *tengah, terakhir = data
print(pertama, tengah, terakhir)

# 5.1.27 - Unpacking dalam List Comprehension
data_orang = [("Andy", 47), ("Budi", 30)]
label = [f"{nama}:{umur}" for nama, umur in data_orang]
print(label)

# 5.1.28 - Studi kasus pelanggan
pelanggan = ["Andi", "Budi", "Cici"]
pelanggan.append("Deni")
pelanggan.insert(1, "Eka")

if "Budi" in pelanggan:
    pelanggan.remove("Budi")

pelanggan.sort()
backup = pelanggan.copy()

print("Daftar pelanggan:", pelanggan)
print("Jumlah pelanggan:", len(pelanggan))
print("Backup:", backup)
