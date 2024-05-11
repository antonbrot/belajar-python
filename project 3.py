print("------------------------------------------------------------------------------------------------")
print("                                 DAFTAR MENU IPUL SARI                                          ")
print("------------------------------------------------------------------------------------------------")
print("a nasi bakar     ")
print("b soto makasar   ")
print("c es teh         ")
print()

nama_pembeli = input("masukan nama anda : ") 
num_meja= input("masukan nomer meja anda : ")
menu = input("masukan menu (a,b,c) : ")

print("")
if menu == "a" :
    pesanan = "nasi bakar"
    harga = 8000

elif menu == "b" :
    pesanan = "soto makasar"
    harga = 12000

elif menu == "c" :
    pesanan = "es teh"
    harga = 6000

else :
 print("menu tidak ada,silahkan refresh dan ulangi login !")
 print("")
 exit()

if pesanan is not None :
    jumlah = int(input("banyak pesanan (dengan angka) : "))

    pajak=11/100
    totalkotor = harga*jumlah
    totalbersih = totalkotor-(totalkotor*pajak)
    print(f"jumlah {pesanan} anda {jumlah} dengan harga {totalbersih}")