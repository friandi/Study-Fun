"""
Python 8.3 - Handling Exceptions
Menangani Kesalahan Program
"""


def demo_try_except():
    try:
        angka = int("10")
    except ValueError:
        print("Input tidak valid")
    else:
        print("Angka:", angka)


def demo_value_error(teks):
    try:
        angka = int(teks)
    except ValueError:
        print("Input harus berupa angka")
        return None
    else:
        return angka


def demo_zero_division(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Pembagi tidak boleh 0")
        return None
    else:
        return hasil


def demo_multiple_except(teks_pembagi):
    try:
        pembagi = float(teks_pembagi)
        hasil = 100 / pembagi

    except ValueError:
        print("Pembagi harus berupa angka")
        return None

    except ZeroDivisionError:
        print("Pembagi tidak boleh 0")
        return None

    else:
        return hasil


def demo_tuple_except(value):
    try:
        hasil = int(value)
    except (ValueError, TypeError):
        print("Data tidak dapat dikonversi ke int")
        return None
    else:
        return hasil


def demo_exception_as_e():
    try:
        int("abc")
    except Exception as e:
        print("Jenis :", type(e).__name__)
        print("Pesan :", str(e))
        print("Args  :", e.args)


def demo_function_propagation():
    def bagi(a, b):
        return a / b

    try:
        print(
            bagi(10, 0)
        )
    except ZeroDivisionError:
        print(
            "Exception dari function "
            "ditangani di caller"
        )


def input_angka_positif():
    while True:
        try:
            n = int(
                input(
                    "Masukkan angka (>0): "
                )
            )

        except ValueError:
            print(
                "Input harus berupa angka."
            )
            continue

        if n <= 0:
            print(
                "Angka harus lebih dari 0."
            )
            continue

        return n


def input_angka_positif_else():
    while True:
        try:
            n = int(
                input(
                    "Masukkan angka (>0): "
                )
            )

        except ValueError:
            print(
                "Input harus berupa angka."
            )

        else:
            if n > 0:
                return n

            print(
                "Angka harus lebih dari 0."
            )


def demo_keyboard_interrupt():
    print(
        "Contoh KeyboardInterrupt."
    )
    print(
        "Aktifkan loop berikut "
        "dan tekan Ctrl+C:"
    )

    print(
        """
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Dihentikan user")
"""
    )


def demo_system_exit():
    print(
        "SystemExit biasanya "
        "dibangkitkan oleh sys.exit()."
    )

    print(
        """
import sys

if kondisi:
    sys.exit("Program dihentikan")
"""
    )


def main():
    print(
        "Python 8.3 - "
        "Handling Exceptions"
    )

    demo_try_except()

    print(
        "ValueError test:",
        demo_value_error("abc"),
    )

    print(
        "ZeroDivision test:",
        demo_zero_division(10, 0),
    )

    print(
        "Multiple except test:",
        demo_multiple_except("0"),
    )

    print(
        "Tuple except test:",
        demo_tuple_except(None),
    )

    demo_exception_as_e()
    demo_function_propagation()
    demo_keyboard_interrupt()
    demo_system_exit()

    # Aktifkan untuk latihan interaktif:
    # nilai = input_angka_positif()
    # print("Input valid:", nilai)


if __name__ == "__main__":
    main()
