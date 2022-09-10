# Operasi Aritmatika

a = 13
b = 3

# Operasi Tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# Operasi Pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# Operasi Perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# Operasi Pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# Operasi Eksponen (Pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# Operasi Modulus (Sisa Bagi) %
hasil = a % b
print(a,'%',b,'=',hasil)

# Operasi Floor Division //
hasil = a // b
print(a,'//',b,'=',hasil)

# Prioritas Operasi, Operational Precedence:
'''
    Urutan prioritas operasi:
    1. ()
    2. eksponen **
    3. perkalian dkk (* / ** % //)
    4. Pertambahan dan Pengurangan (+ -)
'''
x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=',hasil)