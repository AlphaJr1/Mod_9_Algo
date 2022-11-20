def buat():
    jdl=str(input("Masukkan nama file : "))
    f=open(f'{jdl}',"w")
    nama=str(input("Masukkan Namamu : "))
    nim=str(input("Masukkan NIM kamu : "))
    akt=str(input("Masukkan tahun angkatanmu : "))
    f.write(f'Nama : {nama}\nNIM : {nim}\nAngkatan : {akt}')
    f.close()

def baca():
    jdl=str(input("Masukkan nama file : "))
    f = open(f'{jdl}', "r")
    text = f.read()
    print(text)
    f.close()

def tambah():
    jdl=str(input("Masukkan nama file : "))
    f = open(f'{jdl}', "a")
    mom=str(input("Masukkan Nama Ibumu : "))
    note=str(input("Catatan tambahan : "))
    f.write(f'Nama Ibu : {mom}\nNote : {note}')
    f.close()

while True:
    print(f'====== Program file Handling ======\n1. Membuat dan membaca file\n2. Membaca file\n3. Menambahkan text pada file\n4. Keluar dari program')
    n = int(input("Masukkan nomor perintahmu : "))
    if (n == 1):
        print(f'\n{buat()}\n')
    elif (n==2):
        print(f'\n{baca()}\n')
    elif (n==3):
        print(f'\n{tambah()}\n')
    elif (n==4):
        print("Terimakasih telah menggunakan program ini")
        break
    else :
        print("Mohon input nomor yang sesuai\n")