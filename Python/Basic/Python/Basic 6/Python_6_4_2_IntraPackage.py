# Python 6.4.2 - Intra-package References
# File ini berisi template. Salin ke file/folder sesuai judul.

TEMPLATES = {
    'struktur': 'shop_app/\n├── main.py\n└── toko/\n    ├── __init__.py\n    ├── core/\n    │   ├── __init__.py\n    │   ├── harga.py\n    │   └── validator.py\n    ├── reports/\n    │   ├── __init__.py\n    │   └── receipt.py\n    └── utils/\n        ├── __init__.py\n        └── formatter.py\n',
    'toko/core/validator.py': 'def valid_qty(qty):\n    return isinstance(qty, int) and qty > 0\n',
    'toko/utils/formatter.py': 'def rupiah(value):\n    return f"Rp{value:,.0f}"\n',
    'toko/reports/receipt.py': 'def buat_receipt(nama, total_text):\n    return (\n        f"Produk: {nama}\\n"\n        f"Total : {total_text}"\n    )\n',
    'toko/core/harga.py relative': 'from .validator import valid_qty\nfrom ..utils.formatter import rupiah\nfrom ..reports.receipt import buat_receipt\n\ndef proses(nama, harga, qty):\n    if not valid_qty(qty):\n        raise ValueError("Qty invalid")\n\n    total = harga * qty\n    return buat_receipt(\n        nama,\n        rupiah(total),\n    )\n',
    'toko/core/harga.py absolute': 'from toko.core.validator import valid_qty\nfrom toko.utils.formatter import rupiah\nfrom toko.reports.receipt import buat_receipt\n\ndef proses(nama, harga, qty):\n    if not valid_qty(qty):\n        raise ValueError("Qty invalid")\n\n    total = harga * qty\n    return buat_receipt(\n        nama,\n        rupiah(total),\n    )\n',
    'main.py': 'from toko.core.harga import proses\n\nprint(\n    proses(\n        "Keyboard",\n        150000,\n        2,\n    )\n)\n',
    'run module': '# dari folder project:\npython -m toko.core.harga\n',
    'relative sibling examples': '# module satu package:\nfrom . import validator\nfrom .validator import valid_qty\n\n# sibling subpackage:\nfrom ..reports import receipt\nfrom ..reports.receipt import buat_receipt\n',
}

def main():
    for nama, isi in TEMPLATES.items():
        print("\n" + "=" * 72)
        print(nama)
        print("=" * 72)
        print(isi)

if __name__ == "__main__":
    main()
