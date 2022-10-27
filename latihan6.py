print("------------------------------------------------------")
print("----------- Latihan 6 - muhamad dafik kholik firdaus -----------")
print("------------------------------------------------------")

print("\n======================================================")
print("=========== Program menentukan Grade Nilai ===========")
print("======================================================")

nama = input("\nMasukan nama Mahasiswa : ")
nilai = input("Inputkan nilai akhir   : ")

if nilai.isnumeric() >= 90:
    grade = "A"
    predikat = "Dengan Pujian"

elif nilai.isnumeric() >= 80:
    grade = "B"
    predikat = "Sangat Memuaskan"

elif nilai.isnumeric() >= 70:
    grade = "C"
    predikat = "Memuaskan"

elif nilai.isnumeric() >= 60:
    grade = "D"
    predikat = "Tidak Memuaskan"

elif nilai.isnumeric() >= 1:
    grade = "E"
    predikat = "Tidak Lulus"

else:
    print("\nMaaf input anda Salah")

print("\n------------------------")
print("Nama Mahasiswa : ", nama)
print("Grade Anda     : ", grade)
print("Predikat Anda  : ", predikat)

print("\n======================================================")

