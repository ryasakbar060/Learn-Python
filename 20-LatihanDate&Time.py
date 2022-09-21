# Latihan Date and Time

import datetime as dt

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: ")) 

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Hari lahir anda adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")

# hari_ini = dt.date.today()
# print(hari_ini)
# print(f"Hari ini adalah hari = {hari_ini:%A}") # :%A untuk memunculkan nama hari 

# tanggal = dt.date(2000,11,10)
# print(tanggal)
# print(f"Hari lahir anda adalah = {tanggal:%A}") # :%A untuk memunculkan nama hari 