# Format Stering

# contoh generic
# string
nama = "otong"
format_str = f"hello {nama}"

print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str= f"bilangan bulat = {angka:d}" # :d menandakan bilangan bulat
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}" # :, memunculkan koma pada angka ribuan
print(format_str)

# bilangan jutaan
angka = 2000000
format_str = f"jutaan = {angka:,}" # :, memunculkan pada angka ribuan
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" # :.2f untuk menentukan berapa banyak angka di belakang koma 
print(format_str)

# menampilkan leading zero 
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}" # 
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.4567
format_minus = f"minus = {angka_minus:+d}" # 
format_plus = f"plus = {angka_plus:+.2f}" # 
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp. {harga * jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)