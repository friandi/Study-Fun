"""
Python 3.6 - Urutan Pengecekan if / elif / else
Fokus: Python membaca dari atas ke bawah dan berhenti pada True pertama.
"""

print("=== CONTOH 1: NILAI 95 ===")
nilai = 95
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
else:
    print("C")

print("\n=== CONTOH 2: NILAI 85 ===")
nilai = 85
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
else:
    print("C")

print("\n=== CONTOH 3: NILAI 60 ===")
nilai = 60
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
else:
    print("C")

print("\n=== CONTOH 4: URUTAN YANG SALAH ===")
nilai = 95
if nilai >= 70:
    print("C")
elif nilai >= 80:
    print("B")
elif nilai >= 90:
    print("A")

print("\n=== CONTOH 5: URUTAN YANG BENAR ===")
nilai = 95
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")
else:
    print("D")

print("\n=== CONTOH 6: DISKON BERTINGKAT ===")
belanja = 600000
if belanja >= 500000:
    print("Diskon 20%")
elif belanja >= 200000:
    print("Diskon 10%")
elif belanja >= 100000:
    print("Diskon 5%")
else:
    print("Tidak ada diskon")

print("\n=== CONTOH 7: DUA IF TERPISAH ===")
x = 10
if x > 0:
    print("Positif")
if x > 5:
    print("Lebih dari 5")

print("\n=== LATIHAN ===")
x = 7
if x > 0:
    print("A")
elif x > 5:
    print("B")
elif x > 3:
    print("C")
else:
    print("D")
