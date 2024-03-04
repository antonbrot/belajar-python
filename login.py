from os import system

def login():
    system('cls')
    print("====================================\n")
    print("Selamat Datang di Kalkulator\n")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Misalkan username dan password yang diharapkan adalah 'admin' dan '1234'
    if username == 'admin' and password == '1234':
        return True
    else:
        print("Username atau password salah.")
        input("Tekan Enter untuk mencoba lagi...")
        return False
    
if login():
    while True:
        system('cls')
        print("====================================\n")
        userinput = int(input("Kalkulator\n\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n\n\nMasukan nomor: "))
