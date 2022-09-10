# Episode Input User

# Data yang di masukkan pasti string
data = input("Masukkan nama: ")

print("data = ", data, ",type = ",type(data))

# Jika kita ingin mengambil data int
angka = int(input("Masukkan angka: "))
# angka = float(input("Masukkan angka: "))
print("data = ", angka, ",type = ",type(angka))

# Bagaimana dengan boolean
biner = bool(int(input("Masukkan nilai boolean: ")))
print("data = ", biner, ",type = ",type(biner))