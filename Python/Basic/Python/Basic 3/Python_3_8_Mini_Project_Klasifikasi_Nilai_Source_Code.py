"""
Python 3.8 - Mini Project: Klasifikasi Nilai
Input nilai -> if/elif/else -> Grade A/B/C/D
"""

# ============================================================
# VERSI 1 - DASAR
# ============================================================

print("=== KLASIFIKASI NILAI - VERSI DASAR ===")

nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)


# ============================================================
# VERSI 2 - DENGAN VALIDASI 0 SAMPAI 100
# ============================================================

print("\n=== KLASIFIKASI NILAI - DENGAN VALIDASI ===")

nilai = int(input("Masukkan nilai 0-100: "))

if nilai < 0 or nilai > 100:
    print("Nilai harus antara 0 dan 100")
else:
    if nilai >= 90:
        grade = "A"
    elif nilai >= 80:
        grade = "B"
    elif nilai >= 70:
        grade = "C"
    else:
        grade = "D"

    print("Grade:", grade)


# ============================================================
# VERSI 3 - TEST CASE TANPA INPUT MANUAL
# ============================================================

print("\n=== TEST CASE ===")

daftar_nilai = [100, 95, 90, 89, 85, 80, 79, 75, 70, 69, 60]

for nilai in daftar_nilai:
    if nilai >= 90:
        grade = "A"
    elif nilai >= 80:
        grade = "B"
    elif nilai >= 70:
        grade = "C"
    else:
        grade = "D"

    print("Nilai:", nilai, "-> Grade:", grade)


# ============================================================
# LATIHAN
# Ubah aturan menjadi:
# 85-100 = A
# 75-84  = B
# 65-74  = C
# 0-64   = D
# ============================================================

print("\n=== LATIHAN MODIFIKASI ===")

nilai_latihan = 85

if nilai_latihan >= 85:
    grade_latihan = "A"
elif nilai_latihan >= 75:
    grade_latihan = "B"
elif nilai_latihan >= 65:
    grade_latihan = "C"
else:
    grade_latihan = "D"

print("Nilai latihan:", nilai_latihan)
print("Grade latihan:", grade_latihan)
