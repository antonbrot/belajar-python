while True:
    user_input = input("Masukkan nilai ujian (0-100) atau ketik 'exit' untuk keluar: ")

    if user_input.lower() == 'exit':
        print("Program dihentikan.")
        break

    try:
        grade = int(user_input)

        if grade < 0 or grade > 100:
            print("Nilai tidak valid. Harus antara 0 dan 100.")
        elif grade >= 55:
            print("You passed.")
        else:
            print("You failed.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka atau ketik 'exit'.")

    print()
