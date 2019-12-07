angka1 = int(input('Masukkan angka Pertama : '))
angka2 = int(input('Masukkan angka Kedua :   '))
print('operator : \n1.Penjumlahan \n2.Pengurangan \n'
     '3.Perkalian \n4.Pembagaian')
pilih = int(input ('Masukkan operator : '))
if pilih == 1:
    Tambah = angka1+angka2
    print('Hasilnya Adalah :',Tambah)
elif pilih == 2:
    Kurang = angka1-angka2
    print('Hasilnya Adalah :',Kurang)
elif pilih == 3:
    Kali = angka1*angka2
    print('Hasilnya Adalah :',Kali)
elif pilih == 4:
    Bagi = angka1/angka2
    print('Hasilnya Adalah :',Bagi)
else:
    print('Operator Yang Anda Masukkan Tidak Ada ....Coba Lagi!!')
