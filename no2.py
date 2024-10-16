#2 Tulislah program PYTHON untuk mencari bilangan terbesar dari tiga bilangan!

def bilangan_terbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input tiga bilangan dari pengguna
bilangan1 = float(input("Isi bilangan pertama: "))
bilangan2 = float(input("Isi bilangan kedua: "))
bilangan3 = float(input("Isi bilangan ketiga: "))

print("Bilangan terbesar adalah:", bilangan_terbesar(bilangan1, bilangan2, bilangan3))