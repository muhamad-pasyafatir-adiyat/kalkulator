# kalkulaotr.py, kalkulator sederhana
from bantuan import format_hasil


def tambah(a, b):
    return a + b

if __name__ == "__main__":
    print("kalkulator sederhana")
    print("2 + 3 =", tambah(2, 3))
    print(format_hasil("+", 2, 3, tambah(2, 3)))
    