"""
Python 3.33 - Coding Style
Contoh before/after dan latihan merapikan kode.
"""

# =========================================================
# 1. INDENTATION
# =========================================================
def cek_nilai(nilai):
    if nilai >= 80:
        print("Bagus")
    else:
        print("Belajar lagi")


# =========================================================
# 2. NAMING
# =========================================================
nama_user = "Andy"
total_harga = 50_000

def hitung_diskon(harga, persen=10):
    """Hitung harga setelah diskon."""
    return harga - harga * persen / 100


# =========================================================
# 3. SPACING
# =========================================================
harga = 25_000
jumlah = 3
ongkir = 10_000

total = harga * jumlah + ongkir

if total > 100_000:
    diskon = total * 0.10
else:
    diskon = 0


# =========================================================
# 4. LONG CONDITION
# =========================================================
user_aktif = True
status_verifikasi = "VALID"
saldo = 1_000_000
minimum_saldo = 100_000
bukan_blacklist = True
limit_tersedia = 500_000

if (
    user_aktif
    and status_verifikasi == "VALID"
    and saldo > minimum_saldo
    and bukan_blacklist
    and limit_tersedia > 0
):
    print("Transaksi dapat diproses")


# =========================================================
# 5. COMMENT YANG BAIK
# =========================================================
MAX_RETRY = 3
retry = 2

# Batasi percobaan agar login gagal tidak dicoba tanpa batas.
retry += 1

if retry > MAX_RETRY:
    print("Akun diblokir sementara")


# =========================================================
# 6. DOCSTRING
# =========================================================
def konversi_celsius(fahrenheit):
    """
    Konversi Fahrenheit menjadi Celsius.

    Args:
        fahrenheit: Suhu dalam Fahrenheit.

    Returns:
        Nilai suhu dalam Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


# =========================================================
# 7. BEFORE
# =========================================================
# Contoh berikut sengaja berantakan.
#
# def HitungTotal(Nama,Barang):
#  total=0
#  for i in Barang:total+=i
#  if total>100000:diskon=total*0.1
#  else:diskon=0
#  print('Total',Nama,':',total-diskon)


# =========================================================
# 8. AFTER
# =========================================================
def hitung_total(nama, barang):
    """Hitung total belanja setelah diskon."""
    total = sum(barang)

    if total > 100_000:
        diskon = total * 0.10
    else:
        diskon = 0

    total_bayar = total - diskon
    print(f"Total {nama}: {total_bayar}")

daftar_harga = [50_000, 30_000, 40_000]
hitung_total("Budi", daftar_harga)


# =========================================================
# LATIHAN 1 - SPACING
# =========================================================
a = 10
b = 20
c = a + b * 2

if c > 30:
    print(c)


# =========================================================
# LATIHAN 2 - NAMING
# =========================================================
nama = "Andy"
umur = 47
kota = "Jakarta"

def tampilkan_profil(nama, umur, kota):
    print(nama, umur, kota)

tampilkan_profil(nama, umur, kota)


# =========================================================
# LATIHAN 3 - INDENTATION
# =========================================================
def cek_grade(nilai):
    if nilai >= 80:
        print("A")
    elif nilai >= 70:
        print("B")
    else:
        print("C")


# =========================================================
# LATIHAN 4 - DOCSTRING
# =========================================================
def kuadrat(n):
    """Mengembalikan kuadrat dari n."""
    return n * n
