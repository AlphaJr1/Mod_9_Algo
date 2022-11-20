def Bio():
    nama=str(input("Masukkan namamu : "))
    umur=str(input("Masukkan umurmu : "))
    ads=str(input("Masukkan alamatmu : "))
    email=str(input("Masukkan emailmu : "))
    dos=str(input("Siapa dosen walimu : "))
    f = open("Biodata.txt", "w")
    f.write (f'Nama : {nama}\nUmur : {umur} tahun \nAlamat :{ads}\nEmail : {email}\nDosen Wali : {dos}')
    f.close()
Bio()


def Baca():
    f = open("Biodata.txt", "r")
    print(f.read())
Baca()