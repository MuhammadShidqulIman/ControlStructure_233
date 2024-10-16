#5. Tulis program PYTHON untuk menghasilkan desain berikut
    # 1
    # 2 2
    # 3 3 3
    # 4 4 4 4 
    # 5 5 5 5 5
    # Jika pengguna memasukkan nilai n sebagai 5

def cetak_pola(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))
cetak_pola(n)