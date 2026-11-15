# kalkulaotr.py, kalkulator sederhana
from utilitas import format_hasil


def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

if __name__ == "__main__":
    print("Kalkulator Sederhana")
    print(format_hasil("+", 2, 3, tambah(2, 3)))
    print(format_hasil("-", 7, 4, kurang(7, 4)))
    print(format_hasil("*", 6, 7, kali(6, 7)))
    
