# Latihan konversi satuan temperatur

'''
            | Celcius | Reamur   | Fahrenheit     | Kelvin       |
____________|_________|__________|________________|______________|
Celcius     |         |4/5 C     | 9/5 C + 32     |C + 273       |
Reamur      |5/4 R    |          | 9/4 R + 32     |5/4 R +273    |
Fahrenheit  |5/9(F-32)|4/9(F-32) |                |5/9(F-32) +273|
Kelvin      |K-273    |4/5(K-273)| 9/5(K-273) + 32|              |
'''

print("\nPROGRAM KONVERSI TEMPERATUR\n")

print("===Konversi Celcius To (Reamur,Fahrenheit,Kelvin)===")
celcius = float(input('Masukkan suhu dalam celcius : '))
print("Suhu adalah", celcius, "C")

# Reamur
# (4/5)C
reamur = (4 / 5) * celcius
print("Suhu dalam reamur", reamur, "R")

# Fahrenheit
fahrenheit = (9 / 5) * celcius + 32
print("Suhu dalam fahrenheit", fahrenheit, "F")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin", kelvin, "K")

print("===Konversi Reamur To (Celcius,Fahrenheit,Kelvin)===")
reamur = float(input('Masukkan suhu dalam reamur : '))
print("Suhu adalah", reamur, "R")

celcius = (5 / 4) * reamur
print("Suhu dalam celcius", celcius, "C")

fahrenheit = (9 / 4) * reamur + 32
print("Suhu dalam fahrenheit", fahrenheit, "F")

kelvin = (5 / 4) * reamur + 273
print("Suhu dalam kelvin", kelvin, "K")

print("===Konversi Fahrenheit To (Celcius,Reamur,Kelvin)===")
fahrenheit = float(input('Masukkan suhu dalam fahrenheit : '))
print("Suhu adalah", fahrenheit, "R")

celcius = 5 / 9 * (fahrenheit-32)
print("Suhu dalam celcius", celcius, "C")

reamur = 4 / 9 * (fahrenheit-32)
print("Suhu dalam reamur", reamur, "R")

kelvin = 5 / 9 * (fahrenheit-32) + 273
print("Suhu dalam kelvin", kelvin, "K")

print("===Konversi Kelvin To (Celcius,Reamur,Fahrenheit)===")
kelvin = float(input('Masukkan suhu dalam kelvin : '))
print("Suhu adalah", kelvin, "K")

celcius = kelvin - 273
print("Suhu dalam celcius", celcius, "C")

reamur = 4 / 5 * (kelvin-273) 
print("Suhu dalam reamur", reamur, "R")

fahrenheit = 9 / 5 * (kelvin-273) + 32
print("Suhu dalam fahrenheit", fahrenheit, "F")


