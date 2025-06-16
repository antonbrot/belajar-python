num = 6
percobaan = 0
kesempatan = 5

print("GAME TEBAK ANGKA (1-15). Kamu punya 5 kesempatan😹")

while percobaan < kesempatan:
    s = input(f"Tebakan ke-{percobaan+1}: ")

    if not s.isdigit():
        print("Masukkan angka yang valid!")
        continue

    nilai = int(s)

    if nilai < 1 or nilai > 15:
        print("Angka harus antara 1 dan 15!")
        continue

    percobaan += 1
    tebakan = nilai

    if tebakan == num:
        print("You got it! Keren 🎉")
        break
    elif tebakan < num:
        print("Terlalu kecil.")
    else:
        print("Terlalu besar.")

if tebakan != num:
    print(f"Kamu kalah 😭, kesempatan habis. Jawabannya {num}.")
