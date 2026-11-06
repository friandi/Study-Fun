"""
Python 3.5 - if ... elif ... else
Lebih dari dua pilihan.
"""

print("=== CONTOH 1: GRADE NILAI ===")
nilai = 85
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")

print("\n=== CONTOH 2: KATEGORI UMUR ===")
umur = 17
if umur < 13:
    print("Anak-anak")
elif umur <= 17:
    print("Remaja")
else:
    print("Dewasa")

print("\n=== CONTOH 3: KATEGORI SUHU ===")
suhu = 32
if suhu < 20:
    print("Dingin")
elif suhu <= 30:
    print("Sejuk")
else:
    print("Panas")

print("\n=== CONTOH 4: DISKON ===")
belanja = 250000
if belanja >= 500000:
    print("Diskon 20%")
elif belanja >= 200000:
    print("Diskon 10%")
elif belanja >= 100000:
    print("Diskon 5%")
else:
    print("Tidak ada diskon")

print("\n=== CONTOH 5: STATUS PESANAN ===")
status = "dikirim"
if status == "baru":
    print("Pesanan baru")
elif status == "diproses":
    print("Sedang diproses")
elif status == "dikirim":
    print("Dalam pengiriman")
else:
    print("Status lain")

print("\n=== CONTOH 6: MENU ===")
pilihan = 2
if pilihan == 1:
    print("Tambah data")
elif pilihan == 2:
    print("Lihat data")
elif pilihan == 3:
    print("Hapus data")
else:
    print("Pilihan tidak dikenal")

print("\n=== CONTOH 7: TRUE PERTAMA MENANG ===")
x = 10
if x > 0:
    print("Positif")
elif x > 5:
    print("Lebih dari 5")
else:
    print("Lainnya")

print("\n=== LATIHAN ===")
nilai_latihan = 95
if nilai_latihan >= 90:
    print("Grade A")
elif nilai_latihan >= 80:
    print("Grade B")
elif nilai_latihan >= 70:
    print("Grade C")
else:
    print("Grade D")
