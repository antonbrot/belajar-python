def panjang_kata(kata):
    """Mengembalikan panjang kata (jumlah karakter)."""
    return len(kata)


def tampilkan_mapel(mapel_list):
    """Mencetak daftar mata pelajaran RPL."""
    print("Mata Pelajaran RPL:")
    for m in mapel_list:
        print(f"- {m}")


def total_nilai(komponen_list):
    """Menghitung total nilai proyek dari daftar komponen."""
    return sum(komponen_list)


def tampil_tips(tips_list):
    """Mencetak beberapa tips; setiap tips diawali header yang sama."""
    for tip in tips_list:
        print("Tips untuk Programmer:")
        print(tip)


def konversi_kb_ke_mb(kb):
    """Mengonversi Kilobyte ke Megabyte (1 MB = 1024 KB) dan membulatkan 2 desimal."""
    mb = kb / 1024
    return round(mb, 2)


def main():
    print("Selamat datang, calon programmer RPL!")

    kata = "PEMROGRAMAN"
    panjang = panjang_kata(kata)
    print(f"Panjang kata '{kata}' adalah {panjang} karakter.")

    print("Mata Pelajaran RPL:")
    mapel = [
        "Basis Data",
        "Pemrograman Web",
        "Jaringan Komputer",
        "Desain Grafis",
    ]
    for m in mapel:
        print(f"- {m}")

    komponen_nilai = [100, 50, 100]  # contoh komponen sehingga total = 250
    total = total_nilai(komponen_nilai)
    print(f"Total nilai proyek adalah {total}")

    nilai_akhir = 90
    print(f"Nilai akhir Anda adalah {nilai_akhir}")

    print("=====================================================")

    tips = [
        "Jangan pernah berhenti belajar.",
        "Kode yang bersih lebih berharga dari kode yang pintar.",
        "Satu baris komentar bernilai ribuan baris kode.",
        "Jangan takut mencoba hal baru.",
    ]
    tampil_tips(tips)

    print("=====================================================")

    print("Selamat Belajar Bahasa Python!")
    print("Semangat ngoding dengan JavaScript!")
    print("Teruslah berkarya dengan PHP!")

    print("=====================================================")

    kb = 1000
    mb = konversi_kb_ke_mb(kb)
    print(f"{kb} Kilobyte sama dengan {mb} Megabyte")


if __name__ == "__main__":
    main()
