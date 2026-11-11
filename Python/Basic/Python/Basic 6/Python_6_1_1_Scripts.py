
# Python 6.1.1 - Executing Modules as Scripts
# Menjalankan Modul sebagai Program.
#
# File ini berisi beberapa TEMPLATE contoh.
# Salin bagian yang diperlukan menjadi file .py terpisah.

CEK_NAMA_PY = r'''
print("__name__ =", __name__)
'''

MODULE_GUARD_PY = r'''
def sapa(nama):
    return f"Halo {nama}"

def main():
    print("Demo langsung")
    print(sapa("Andy"))

if __name__ == "__main__":
    main()
'''

LIHAT_ARG_PY = r'''
import sys

print("sys.argv =", sys.argv)

for index, value in enumerate(sys.argv):
    print(index, value)
'''

SALAM_PY = r'''
import sys

def sapa(nama):
    return f"Halo {nama}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python salam.py NAMA")
        raise SystemExit(1)

    nama = sys.argv[1]
    print(sapa(nama))

if __name__ == "__main__":
    main()
'''

TAMBAH_PY = r'''
import sys

def tambah(a, b):
    return a + b

def main():
    if len(sys.argv) != 3:
        print("Usage: python tambah.py A B")
        raise SystemExit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        print("A dan B harus berupa bilangan bulat")
        raise SystemExit(1)

    print(tambah(a, b))

if __name__ == "__main__":
    main()
'''

SUHU_PY = r'''
import sys

def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def main():
    if len(sys.argv) != 2:
        print("Usage: python suhu.py CELSIUS")
        raise SystemExit(1)

    try:
        celsius = float(sys.argv[1])
    except ValueError:
        print("CELSIUS harus berupa angka")
        raise SystemExit(1)

    print(c_to_f(celsius))

if __name__ == "__main__":
    main()
'''

KALKULATOR_PY = r'''
import sys

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan 0")
    return a / b

def hitung(operasi, a, b):
    if operasi == "tambah":
        return tambah(a, b)
    if operasi == "kurang":
        return kurang(a, b)
    if operasi == "kali":
        return kali(a, b)
    if operasi == "bagi":
        return bagi(a, b)

    raise ValueError(f"Operasi tidak dikenal: {operasi}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python kalkulator.py OPERASI A B")
        print("OPERASI: tambah | kurang | kali | bagi")
        raise SystemExit(1)

    operasi = sys.argv[1]

    try:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        hasil = hitung(operasi, a, b)
    except ValueError as error:
        print("Error:", error)
        raise SystemExit(1)

    print("Hasil:", hasil)

if __name__ == "__main__":
    main()
'''

APP_PY = r'''
import kalkulator

print(kalkulator.tambah(10, 20))
print(kalkulator.kali(4, 5))
'''

def tampilkan_template(nama, isi):
    print("\n" + "=" * 64)
    print(nama)
    print("=" * 64)
    print(isi.strip())

if __name__ == "__main__":
    tampilkan_template("cek_nama.py", CEK_NAMA_PY)
    tampilkan_template("module_dengan_guard.py", MODULE_GUARD_PY)
    tampilkan_template("lihat_arg.py", LIHAT_ARG_PY)
    tampilkan_template("salam.py", SALAM_PY)
    tampilkan_template("tambah.py", TAMBAH_PY)
    tampilkan_template("suhu.py", SUHU_PY)
    tampilkan_template("kalkulator.py", KALKULATOR_PY)
    tampilkan_template("app.py", APP_PY)
