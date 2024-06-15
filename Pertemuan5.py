profil = ["Noval", False, 16,["gaming", "learning"]]
profile_1 = {
    "name": "Noval", #key: value
    "is_male": False,
    "age": 16,
    "hobbies": ["gaming", "learning"],
}

print(profil[0])
print(profile_1["name"])
print('umur', profile_1["name"], ";", profile_1["age"])

karyawan = {
    "nama": "Althaf",
    "pekerjaan": "Joki Monteg",
}
print(karyawan)
karyawan["pekerjaan"] = "penjaga musang"
print(karyawan)
karyawan["instansi"] = "technonatura Jogja"
print(karyawan)

karyawan.pop("nama")
print(karyawan)

buku = {}
judul = "laskar pelangi"
penulis = "Ucok"
tahun = 2000
buku["judul"] = judul
print(buku)

buku = [judul, penulis, tahun]
print(buku)
