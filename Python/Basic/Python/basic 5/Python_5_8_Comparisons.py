"""
Python 5.8 - Comparing Sequences and Other Types
Perbandingan Data + Evaluasi Akhir Modul 5.
"""

print("=== 5.8.1 PERBANDINGAN SEQUENCE ===")
print([1, 2] == [1, 2])
print([1, 2] < [1, 3])

print("\n=== 5.8.2 LIST ===")
print([1, 2] == [1, 2])
print([1, 2] == [1, 3])
print([1, 2] < [1, 3])
print([2, 0] > [1, 99])

print("\n=== 5.8.3 TUPLE ===")
print((1, 2) == (1, 2))
print((1, 2) < (1, 3))
print((2, 0) > (1, 99))
print([1, 2] == (1, 2))

print("\n=== 5.8.4 STRING ===")
print("apel" < "jeruk")
print("apel" == "apel")
print("abc" < "abd")
print("Z" < "a")

a = "Python"
b = "python"
print(a == b)
print(a.casefold() == b.casefold())

print("\n=== 5.8.5 LEXICOGRAPHICAL ===")
print([1, 2, 9] < [1, 3, 0])
print("apel" < "april")

print("\n=== 5.8.6 ELEMEN DEMI ELEMEN ===")
print([1, 2, 5] < [1, 2, 7])
print([9, 0] < [1, 999])

print("\n=== 5.8.7 NESTED ===")
a = [[1, 2], 3]
b = [[1, 3], 0]
print(a < b)

print("\n=== 5.8.8 PANJANG BERBEDA ===")
print([1, 2] < [1, 2, 3])
print((1, 2) < (1, 2, 0))
print("app" < "apple")
print([9] < [1, 2, 3, 4])

print("\n=== 5.8.9 INT VS FLOAT ===")
print(1 == 1.0)
print(2 < 2.5)
print(3.0 >= 3)
print(type(1) == type(1.0))
print([1, 2] == [1.0, 2.0])

print("\n=== 5.8.10 TYPEERROR ===")
print(3 == "3")

try:
    print(3 < "3")
except TypeError as error:
    print("TypeError:", error)

try:
    print([1, "2"] < [1, 3])
except TypeError as error:
    print("TypeError:", error)

angka_teks = "4"
angka = 3
print(angka < int(angka_teks))

print("\n=== 5.8.11 LATIHAN ===")
tests = [
    ([1, 2, 9], [1, 3, 0]),
    ([5], [1, 9, 9]),
    ([1, 2], [1, 2]),
]

for kiri, kanan in tests:
    print(kiri, "<", kanan, "=", kiri < kanan)
    print(kiri, "==", kanan, "=", kiri == kanan)

print("\nEvaluasi string:")
print("apel" < "april")
print("Zoo" < "apple")
print("abc" == "ABC")

print("\nEvaluasi nested:")
print([[1, 2], 5] < [[1, 3], 0])
