"""
Python 5.7 - More on Conditions
Kondisi Lanjutan.
"""

print("=== 5.7.1 TRUE / FALSE ===")
print(5 > 3)
print(10 == 8)
print(bool(0), bool(""), bool([]))
print(bool(10), bool("Halo"), bool([1]))

print("\n=== 5.7.2 in / not in ===")
print(3 in [1, 2, 3])
print("py" in "python")
allowed = {"admin", "user"}
role = "guest"
print(role not in allowed)

print("\n=== 5.7.3 is / is not ===")
a = [1, 2]
b = a
c = [1, 2]
print(a is b)
print(a is c)
hasil = None
print(hasil is None)

print("\n=== 5.7.4 == vs is ===")
a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)

print("\n=== 5.7.5 CHAINED COMPARISON ===")
umur = 25
print(18 <= umur <= 60)

print("\n=== 5.7.6-8 and / or / not ===")
punya_ktp = True
print(umur >= 17 and punya_ktp)
hari = "Minggu"
print(hari == "Sabtu" or hari == "Minggu")
aktif = False
print(not aktif)

print("\n=== 5.7.9 PRECEDENCE ===")
print(not False and True or False)

print("\n=== 5.7.10 SHORT-CIRCUIT ===")
data = []
if data and data[0] > 10:
    print("Besar")
else:
    print("Aman: data kosong")

nama = "Andy"
hasil = nama or input("Nama: ")
print(hasil)

print("\n=== 5.7.11 and/or RETURN OPERAND ===")
nama = ""
print(nama or "Guest")
login = True
print(login and "Masuk")
login = False
print(login and "Masuk")

print("\n=== 5.7.12 WALRUS ===")
data = [10, 20, 30]
if (n := len(data)) > 2:
    print("Jumlah data:", n)

# Interaktif:
# while (teks := input("Ketik (kosong untuk berhenti): ")):
#     print("Anda mengetik:", teks)

print("\n=== 5.7.13 STUDI KASUS ===")
user = {
    "username": "andy",
    "aktif": True,
    "role": "admin",
}
allowed_roles = {"admin", "manager"}

if user.get("aktif") and user.get("role") in allowed_roles:
    print("Akses diberikan")
else:
    print("Akses ditolak")

umur = 25
aktif = True
blacklist = False
boleh = 18 <= umur <= 60 and aktif and not blacklist
print("Boleh:", boleh)

print("\n=== LATIHAN ===")
a = [1, 2]
b = [1, 2]
c = a
print(a == b)
print(a is b)
print(a is c)

nilai = 85
if 0 <= nilai <= 100:
    print("Nilai valid")

data = []
if data and data[0] == 10:
    print("Elemen pertama 10")

nickname = ""
print(nickname or "Anonymous")

data = [1, 2, 3, 4, 5, 6]
if (jumlah_data := len(data)) > 5:
    print("Jumlah data:", jumlah_data)
