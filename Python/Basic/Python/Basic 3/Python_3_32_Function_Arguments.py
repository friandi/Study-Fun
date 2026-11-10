"""
Python 3.32 - Function Arguments & Advanced Function Basics
Materi: default, keyword, special parameters, *args, **kwargs,
unpacking, lambda, docstring, annotations.
"""

# =========================================================
# 1. DEFAULT ARGUMENT VALUES
# =========================================================
def sapa(nama="Teman"):
    print("Halo", nama)

sapa()
sapa("Andy")


def pesan(nama, salam="Halo", tanda="!"):
    print(salam, nama + tanda)

pesan("Andy")
pesan("Andy", "Selamat pagi")
pesan("Andy", "Hai", "!!!")


def hitung_pajak(harga, persen=11):
    return harga + (harga * persen / 100)

print(hitung_pajak(100000))
print(hitung_pajak(100000, 12))


# =========================================================
# 2. KEYWORD ARGUMENTS
# =========================================================
def biodata(nama, umur, kota):
    print(nama, umur, kota)

biodata("Andy", 47, "Jakarta")
biodata(kota="Jakarta", nama="Andy", umur=47)


def buat_profil(nama, umur, kota="Jakarta"):
    return f"{nama}, {umur}, {kota}"

print(buat_profil(umur=47, nama="Andy"))
print(buat_profil(kota="Bandung", nama="Budi", umur=30))


# =========================================================
# 3. SPECIAL PARAMETERS
# =========================================================
def bagi(a, b, /):
    return a / b

print(bagi(10, 2))


def koneksi(host, *, timeout=30):
    print("host =", host)
    print("timeout =", timeout)

koneksi("server1", timeout=10)


def contoh(a, b, /, c, *, d):
    print(a, b, c, d)

contoh(1, 2, 3, d=4)
contoh(1, 2, c=3, d=4)


def kirim_email(alamat, /, *, subject="Info"):
    print("To:", alamat)
    print("Subject:", subject)

kirim_email("user@example.com", subject="Laporan")


# =========================================================
# 4. *args DAN **kwargs
# =========================================================
def jumlahkan(*args):
    total = 0

    for n in args:
        total += n

    return total

print(jumlahkan())
print(jumlahkan(1))
print(jumlahkan(1, 2, 3, 4))


def profil(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

profil(nama="Andy", umur=47, kota="Jakarta")


def gabungan(nama, *args, **kwargs):
    print("nama =", nama)
    print("args =", args)
    print("kwargs =", kwargs)

gabungan("Andy", 10, 20, kota="Jakarta")


def rata_rata(*angka):
    if len(angka) == 0:
        return 0

    return sum(angka) / len(angka)

print(rata_rata(80, 90, 85))


# =========================================================
# 5. UNPACKING ARGUMENT LISTS
# =========================================================
def tambah3(a, b, c):
    return a + b + c

angka = [10, 20, 30]
print(tambah3(*angka))


def tampil_biodata(nama, umur, kota):
    print(nama, umur, kota)

data = {
    "nama": "Andy",
    "umur": 47,
    "kota": "Jakarta",
}

tampil_biodata(**data)


def luas(panjang, lebar):
    return panjang * lebar

ukuran = [5, 4]
print(luas(*ukuran))


# =========================================================
# 6. LAMBDA EXPRESSIONS
# =========================================================
kuadrat = lambda x: x * x
print(kuadrat(5))

tambah_lambda = lambda a, b: a + b
print(tambah_lambda(3, 5))

kali10 = lambda x: x * 10
print(kali10(7))

maks = lambda a, b: a if a > b else b
print(maks(10, 7))

produk = [
    ("Mouse", 150000),
    ("Keyboard", 300000),
    ("Monitor", 2000000),
]

produk_urut = sorted(produk, key=lambda item: item[1])
print(produk_urut)


# =========================================================
# 7. DOCSTRING
# =========================================================
def hitung_bmi(berat, tinggi):
    """
    Menghitung Body Mass Index.

    berat: berat badan dalam kilogram
    tinggi: tinggi badan dalam meter
    return: nilai BMI
    """
    return berat / (tinggi ** 2)

print(hitung_bmi(70, 1.75))
print(hitung_bmi.__doc__)


def hitung_diskon(harga, persen=10):
    """
    Menghitung harga setelah diskon.

    harga: harga awal
    persen: persentase diskon, default 10
    return: harga setelah diskon
    """
    return harga - (harga * persen / 100)

print(hitung_diskon(100000))


# =========================================================
# 8. FUNCTION ANNOTATIONS
# =========================================================
def tambah_annotation(a: int, b: int) -> int:
    return a + b

print(tambah_annotation(3, 5))
print(tambah_annotation.__annotations__)


def total(data: list[int]) -> int:
    hasil = 0

    for n in data:
        hasil += n

    return hasil

print(total([1, 2, 3]))


def hitung_luas(panjang: float, lebar: float) -> float:
    return panjang * lebar

print(hitung_luas(5.0, 4.0))


# =========================================================
# LATIHAN BESAR 1
# =========================================================
def laporan(nama, *nilai, status="Aktif", **info):
    rata = sum(nilai) / len(nilai) if nilai else 0

    return {
        "nama": nama,
        "rata_rata": rata,
        "status": status,
        "kota": info.get("kota", "-"),
    }

print(
    laporan(
        "Andy",
        80,
        90,
        85,
        status="Aktif",
        kota="Jakarta",
    )
)


# =========================================================
# LATIHAN BESAR 2
# =========================================================
angka = [10, 20, 30]
print(tambah3(*angka))

profil_data = {"nama": "Andy", "kota": "Jakarta"}

def tampil_profil(nama, kota):
    print(nama, kota)

tampil_profil(**profil_data)


# =========================================================
# LATIHAN BESAR 3
# =========================================================
produk = [
    ("Mouse", 150000),
    ("Keyboard", 300000),
    ("Monitor", 2000000),
]

hasil = sorted(produk, key=lambda item: item[1])
print(hasil)
