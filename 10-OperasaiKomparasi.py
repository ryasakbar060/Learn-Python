# Operasi Komparasi

# Setiap hasil dari operasi adalah boolean

# >,<,<=,==,!=,is,is not

a = 4
b = 2

# Lebih besar dari >
print('===Lebih Dari (>)===')
hasil = a > 3
print(a, " > ", 3, " = ", hasil)
hasil = b > 3
print(b, " > ", 3, " = ", hasil)
hasil = b > 3
print(b, " > ", 2, " = ", hasil)

# Kurang dari <
print('===Kurang Dari (<)===')
hasil = a < 3
print(a, " < ", 3, " = ", hasil)
hasil = b < 3
print(b, " < ", 3, " = ", hasil)
hasil = b < 2
print(b, " < ", 2, " = ", hasil)

# Lebih dari samadengan >=
print('===Lebih Dari Samadengan (>=)===')
hasil = a >= 3
print(a, " >= ", 3, " = ", hasil)
hasil = b >= 3
print(b, " >= ", 3, " = ", hasil)
hasil = b >= 2
print(b, " >= ", 2, " = ", hasil)

# Kurang dari samadengan >=
print('===Kurang Dari Samadengan (>=)===')
hasil = a <= 3
print(a, " <= ", 3, " = ", hasil)
hasil = b <= 3
print(b, " <= ", 3, " = ", hasil)
hasil = b <= 2
print(b, " <= ", 2, " = ", hasil)

# Samadengan ==
print('===Samadengan (==)===')
hasil = a == 4
print(a, " == ", 4, " = ", hasil)
hasil = b == 4
print(b, " == ", 4, " = ", hasil)

# Tidak Samadengan ==
print('===Tidak Samadengan (!=)===')
hasil = a != 4
print(a, " != ", 4, " = ", hasil)
hasil = b != 4
print(b, " != ", 4, " = ", hasil)

# 'is' sebagai komparasi object identity
print('===Object Identity (is)===')
x = 5 # ini adalah assignment membuat object
y = 5
print('Nilai x = ', x,', id = ', hex(id(x)))
print('Nilai y = ', y,', id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('Nilai x = ', x,', id = ', hex(id(x)))
print('Nilai y = ', y,', id = ', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

# 'is not' sebagai komparasi object identity
print('===Object Identity (is not)===')
x = 5 # ini adalah assignment membuat object
y = 5
print('Nilai x = ', x,', id = ', hex(id(x)))
print('Nilai y = ', y,', id = ', hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('Nilai x = ', x,', id = ', hex(id(x)))
print('Nilai y = ', y,', id = ', hex(id(y)))
hasil = x is not y
print('x is not y = ', hasil)