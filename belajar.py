from os import system
import time


class login:
    def login():
        system('cls')
        print("================================================")
        print("              Selamat Datang di Kalkulator")
        print("================================================\n")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == 'asep' and password == '2222':
            return True
        else:
            print("Username atau password salah.")
            input("Tekan Enter untuk mencoba lagi...")
            return False


def tampilkan_menu():
    print("================================================\n")
    print("                  KALKULATOR             \n")
    print("================================================\n")
    print("Pilih operasi yang ingin Anda lakukan:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar\n")

def hitung_penjumlahan():
    system('cls')
    print("================================================")
    print("            KALKULATOR PENJUMLAHAN     ")
    print("================================================\n")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    print ("Menghitung..")
    time.sleep(1.5)
    Hasil = angka1 + angka2
    print("hasil: ", Hasil, "\n")
    input("Tekan Enter untuk melanjutkan...")

def hitung_pengurangan():
    system('cls')
    print("================================================")
    print("            KALKULATOR PENGURANGAN     ")
    print("================================================\n")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    print ("Menghitung..")
    time.sleep(1.5)
    Hasil = angka1 - angka2
    print("hasil: ", Hasil, "\n")
    input("Tekan Enter untuk melanjutkan...")

def hitung_perkalian():
    system('cls')
    print("================================================")
    print("            KALKULATOR PERKALIAN     ")
    print("================================================\n")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    print ("Menghitung..")
    time.sleep(1.5)
    Hasil = angka1 * angka2
    print("hasil: ", Hasil, "\n")
    input("Tekan Enter untuk melanjutkan...")

def hitung_pembagian():
    system('cls')
    print("================================================")
    print("            KALKULATOR PEMBAGIAN     ")
    print("================================================\n")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    system('cls')
    print ("Menghitung..")
    time.sleep(1.5)
    Hasil = angka1 / angka2
    print("hasil: ", Hasil, "\n")
    input("Tekan Enter untuk melanjutkan...")

def keluar():
    system('cls')
    print("================================================")
    print("Terima kasih telah menggunakan kalkulator!")
    print("================================================\n")

if login():
    while True:
        system('cls')
        tampilkan_menu()
        userinput = input("Masukkan nomor operasi yang dipilih: ")
        if userinput == '1':
            hitung_penjumlahan()
        elif userinput == '2':
            hitung_pengurangan()
        elif userinput == '3':
            hitung_perkalian()
        elif userinput == '4':
            hitung_pembagian()
        elif userinput == '5':
            keluar()
            break
        else:
            print("Input tidak valid! Silakan masukkan nomor yang sesuai dengan pilihan menu.")
            input("Tekan Enter untuk melanjutkan...")
