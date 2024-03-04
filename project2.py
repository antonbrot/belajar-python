from os import system

def get_user_choice(prompt):
    while True:
        try:
            choice = int(input(prompt))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_perimeter_area_volume(bangun, dimensions):
    if bangun == "Persegi":
        sisi = float(input("Masukkan panjang sisi: "))
        return 4 * sisi, sisi ** 2
    elif bangun == "Persegi Panjang":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        return 2 * (panjang + lebar), panjang * lebar
    elif bangun == "Segitiga":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        return alas * 3, (alas * tinggi) / 2
    elif bangun == "Lingkaran":
        jari_jari = float(input("Masukkan jari-jari: "))
        return 2 * 3.14 * jari_jari, 3.14 * jari_jari ** 2
    elif bangun == "Jajar Genjang":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        return 2 * (panjang + lebar), panjang * lebar
    elif bangun == "Kubus":
        sisi = float(input("Masukkan panjang sisi: "))
        return 4 * sisi, sisi ** 3
    elif bangun == "Balok":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        tinggi = float(input("Masukkan tinggi: "))
        return 2 * (panjang + lebar + tinggi), panjang * lebar * tinggi
    elif bangun == "Tabung":
        jari_jari = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        return 2 * 3.14 * jari_jari + 2 * 3.14 * jari_jari * tinggi, 3.14 * jari_jari ** 2 * tinggi
    elif bangun == "Bola":
        jari_jari = float(input("Masukkan jari-jari: "))
        return 2 * 3.14 * jari_jari, (4/3) * 3.14 * jari_jari ** 3
    elif bangun == "Kerucut":
        jari_jari = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        return 2 * 3.14 * jari_jari + 2 * 3.14 * jari_jari * tinggi, (1/3) * 3.14 * jari_jari ** 2 * tinggi
    else:
        return None

def main():
    while True:
        print("================================================")
        print("                  KALKULATOR Bangun Datar             ")
        print("================================================")
        print("Pilih rumus yang ingin anda gunakan:")
        print("1. Rumus Bangun Datar")
        print("2. Rumus Bangun Ruang")
        print("99. Keluar")
        pilihan = get_user_choice("Masukkan pilihan Anda: ")
        if pilihan == 1:
            print("Pilih operasi yang ingin Anda lakukan:")
            print("1. Persegi")
            print("2. Persegi Panjang")
            print("3. Segitiga")
            print("4. Lingkaran")
            print("5. Jajar Genjang")
            print("99. Keluar")
            pilihan = get_user_choice("Masukkan pilihan Anda: ")
            if pilihan in [1, 2, 3, 4, 5]:
                bangun = input("Masukkan nama bangun: ")
                dimensions = input("Masukkan dimensi bangun: ").split()
                result = calculate_perimeter_area_volume(bangun, dimensions)
                print(f"Keliling {bangun}: {result[0]}")
                print(f"Luas {bangun}: {result[1]}")
            elif pilihan == 99:
                break
            else:
                print("Input tidak valid. Silakan pilih 1-5 untuk operasi bangun datar.")
        elif pilihan == 2:
            print("Pilih operasi yang ingin Anda lakukan:")
            print("1. Kubus")
            print("2. Balok")
            print("3. Tabung")
            print("4. Bola")
            print("5. Kerucut")
            print("99. Keluar")
            pilihan = get_user_choice("Masukkan pilihan Anda: ")
            if pilihan in [1, 2, 3, 4, 5]:
                bangun = input("Masukkan nama bangun: ")
                dimensions = input("Masukkan dimensi bangun: ").split()
                result = calculate_perimeter_area_volume(bangun, dimensions)
                print(f"Keliling {bangun}: {result[0]}")
                print(f"Volume {bangun}: {result[1]}")
            elif pilihan == 99:
                break
            else:
                print("Input tidak valid. Silakan pilih 1-5 untuk operasi bangun ruang.")
        elif pilihan == 99:
            break
        else:
            print("Input tidak valid. Silakan pilih 1-2 untuk operasi bangun.")

    input("Tekan Enter untuk keluar.")

if __name__ == "__main__":
    main()