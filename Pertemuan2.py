print("Robot siap beraksi") 
print("Robot bergerak maju") #menampilkan teks "Robot bergerak maju"
speed = ("kecepatan Robot = 10")
print(speed)

arah = "kiri"
kecepatan = "5"
durasi = "10 detik"
print("Robot bergerak ke", arah, "dengan kecepatan", kecepatan, "Selama", durasi)


status1 = "Robot aktif" 
status2 = "menunggu perintah"
print(status1, "dan", status2)

# list with int as element's data type
list_1 = [2, 4, 8, 16,]
# list with str as element's data type
list_2 = ["grayson", "jason", "tim", "damian"]
# list with various data type in the element
list_3 = [2, False, "hello Python"]
hari = ["senin", "selasa", "Rabu", "kamis", "jum'at", "sabtu", "minggu"]

print(list_1)
print(list_1 [2])
print(list_2 [3])
print(list_3[0])
print(hari[2])
print("hari ini hari", hari[5])

nama_depan = "akhdan"
nama_belakang = "kautsar"
umur = "Secret"
sudah_menikah = False
Agama = "seusai kepercayaan masing masing"

Profil = [nama_depan, nama_belakang, umur, sudah_menikah, Agama]
print(Profil)

Profil.append(Agama)
print(Profil)

buah = ["mangga", "pisang", "jeruk", "anggur"]
buah[0] = "durian"
print(buah)
print(len(buah))

buah.append("apel")
print(buah)

buah.remove("anggur")
print(buah)
