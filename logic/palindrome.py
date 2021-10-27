print("Mengecek Apakah Kata/Kalimat Palindrom & Bukan Palindrom")

print()

kata = input("Masukkan Kata/Kalimat : ")
temp = ""

for i in range(len(kata)-1, -1, -1): #Looping dari karakter / huruf terakhir
    temp+=kata[i]

print("Hasil Pengecekan : ", end="")
if(kata == temp): #Pengecekan kondisi dengan membandingkan kedua variabel
    print("Palindrom")
else:
    print("Bukan Palindrom")
