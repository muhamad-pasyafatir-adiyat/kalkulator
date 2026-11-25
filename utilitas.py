#utilitas.py - fungsi bantu
def format_hasil (operasi, a, b, hasil):
    return f"{a} {operasi} {b} = {hasil}"

def pangkat(a, b):
    return a ** b# penulis: fatir

def modulus(a, b):
    if b == 0:
        return "Error: modulus dengan nol"
    return a % b
