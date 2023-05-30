center = " " * 10
batas  = "=" * 60
maksimum = 3
Repetisi = True

print (f"{center} SELAMAT DATANG DI QALESYA MEAT {center}")
print (batas)
nomormeja = input (" MASUKAN NOMOR MEJA PELANGGAN?\n ")
nama_pelayan = input (" MASUKAN NAMA PELAYAN ? \n ")

while Repetisi == True:
        Repetisi = False
        print(batas)
        print (f"{center} DAFTAR MENU MAKANAN {center}")
        print(batas)
        print("PAKET DAGING SUPER")
        print(" 1. PAKET SUPER DAGING MENTAH, DAGING + MINUM YANG SEGAR RP. 50,000")
        print(" 2. PAKET SUPER DAGING SEMI MATANG, DAGING + MINUM TEH MANIS. 75,000")
        print(" 3. PAKET SUPER DAGING MATENG, DAGING + MINUMAN SODA RP. 100,000 ")
        pesanan = int(input (" \n SILAHKAN INPUT PAKET YANG DIPILIH ? "))

        if pesanan == 1 or pesanan == 2 or pesanan == 3:
                jumlah_pesanan = (int(input(" JUMLAH PAKET YANG DIPESAN ? ")))
                if pesanan == 1:
                        total_harga = 50 * jumlah_pesanan
                        pajak = int(total_harga * 0.11)
                        print( f"Paket daging super Rp. 50,000 (x{jumlah_pesanan})")
                elif pesanan == 2:
                        total_harga = 75 * jumlah_pesanan
                        pajak = int(total_harga * 0.11)
                        print( f" Daging Semi Matang Rp. 75,000 (x{jumlah_pesanan})")
                elif pesanan == 3:
                        total_harga = 100 * jumlah_pesanan
                        pajak = int(total_harga * 0.11)
                        print( f" Daging Matang Rp. 100,000 (x{jumlah_pesanan})")

                print(f" TOTAL =  Rp. {total_harga},000")
                print(batas)
                print (f"{center} TERIMAKASIH TELAH BERBELANJA DI RESTO KAMi {center}")
                print(batas)

        else:
                print("APA YANG ANDA MASUKAN SALAH, SILAHKAN COBA LAGI")
                        

