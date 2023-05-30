pembatas = "=" * 90
center = " " * 20
alamat = " Pamulang Permai 1, Jl Bougenvile 1 blok A38 no 10, Pamulang, Tangerang Selatan 15417"

produk = 4
namaProduk = ""
harga = ""
ppn = ""
total = ""
npwp = "1234567890"
formatted_npwp = '{}.{}.{}'.format(npwp[:3], npwp[3:6], npwp[6:])
nama_PT = "PT JAYA JAYA JAYA"

IPHONE_11 = 7000000
Macbook_air_m1 = 11000000
ifinix_11_play = 1200000
mechanical_keyboard = 500000

import datetime
current_date = datetime.date.today()
formatted_date = current_date.strftime("%d/%m/%Y")


# ============================================================================================================



print (f"{pembatas}\n {center}SELAMAT DATANG DI MINTA IJIN DULU STORE \n{alamat} \n {center} {formatted_npwp} \n{pembatas}")
print (formatted_date)
formatted_npwp = '{}.{}.{}'.format(npwp[:3], npwp[3:6], npwp[6:])

nama_pelanggan = input(" MASUKAN NAMA PELANGGAN ? \n ")
print(pembatas)

def daftar_barang ():
    print(daftar_barang)
    print(pembatas)
    print("List_product")  
    print (" 1. IPHONE_11: Rp {:,}".format(IPHONE_11))
    print (" 2. Macbook_air_m1: Rp {:,}".format(Macbook_air_m1))
    print (" 3. ifinix_11_play: Rp {:,}".format(ifinix_11_play))
    print (" 4. mechanical_keyboard: Rp {:,}".format(mechanical_keyboard))
    print(pembatas)

    pesan = int(input("SILAHKAN INPUT ANGKA PRODUCT YANG DIINGINKAN ? " ))
    jumlah_pesanan = int(input("QTY Product yang dipesan ?" ))

    if pesan == 1:
        total_harga = 7000000 * jumlah_pesanan
        namaProduk = "IPHONE_11"
        harga=(IPHONE_11 * jumlah_pesanan)
        ppn = int(harga * 0.1)
        if pesan >= 2:
           total =int(harga+ppn)
        else:
          total=int(harga+ppn)

    elif pesan == 2:
        total_harga = 11000000 * jumlah_pesanan
        namaProduk = "Macbook_air_m1"
        harga = (Macbook_air_m1 * jumlah_pesanan)
        ppn = int(harga * 0.1)
        if pesan >= 2:
            total =int(harga+ppn)
        else:
            total=int(harga+ppn)

    elif pesan == 3:
        total_harga = 1200000 * jumlah_pesanan
        namaProduk = "ifinix_11_play"
        harga = (ifinix_11_play * jumlah_pesanan)
        ppn = int(harga * 0.1)
        if pesan >= 2:
            total =int(harga+ppn)
        else:
            total=int(harga+ppn)
                
    elif pesan == 4:
        total_harga = 500000 * jumlah_pesanan
        namaProduk = "mechanical_keyboard"
        harga = (mechanical_keyboard * jumlah_pesanan)
        ppn = int(harga * 0.1)  
        if pesan >= 2:
            total =int(harga+ppn)
        else:
            total=int(harga+ppn)   
    else: 
        namaProduk = exit(" MAAF PRODUCT TIDAK ADA DI ETALASE")
    return      

    print (f"{pembatas}\n {center}TERIMAKASIH TELAH BERBELANJA \n{pembatas}")
    print("product :",namaProduk)
    print("Harga : " ,harga)
    print("PPN   : " , ppn)
    print(pembatas)
    print("Total Pembayaran :", total)
    print(pembatas)
    print (f"{pembatas}\n {center}TERIMAKASIH TELAH BERBELANJA \n{pembatas}")
   

    daftar_barang()


        







