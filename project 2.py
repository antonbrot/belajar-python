from os import system
import math

# RUMUS BANGUN DATAR
def hitung_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    system('cls')
    print("Luas Persegi:", sisi * sisi)
    print("Keliling Persegi:", 4 * sisi)
    print("\nDeskripsi Rumus Persegi: ")
    print("Luas Persegi: sisi^2")
    print("Keliling Persegi: 4 * sisi")

def hitung_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    system('cls')
    print("Luas Persegi Panjang:", panjang * lebar)
    print("Keliling Persegi Panjang:", 2 * (panjang + lebar))
    print("\nDeskripsi Rumus Persegi Panjang: ")
    print("Luas Persegi Panjang: panjang * lebar")
    print("Keliling Persegi Panjang: 2 * (panjang + lebar)")

def hitung_segitiga():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    sisi_miring = float(input("Masukkan panjang sisi miring segitiga: "))
    system('cls')
    print("Luas Segitiga:", 0.5 * alas * tinggi)
    print("Keliling Segitiga:", alas + tinggi + sisi_miring)
    print("\nDeskripsi Rumus Segitiga: ")
    print("Luas Segitiga: 0.5 * alas * tinggi")
    print("Keliling Segitiga: alas + tinggi + sisi miring")

def hitung_lingkaran():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    system('cls')
    print("Luas Lingkaran:", math.pi * jari_jari ** 2)
    print("Keliling Lingkaran:", 2 * math.pi * jari_jari)
    print("\nDeskripsi Rumus Lingkaran: ")
    print("Luas Lingkaran: π * jari-jari^2")
    print("Keliling Lingkaran: 2 * π * jari-jari")
    
def hitung_jajar_genjang():
    alas = float(input("Masukkan panjang alas Jajar Genjang: "))
    tinggi = float(input("Masukkan tinggi Jajar Genjang: "))
    sisi_miring = float(input("Masukkan panjang sisi miring Jajar Genjang: "))
    system('cls')
    print("Luas Jajar Genjang:", alas * tinggi)
    print("Keliling Jajar Genjang:", 2 * alas + 2 * sisi_miring)
    print("\nDeskripsi Rumus Jajar Genjang: ")
    print("Luas Jajar Genjang: alas * tinggi")
    print("Keliling Jajar Genjang: 2 * alas + 2 * sisi miring")

# RUMUS BANGUN RUANG
def hitung_kubus():
    sisi = float(input("Masukkan panjang sisi kubus: "))
    system('cls')
    print("Volume Kubus:", sisi ** 3)
    print("Luas Permukaan Kubus:", 6 * sisi ** 2)
    print("\nDeskripsi Rumus Kubus: ")
    print("Volume Kubus: sisi^3")
    print("Luas Permukaan Kubus: 6 * sisi^2")

def hitung_balok():
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    system('cls')
    print("Volume Balok:", panjang * lebar * tinggi)
    print("Luas Permukaan Balok:", 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi))
    print("\nDeskripsi Rumus Balok: ")
    print("Volume Balok: panjang * lebar * tinggi")
    print("Luas Permukaan Balok: 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)")

def hitung_bola():
    jari_jari = float(input("Masukkan jari-jari bola: "))
    system('cls')
    print("Volume Bola:", (4 / 3) * math.pi * jari_jari ** 3)
    print("Luas Permukaan Bola:", 4 * math.pi * jari_jari ** 2)
    print("\nDeskripsi Rumus Bola: ")
    print("Volume Bola: (4 / 3) * π * jari-jari^3")
    print("Luas Permukaan Bola: 4 * π * jari-jari^2")
    

def hitung_tabung():
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    system('cls')
    print("Volume Tabung:", math.pi * jari_jari ** 2 * tinggi)
    print("Luas Permukaan Tabung:", 2 * math.pi * jari_jari * (jari_jari + tinggi))
    print("\nDeskripsi Rumus Tabung: ")
    print("Volume Tabung: π * jari-jari^2 * tinggi")
    print("Luas Permukaan Tabung: 2 * π * jari-jari * (jari-jari + tinggi)")

def hitung_kerucut():
    jari_jari = float(input("Masukkan jari-jari kerucut: "))
    tinggi = float(input("Masukkan tinggi kerucut: "))
    sisi_miring = math.sqrt(jari_jari ** 2 + tinggi ** 2)
    system('cls')
    print("Volume Kerucut:", (1 / 3) * math.pi * jari_jari ** 2 * tinggi)
    print("Luas Permukaan Kerucut:", math.pi * jari_jari * (jari_jari + sisi_miring))
    print("\nDeskripsi Rumus Kerucut: ")
    print("Volume Kerucut: (1 / 3) * π * jari-jari^2 * tinggi")
    print("Luas Permukaan Kerucut: π * jari-jari * (jari-jari + sisi_miring)")
    

def tampilkan_menu_bangun_ruang():
    print("Pilih Bangun Ruang yang ingin dihitung:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Bola")
    print("4. Tabung")
    print("5. Kerucut")
    print("99. Keluar")


def apat():
    print("Syafaatul")

def tampilkan_menu_bangun_datar():
    print("Pilih Bangun Datar yang ingin dihitung:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar Genjang")
    print("99. Keluar")

while True:
    system ('cls')
    print("Pilih jenis bangun yang ingin dihitung:")
    print("1. Bangun Datar")
    print("2. Bangun Ruang")
    print("99. Keluar")

    pilihan = int(input("Masukkan pilihan Anda: "))

    if pilihan == 1:
        system ('cls')
        tampilkan_menu_bangun_datar()
        pilihan_datar = int(input("Masukkan pilihan Anda: "))

        if pilihan_datar == 1:
            system ('cls')
            print("Perhitungan Persegi")
            hitung_persegi()
        elif pilihan_datar == 2:
            system ('cls')
            print("Perhitungan Persegi Panjang")
            hitung_persegi_panjang()
        elif pilihan_datar == 3:
            system ('cls')
            print("Perhitungan Segitiga")
            hitung_segitiga()
        elif pilihan_datar == 4:
            print("Perhitungan Lingkaran")
            system ('cls')
            hitung_lingkaran()
        elif pilihan_datar == 5:
            system ('cls')
            print("Perhitungan Jajar Genjang")
            hitung_jajar_genjang()
        elif pilihan_datar == 99:
            print("Kembali ke menu utama")
        else:
            print("Pilihan tidak valid!")

    elif pilihan == 2:
        system ('cls')
        tampilkan_menu_bangun_ruang()
        pilihan_ruang = int(input("Masukkan pilihan Anda: "))

        if pilihan_ruang == 1:
            system ('cls')
            print("Perhitungan Kubus")
            hitung_kubus()
        elif pilihan_ruang == 2:
            system ('cls')
            print("Perhitungan Balok")
            hitung_balok()
        elif pilihan_ruang == 3:
            system ('cls')
            print("Perhitungan Bola")
            hitung_bola()
        elif pilihan_ruang == 4:
            system ('cls')
            print("Perhitungan Tabung")
            hitung_tabung()
        elif pilihan_ruang == 5:
            system ('cls')
            print("Perhitungan Kerucut")
            hitung_kerucut()
        elif pilihan_ruang == 99:
            print("Kembali ke menu utama")
        else:
            print("Pilihan tidak valid!")

    elif pilihan == 99:
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid!")

    lanjut = input("Apakah Anda ingin melanjutkan menghitung? (Y/N): ")
    if lanjut.upper() != 'Y':
        print("Terima kasih telah menggunakan program ini!")
        break
