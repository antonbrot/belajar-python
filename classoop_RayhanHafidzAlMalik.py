class Student:
    def __init__(self, name, year, gpa):
        # atribut: name, year, gpa
        self.name = name
        self.year = year
        self.gpa = gpa

    def update_gpa(self, new_gpa):
        # mengubah nilai GPA
        self.gpa = new_gpa

    def is_honors(self):
        # mengembalikan True jika GPA >= 3.5
        return self.gpa >= 3.5

    def __repr__(self):
        return f"Student(nama={self.name!r}, year={self.year}, gpa={self.gpa})"


#buat 2 objek mahasiswa dan tampilkan datanya
m1 = Student("Daniel Li", 10, 4.0)
m2 = Student("Rina Putri", 17, 3.2)

print("Data dua mahasiswa (menggunakan vars):")
print(vars(m1))
print(vars(m2))
print()

#Method: update_gpa dan is_honors
print("Contoh: update GPA dan cek honors")
print("Sebelum update:", m2)
m2.update_gpa(3.6)
print("Sesudah update:", m2)
print("Apakah m1 honors?", m1.is_honors())
print("Apakah m2 honors?", m2.is_honors())
print()

#Membuat list daftar mahasiswa
daftar_mahasiswa = [
    Student("Budi", 18, 3.2),
    Student("Sari", 19, 3.7),
    Student("Rina", 18, 3.9),
    Student("Andi", 20, 2.9),
    Student("Dewi", 19, 3.5)
]

#mencetak semua mahasiswa
print("Semua mahasiswa:")
for m in daftar_mahasiswa:
    print(m)
print()

#Fungsi untuk mencetak semua mahasiswa yang honors/berprestasi
def cetak_honors(daftar):
    print("Mahasiswa yang honors (GPA >= 3.5):")
    ada = False
    for m in daftar:
        if m.is_honors():
            print(f"- {m.name} (Year {m.year}) - GPA: {m.gpa}")
            ada = True
    if not ada:
        print("Tidak ada mahasiswa yang memenuhi kriteria honors.")

# memanggil fungsi semua mahasiswa yang memenuhi kriteria berprestasi
cetak_honors(daftar_mahasiswa)
