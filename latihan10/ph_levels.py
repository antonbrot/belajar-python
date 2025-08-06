# ph_levels.py

while True:
    user_input = input("Masukkan nilai pH (0-14) atau ketik 'exit' untuk keluar: ")

    if user_input.lower() == 'exit':
        print("Program dihentikan.")
        break

    try:
        ph = float(user_input)

        if ph < 0 or ph > 14:
            print("Nilai pH tidak valid. Harus antara 0 hingga 14.")
        elif ph < 7:
            print("Acidic")
        elif ph > 7:
            print("Basic")
        else:
            print("Neutral")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka antara 0 hingga 14 atau 'exit'.")

    print()
