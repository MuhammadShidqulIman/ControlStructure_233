#1. Tulis program PYTHON untuk mengevaluasi kinerja siswa
#  If % is >=90 then Excellent performance
#  If % is >=80 then  Very Good performance
#   If % is >=70 then Good performance
#   If % is >=60 then average performance

nilai = input("Masukkan Nilai: ")

nilai = int(nilai)
if nilai >= 90:
    print(" Excellent performance")
elif nilai >= 80:
    print(" Very Good performance")
elif nilai >= 70:
    print(" Good performance")
elif nilai >= 60:
    print(" average performance")
else:
    print("Performa perlu ditingkatkan")


    