# Latihan Perulangan

# Latihan perulangan membuat segitiga

sisi = 10

# 1. Menggunakan For

# dummy variable
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("Akhir dari for")
# 2. Menggunakan While

print("Awal While")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("Akhir dari while")
# 3. Hanya ganjil saja

print("Awal While")
count = 1
while True:
    if (count % 2):
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika cout melebihi sisi
    if count > sisi:
        break

print("Akhir dari while")
# 4. Hanya ganjil saja

print("Awal While")
count = 1
spasi = int(sisi/2)
print(spasi)
while True:
    if (count % 2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika cout melebihi sisi
    if count > sisi:
        break

print("Akhir dari while")
# 4. Tugas ketupat

print("Awal While")
count = 1
spasi = int(sisi/2)
while True:
    if (count % 2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika cout melebihi sisi
    if count > sisi:
        break
while True:
    if (count % 2):
        # print jika ganjil
        spasi += 1
        print(" "*spasi,"+"*count)
        count -= 1
    else:
        # akan kembali ke atas jika ganjil
        count -= 1
        continue

    # akan break jika cout melebihi sisi
    if count == 0:
        break

print("Akhir dari while")






















