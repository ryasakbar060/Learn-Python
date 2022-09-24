# Latihan Percabangan

# Kalkulator Sederhana

# Roles: 
# 1. Data User -> angka1, angka2, aperator
# 2. Percabangan 
# 3. hasil / output

print(55*"=")
print("\t\tKalkulator Sederhana")
print(55*"=")

# Input Data User (Nilai dan Operator)
angka_1 = float(input("Masukkan angka 1 = "))
operator = input("Operator (+,-,x,/) = ")
angka_2 = float(input("Masukkan angka 2 = "))

# Percabangan
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasil penjumlahan dari {angka_1} dan {angka_2} adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasil pengurangan dari {angka_1} dan {angka_2} adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasil perkalian dari {angka_1} dan {angka_2} adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasil pembagian dari {angka_1} dan {angka_2} adalah {hasil}")
else:
    print("NOT FOUND 404...")

print(55*"=")
print("Terimakasih sudah menggunakan program kalkulator kami!")
print(55*"=")