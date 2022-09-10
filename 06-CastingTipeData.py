# Belajar Casting
# Merubah dari satu tipe ke tipe lain
# Tipe dat: int, float, str, bool

# Integer
print("====INTEGER====")
data_int = 9
print("data = ", data_int, ",type = ",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # False apabila nilai int = 0
print("data = ", data_float, ",type = ",type(data_float))
print("data = ", data_str, ",type = ",type(data_str))
print("data = ", data_bool, ",type = ",type(data_bool))

# Float
print("====FLOAT====")
data_float = 9.7
print("data = ", data_float, ",type = ",type(data_float))

data_int   = int(data_float) # Akan dibulatkan ke bawah
data_str   = str(data_float)
data_bool  = bool(data_float) # False apabila nilai int = 0
print("data = ", data_int, ",type = ",type(data_int))
print("data = ", data_str, ",type = ",type(data_str))
print("data = ", data_bool, ",type = ",type(data_bool))

# Boolean
print("====BOOLEAN====")
data_bool = False
print("data = ", data_bool, ",type = ",type(data_bool))

data_int   = int(data_bool) # Akan dibulatkan ke bawah
data_str   = str(data_bool)
data_float  = float(data_bool) 
print("data = ", data_int, ",type = ",type(data_int))
print("data = ", data_str, ",type = ",type(data_str))
print("data = ", data_float, ",type = ",type(data_float))

# String
print("====STRING====")
data_str = "8"
print("data = ", data_str, ",type = ",type(data_str))

data_int   = int(data_str) # String harus angka
data_bool   = bool(data_str) # False apabila string kosong / data_str = ""
data_float  = float(data_str) # String harus angka
print("data = ", data_int, ",type = ",type(data_int))
print("data = ", data_bool, ",type = ",type(data_bool))
print("data = ", data_float, ",type = ",type(data_float))
