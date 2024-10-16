#4 Tulis program PYTHON untuk mencetak bilangan ganjil hingga n!

def cetak_bilangan_ganjil(n):
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i, end=" ")

# Input nilai n dari pengguna
n = int(input("Masukkan nilai n untuk batas bilangan ganjil: "))

# Mencetak bilangan ganjil
cetak_bilangan_ganjil(n)