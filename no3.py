#3 Tulis program PYTHON untuk mencetak deret Fibonacci hingga n!

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

# Input nilai n dari pengguna
n = int(input("Masukkan nilai n untuk batas deret Fibonacci: "))

fibonacci(n)