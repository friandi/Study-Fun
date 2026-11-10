"""
Python 3.31 - Defining Functions / Membuat Fungsi
Materi lengkap untuk pemula.
"""

# =========================================================
# 1. APA ITU FUNCTION?
# =========================================================
def sapa():
    print("Halo")

sapa()


# =========================================================
# 2. MENGAPA FUNCTION DIPERLUKAN?
# =========================================================
def sapa_nama(nama):
    print("Halo", nama)
    print("Selamat belajar")

sapa_nama("Andy")
sapa_nama("Budi")
sapa_nama("Cici")


# =========================================================
# 3. MEMBUAT FUNCTION DENGAN def
# =========================================================
def tampilkan_judul():
    print("=== BELAJAR PYTHON ===")

tampilkan_judul()


# =========================================================
# 4. MEMANGGIL FUNCTION
# =========================================================
for _ in range(3):
    tampilkan_judul()


# =========================================================
# 5. PARAMETER DAN ARGUMENT
# =========================================================
def biodata(nama, umur):
    print("Nama:", nama)
    print("Umur:", umur)

biodata("Andy", 47)
biodata(umur=47, nama="Andy")


# =========================================================
# 6. RETURN
# =========================================================
def tambah(a, b):
    return a + b

hasil = tambah(3, 5)
print("3 + 5 =", hasil)

def luas(panjang, lebar):
    return panjang * lebar

hasil_luas = luas(5, 4)
print("Luas =", hasil_luas)


# =========================================================
# 7. FUNCTION TANPA RETURN DAN None
# =========================================================
def tampilkan_pesan():
    print("Pesan ditampilkan")

hasil = tampilkan_pesan()
print("Nilai return:", hasil)  # None


# =========================================================
# 8. VARIABLE LOKAL DAN GLOBAL
# =========================================================
nama_global = "Andy"

def contoh_scope():
    nama_lokal = "Budi"
    print("Global dari dalam function:", nama_global)
    print("Lokal:", nama_lokal)

contoh_scope()
print("Global dari luar:", nama_global)

# Jangan aktifkan baris ini karena nama_lokal tidak ada di luar function:
# print(nama_lokal)


# =========================================================
# 9. DOCSTRING
# =========================================================
def kali(a, b):
    """
    Mengalikan dua angka.

    a: angka pertama
    b: angka kedua
    return: hasil perkalian
    """
    return a * b

print(kali(4, 5))
print(kali.__doc__)


# =========================================================
# 10. FIBONACCI - MENAMPILKAN
# =========================================================
def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        print(a)
        a, b = b, a + b

print("Fibonacci 7 angka:")
fibonacci(7)


# =========================================================
# 10B. FIBONACCI RECURSIVE - PENGENALAN
# =========================================================
def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)

print("fib(6) =", fib(6))


# =========================================================
# 11. FUNCTION MENGHASILKAN LIST
# =========================================================
def buat_kuadrat(angka_list):
    hasil = []

    for n in angka_list:
        hasil.append(n * n)

    return hasil

print(buat_kuadrat([1, 2, 3, 4]))


def ambil_genap(data):
    hasil = []

    for n in data:
        if n % 2 == 0:
            hasil.append(n)

    return hasil

print(ambil_genap([1, 2, 3, 4, 5, 6]))


def fibonacci_list(n):
    hasil = []
    a, b = 0, 1

    for _ in range(n):
        hasil.append(a)
        a, b = b, a + b

    return hasil

print(fibonacci_list(8))


# =========================================================
# 12. LATIHAN - CONTOH JAWABAN
# =========================================================

# Latihan 1
def tampilkan_judul_latihan():
    print("=== BELAJAR PYTHON ===")

tampilkan_judul_latihan()
tampilkan_judul_latihan()
tampilkan_judul_latihan()


# Latihan 2
def sapa_kota(nama, kota):
    print("Halo", nama, "dari", kota)

sapa_kota("Andy", "Jakarta")
sapa_kota("Budi", "Bandung")
sapa_kota("Cici", "Surabaya")


# Latihan 3
def hitung_diskon(harga, persen):
    potongan = harga * persen / 100
    return harga - potongan

print("Harga setelah diskon:", hitung_diskon(100000, 10))


# Latihan 4
def cek():
    print("Sedang mengecek...")
    return "OK"

hasil = cek()
print("hasil =", hasil)


# Latihan 5
x = 10

def contoh_local():
    x = 20
    print("dalam =", x)

contoh_local()
print("luar =", x)


# Latihan 6
def kali_dua(data):
    hasil = []

    for n in data:
        hasil.append(n * 2)

    return hasil

print(kali_dua([1, 2, 3]))


# Latihan 7
print(fibonacci_list(8))


# Latihan 8 - Kalkulator sederhana
def tambah_kalkulator(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali_kalkulator(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: tidak bisa dibagi 0"

    return a / b

print(tambah_kalkulator(10, 2))
print(kurang(10, 2))
print(kali_kalkulator(10, 2))
print(bagi(10, 2))
print(bagi(10, 0))
