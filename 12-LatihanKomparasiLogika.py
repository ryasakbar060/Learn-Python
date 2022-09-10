# Latihan Komparasi Dan Logika

# ++++++3----------10++++++
# Kasus Gabungan

inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10 : "))

# +++++3-------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print('Kurang dari 3 ? ',isKurangDari)

# -------------10++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 3)
print('Lebih dari 10 ? ',isLebihDari)

# ++++++3----------10++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan : ", isCorrect)

print("\n",10*'=','\n')

# ----3++++++10------
# Kasus irisan

inputUser
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari dari 10 : "))

# -----3++++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print('Lebih dari 3 ? ',isLebihDari)

# ++++++++++++10------
isKurangDari = inputUser < 3
print('Kurang dari 10 ? ',isKurangDari)

# ----3++++++10------
isCorrect = isLebihDari and isKurangDari  
print("Angka yang anda masukkan : ", isCorrect)

print("\n",10*'=','\n')

# TUGAS FROM BANG PUKIS
# 1. -----0+++++5------8+++++11------
# 2. +++++0-----5+++++=8-----11++++++

# Answer
# 1. -----0+++++5------8+++++11------
inputUser = float(input("Masukkan angka 0<n<5 dan 8<n<11 : "))

# -----0+++++5------
# isLebihDariNol
isLebihDariNol = inputUser > 0
print('Lebih dari 0 ? ',isLebihDariNol)
# isKuragDariLima
isKurangDariLima = inputUser < 5
print('Kurang dari 5 ? ',isKurangDariLima)
# Result
resultNolLima = isLebihDariNol and isKurangDariLima
print("Hasil 0<n<5 : ", resultNolLima)

# ------8+++++11------
# isLebihDariDelapan
isLebihDariDelapan = inputUser > 8
print('Lebih dari 8 ? ',isLebihDariDelapan)
# isKurangDariSebelas
isKurangDariSebelas = inputUser < 11
print('Kurang dari 11 ? ',isKurangDariSebelas)
# Result
resultDelapanSebelas = isLebihDariDelapan and isKurangDariSebelas
print("Hasil 8<n<11 : ", resultDelapanSebelas)

# finalResult
finalResult = resultNolLima or resultDelapanSebelas
print("Hasil yang didapatkan yaitu : ", finalResult)

print("\n",10*'=','\n') 

# 2. +++++0-----5++++++8-----11++++++

# +++++0-----5++++++

# ++++++8-----11+++++
