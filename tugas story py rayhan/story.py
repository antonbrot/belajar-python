import random

energi = 5
mood = 5
nilai = 70
reputasi = 5
uang = 10
kesehatan = 10

# fungsi pilih sederhana untuk validasi input
def pilih(prompt, opsi):
    while True:
        print("\n" + prompt)
        for i, o in enumerate(opsi, 1):
            print(f"{i}. {o}")
        s = input("👉 Pilih (angka): ").strip()
        if s.isdigit():
            n = int(s)
            if 1 <= n <= len(opsi):
                return n
        print("⚠️ Input tidak valid. Masukkan nomor opsi.")

# fungsi tampil status akhir (sederhana)
def status_akhir():
    print("\n=== 📊 AKHIR HARI ===")
    print(f"⚡ Energi: {energi}   😀 Mood: {mood}   📘 Nilai: {nilai}%")
    print(f"⭐ Reputasi: {reputasi}   💰 Uang: ${uang}   ❤️ Kesehatan: {kesehatan}")

print("=== 🎮 SIMULASI: Sehari di Sekolah ===")
input("🎉 Tekan Enter untuk mulai...")

# pagi
c = pilih("🌅 PAGI: Mau ngapain?", [
    "📚 Masuk kelas tepat waktu",
    "☕ Nongkrong di kantin (bayar)",
    "😴 Tidur sebentar (risiko telat)"
])
if c == 1:
    energi += 1
    print("✅ Masuk tepat waktu. ⚡ Energi +1.")
elif c == 2:
    uang -= 2
    mood += 1
    print("☕ Ngopi di kantin. 😀 Mood +1, 💰 Uang -2.")
else:
    energi -= 1
    if random.random() < 0.5:
        reputasi -= 1
        print("⏰ Kebablasan tidur. Telat! 👎 Reputasi -1.")
    else:
        print("😌 Tidur sebentar tapi masih sempat. ⚡ Energi -1.")

# dikelas
c = pilih("📖 Pelajaran Matematika: apa yang kamu lakukan?", [
    "✍️ Fokus & catat",
    "🤐 Diam saja",
    "📱 Main HP / ngobrol"
])
if c == 1:
    nilai += 3
    energi -= 1
    reputasi += 1
    print("✨ Kamu fokus. 📘 Nilai +3, ⚡ Energi -1, ⭐ Reputasi +1.")
elif c == 2:
    print("😶 Santai di kelas. Tidak ada perubahan.")
else:
    if random.random() < 0.3:
        nilai -= 2
        reputasi -= 1
        print("🚨 Ketahuan main HP! 📘 Nilai -2, ⭐ Reputasi -1.")
    else:
        mood += 1
        print("😂 Ngobrol seru. 😀 Mood +1.")

# jam istirahat
c = pilih("🍔 Istirahat: pilih aktivitas", ["🥟 Beli jajanan", "⚽ Main bola", "📖 Belajar singkat"])
if c == 1:
    uang -= 3
    mood += 1
    if random.random() < 0.05:
        kesehatan -= 2
        print("🤢 Jajan kurang bersih. ❤️ Kesehatan -2.")
    else:
        print("😋 Jajan enak. 😀 Mood +1.")
elif c == 2:
    energi -= 1
    mood += 2
    if random.random() < 0.1:
        kesehatan -= 1
        print("😵 Terpeleset. ❤️ Kesehatan -1.")
    else:
        print("🔥 Main seru. 😀 Mood +2, ⚡ Energi -1.")
else:
    nilai += 2
    energi -= 1
    print("📖 Belajar singkat. 📘 Nilai +2, ⚡ Energi -1.")

# ceritanya kuis dadakan 30 persen
if random.random() < 0.3:
    print("\n-- 📢 Event: Kuis dadakan! --")
    c = pilih("Kuis: apa yang kamu pilih?", ["🧠 Jawab sendiri", "👀 Mencontek"])
    peluang = 0.4 + (energi / 10) * 0.2 + (nilai / 100) * 0.2
    if c == 1:
        if random.random() < peluang:
            nilai += 5
            print("🎉 Jawaban benar! 📘 Nilai +5.")
        else:
            nilai -= 1
            print("❌ Gagal menjawab. 📘 Nilai -1.")
    else:
        if random.random() < 0.5:
            nilai += 3
            print("😎 Mencontek berhasil. 📘 Nilai +3.")
        else:
            nilai -= 5
            reputasi -= 2
            print("🚨 Ketahuan mencontek! 📘 Nilai -5, ⭐ Reputasi -2.")

# setelah sekolah
c = pilih("🏫 Setelah sekolah: apa yang kamu lakukan?", ["🎭 Ikut ekskul", "💼 Kerja paruh waktu", "🏃 Pulang cepat"])
if c == 1:
    energi -= 2
    reputasi += 1
    print("🎭 Ikut ekskul. ⚡ Energi -2, ⭐ Reputasi +1.")
elif c == 2:
    energi -= 2
    uang += 10
    mood -= 1
    print("💼 Kerja paruh waktu. 💰 Uang +10, ⚡ Energi -2, 😀 Mood -1.")
else:
    energi += 2
    mood += 1
    print("🏃 Pulang cepat. ⚡ Energi +2, 😀 Mood +1.")

# malam hari
c = pilih("🌙 Malam: apa yang kamu pilih?", ["📘 Kerjakan PR sekarang", "🎮 Tunda PR & main", "🛌 Tidur awal"])
if c == 1:
    nilai += 2
    energi -= 1
    print("📘 Kerjakan PR. Nilai +2, ⚡ Energi -1.")
elif c == 2:
    mood += 2
    energi -= 1
    nilai -= 1
    print("🎮 Nonton/main. 😀 Mood +2, 📘 Nilai -1.")
else:
    energi += 3
    mood += 1
    print("😴 Tidur awal. ⚡ Energi +3, 😀 Mood +1.")

# status akhir
status_akhir()
print("🎉 Permainan selesai. Terima kasih telah bermain! 🙌")
