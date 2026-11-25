# kalkulator.py - Kalkulator sederhana
from utilitas import format_hasil, pangkat, modulus


def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        return "Error: pembagian dengan nol"
    return round(a / b, 2)

def akar(a):
    if a < 0:
        return "Error: akar bilangan negatif"
    return round(a ** 0.5, 2)

def maksimum(a, b):
    return a if a > b else b


if __name__ == "__main__":
    print("Kalkulator Sederhana")
    print(format_hasil("+", 2, 3, tambah(2, 3)))
    print(format_hasil("-", 7, 4, kurang(7, 4)))
    print(format_hasil("x", 6, 7, kali(6, 7)))
    print(format_hasil(":", 8, 2, bagi(8, 2)))
    print(format_hasil("max", 10, 25, maksimum(10, 25)))
    print(format_hasil("^", 2, 10, pangkat(2, 10)))
    print("akar 16 =", akar(16))
