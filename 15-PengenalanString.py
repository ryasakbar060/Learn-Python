# Pengenalan String

data = "Ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Hallo Apa Kabar?"')
print("'Hallo Apa Kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\Ryas")

# tab
print("ucup\t\t\totong, jadi jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 4 SD
""")
# multiline literal string dan raw
print(r"""
Nama : Ucup
Kelas : 4 SD \new normal
Website : www.ucup.com/newID
""")








