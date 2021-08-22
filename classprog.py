# pengabdian masyarakat
peng_mas = {
    "peran": ["Anggota", "Panitia Inti/Asisten", "Ketua"],
    "pelaksanaan": ["Individu", "Kelompok"],
    "rentang_waktu": ["<1 Bulan", "Sd. 3 Bulan", "Sd. 6 Bulan", "Sd. 1 Tahun"],
    "nilai": [">25 Orang", "Sd. 25 Orang", "Sd. 10 Orang", "Individu"]
}

# Internsionalisasi, Summit, dan Rekognisi
isr = {
    "pelaksanaan": ["Individu", "Kelompok Sd. 3 Orang", "Kelompok >3 Orang", "Pengurus"],
    "tingkat": ["", "Nasional", "Internasional"],
    "disiplin": ["Tidak Berhubungan", "Berhubungan"],
    "rentang_waktu": ["<1 Bulan", "Sd. 3 Bulan", "Sd. 6 Bulan", "Sd. 1 Tahun", ">1 Tahun"],
    "nilai": ["Pembicara/Nama Pertama/Instruktur", "Panitia/Moderator", "Peserta"]
}


class skem:
    def __init__(self):
        # init variable nya
        self.kredit = 1
        self.final = 1
        self.nilai_angka = 1.0
        # ini penilaian yang A,BC gitu laaa owkwokwo:v
        self.penilaian = [["A", 4.0], ["AB", 3.5], ["B", 3.0], ["BC", 2.5], ["C", 2.0]]

    def nilai_skem(self, tipe):
        # tipe ini dictionary dari isi kredit itu
        self.kredit_desc = []
        self.nama_kegiatan = input("nama kegiatan: ")
        for quest in tipe:
            for i in range(len(tipe[quest])):
                # nge print data dari dictionary
                print(i + 1, "=> " + tipe[quest][i])
            x = int(input("=>"))
            if quest != "nilai":
                # jika variabel quest gak "nilai"
                # final itu nilai akhirnya yang NA*kredit
                self.final *= x
                # kredit desc ini isinya data tentang kredit
                self.kredit_desc.append(tipe[quest][x - 1])
                self.kredit = self.final
            else:
                self.final *= self.penilaian[x - 1][1]
                self.nilai_angka = self.penilaian[x - 1][1]
                self.nilai_huruf = self.penilaian[x - 1][0]

    def csv_row(self):
        self.csv = '"' + self.nama_kegiatan + '",' + str(self.kredit) + ',"' + self.nilai_huruf + '",' + str(
            self.nilai_angka) + ',' + str(self.final)
        return self.csv
