#utilitas.py - fungsi bantu
def format_hasil (operasi, a, b, hasil):
    return f"{a} {operasi} {b} = {hasil}"

def pangkat(a, b):
    return a ** b# penulis: fatir

def modulus(a, b):
    if b == 0:
        return "Error: modulus dengan nol"
    nano utilitas.py # tambahkan pengecekan b == 0 pada fungsi modulusreturn a % b
## feature/modulus...origin/feature/modulus
python3 -c 'from utilitas import modulus; print(modulus(5, 0)); print(modulus(17, 5))'
