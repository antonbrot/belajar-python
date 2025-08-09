import calendar
from datetime import date

# Daftar tanggal merah/libur nasional di Indonesia untuk 2025-2026
public_holidays = [
    date(2025, 11, 6),   # Cuti Bersama
    date(2025, 12, 25),  # Christmas
    date(2025, 12, 31),  # Cuti Bersama
    date(2026, 1, 1),    # New Year's Day
    date(2026, 1, 19),   # Idul Fitri 1st day (Misalnya)
    date(2026, 1, 20),   # Idul Fitri 2nd day (Misalnya)
    # Tambahkan libur lainnya di sini sesuai dengan kalender libur nasional Indonesia
]

# Fungsi untuk menghitung jumlah hari kerja (Senin-Jumat) dalam suatu bulan
def count_working_days(year, month, start_week=1):
    days_in_month = calendar.monthrange(year, month)[1]
    working_days = 0
    # Menghitung mulai dari minggu ke-2 (atau start_week yang ditentukan)
    for day in range(1, days_in_month + 1):
        weekday = calendar.weekday(year, month, day)
        if weekday < 5 and (day >= (start_week - 1) * 7 + 1):  # Senin-Jumat, mulai minggu ke-2
            # Cek apakah tanggal tersebut adalah tanggal merah
            if date(year, month, day) not in public_holidays:
                working_days += 1
    return working_days

# Tahun PKL 2025-2026
year_start = 2025
year_end = 2026

# Total hari kerja mulai minggu ke-2 November 2025 sampai Februari 2026
total_working_days = 0

# November 2025, dimulai dari minggu ke-2
november_working_days = count_working_days(2025, 11, start_week=2)
total_working_days += november_working_days

# Desember 2025, penuh
december_working_days = count_working_days(2025, 12)
total_working_days += december_working_days

# Januari 2026, penuh
january_working_days = count_working_days(2026, 1)
total_working_days += january_working_days

# Februari 2026, sampai akhir bulan
february_working_days = count_working_days(2026, 2)
total_working_days += february_working_days

# Hitung total pendapatan
daily_rate = 50000  # per hari kerja
total_income = total_working_days * daily_rate

print(f"Total hari kerja: {total_working_days} hari")
print(f"Total pendapatan: Rp {total_income:,}")
