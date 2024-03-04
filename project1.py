import random

def ambil_kata():
    kata_kunci = ["apel", "jeruk", "anggur", "pisang", "mangga"]
    return random.choice(kata_kunci)

def tebak_kata(kata):
    tebakan = "_" * len(kata)
    tebakan_list = list(tebakan)
    huruf_sudah_ditebak = []
    kesempatan = 7

    while kesempatan > 0:
        tebakan_terbaru = ''.join(tebakan_list)
        if tebakan_terbaru == kata:
            print("Selamat, Anda berhasil menebak kata:", kata)
            break

        print("Kata yang harus ditebak:", tebakan_terbaru)
        tebakan_pengguna = input("Tebak satu huruf atau kata: ").lower()

        if len(tebakan_pengguna) == 1 and tebakan_pengguna.isalpha():
            if tebakan_pengguna in huruf_sudah_ditebak:
                print("Anda sudah menebak huruf ini sebelumnya.")
            elif tebakan_pengguna not in kata:
                print("Huruf ini tidak ada dalam kata.")
                kesempatan -= 1
                print("Sisa kesempatan Anda:", kesempatan)
            else:
                for i in range(len(kata)):
                    if kata[i] == tebakan_pengguna:
                        tebakan_list[i] = tebakan_pengguna
                huruf_sudah_ditebak.append(tebakan_pengguna)
        elif len(tebakan_pengguna) == len(kata) and tebakan_pengguna.isalpha():
            if tebakan_pengguna == kata:
                print("Selamat, Anda berhasil menebak kata:", kata)
                break
            else:
                print("Tebakan Anda salah.")
                kesempatan -= 1
                print("Sisa kesempatan Anda:", kesempatan)
        else:
            print("Masukkan tidak valid. Coba lagi.")

    else:
        print("Maaf, Anda kehabisan kesempatan. Kata yang benar adalah:", kata)

def main():
    print("Selamat datang di Game Tebak Kata!")
    kata = ambil_kata()
    tebak_kata(kata)
    print("Terima kasih telah bermain!")

if __name__ == "__main__":
    main()
