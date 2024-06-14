tuple_1 = (2, 3, 4)
tuple_2 = ("Wasd", "Qwerty")
tuple_3 = (24, False, "hello python")

print(tuple_1[1])
list = list(tuple_1)
list[0] = 5
tuple_1 = tuple(list)
print(tuple_1)

lokasi = ("Jakarta", -5.2345, 23.23523)
print("kota", lokasi [0])
print("lintang", lokasi [1])
print("bujur", lokasi [2])

produk = ("Laptop", 15000000, 20)
print("harga =", produk[1])

Karyawan = ("Alice", "Engineering", 5)
print(Karyawan[1], Karyawan[2])

db_config = ("localhost", "admin", "password", "database_name")

print(db_config[2], db_config[3])

Mahasiswa = ("Gojo", "matematika", [85, 90, 92])
print(Mahasiswa[0], Mahasiswa[2])
Nilai = Mahasiswa[2]
print(Nilai)
Nilai[0] = 87
print(Nilai)
