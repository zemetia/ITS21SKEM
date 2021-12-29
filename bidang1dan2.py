# Jika ada masalah tolong hubungi Mikask#8368

class skem:
    def __init__(self):
        self.penilaian = {"A": 4.0, "AB": 3.5, "B": 3.0, "BC": 2.5, "C": 2.0}
        self.kredit = 1
        self.kredit_kompetisi = {"Jumlah peserta":
                      {"Individu": 1,
                       "2 anggota": 2,
                       "Lebih dari 2 anggota": 3},
                  "skala":
                      {"Institut": 1,
                       "Regional": 2,
                       "Nasional": 3,
                       "Internasional": 4},
                  "Luaran":
                      {"Ide": 1,
                       "Pelaksanaan": 2,
                       "Hasil": 3},
                  "Rentang waktu":
                      {"<3 Bulan": 1,
                       ">3 Bulan": 2,
                       ">6 Bulan": 3},
                  "Bidang Ilmu":
                      {"Tidak berhubungan": 1,
                       "Berhubungan": 2},
                  "Level":
                      {"Kemendikbud": 2,
                       "Non-Kemendikbud": 1}
                  }

    def kompetisi(self):
        na = {"Kompetisi":
                  {"Juara 1": "A",
                   "Juara 2": "AB",
                   "Juara 3": "B",
                   "Juara Harapan/Finalis": "BC",
                   "Peserta": "C"},
              "PKM":
                  {"Peserta PIMNAS": "A",
                   "Proposal didanai": "AB",
                   "Upload proposal ke SIM BELMAWA": "B",
                   "Peserta Liga PKM ITS": "BC",
                   "ToT / Workshop PKM": "C"},
              "Olahraga":
                  {"Juara Kompetisi Olahraga": "A",
                   "Peserta Kompetisi Olahraga": "AB",
                   "Olahraga mengikuti UKM/KONI": "B",
                   "Olahraga mandiri": "BC"}}
        return na

    def magang(self):
        kredit = {"Tempat Magang":
                      {"Perguruan Tinggi": 1,
                       "Pemerintah/Swasta": 2,
                       "BUMN": 3},
                  "Skala":
                      {"Institut": 1,
                       "Nasional": 2,
                       "Internasional": 3},
                  "Rentang Waktu":
                      {"<3 Bulan ": 1,
                       "3-4 Bulan": 2,
                       ">5 Bulan": 3},
                  "Bidang Ilmu":
                      {"Berhubungan": 2,
                       "Tidak berhubungan": 1}}
        na = {"Magang Bersertifikat Kompetensi": "A",
                   "Magang Bersertifikat Industri": "AB",
                   "Magang Bersertifikat non-Industri": "B"}

        return kredit, na

    def wirausaha(self):
        na = {"Omzet > 50 Juta/Tahun": "A",
                   "Omzet 20-50 Juta/Tahun": "AB",
                   "Omzet 5-19,9 Juta/Tahun": "B",
                   "Omzet 2 – 4,9 Juta/Tahun": "BC",
                   "Omzet < 2 Juta/Tahu": "C"
                   }
        kredit = {"Peran":
                      {"Anggota": 1,
                       "Ketua": 2},
                  "Jumlah pelaku":
                      {"Individu": 1,
                       "Tim Mahasiswa ITS": 2},
                  "Badan Hukum":
                      {"Non": 1,
                       "CV": 2,
                       "PT": 3},
                  "Rentang Waktu":
                      {"< 1 Tahun": 1,
                       ">1 Tahun": 2},
                  "Bidang Ilmu":
                      {"Berhubungan": 2,
                       "Tidak berhubungan": 1}}
        return kredit, na

    def organisasi(self):  # ORGANISASI KEPEMIMPINAN DAN MINAT BAKAT
        na = {"Pengurus Inti": "A",
               "Menteri/Kadep": "AB",
               "Anggota Pengurus": "B",
               "Magang": "BC"}
        kredit = {"Skala":
                      {"Departemem": 1,
                       "Fakultas": 2,
                       "Institut": 3},
                  "Rentang Waktu":
                      {"<1 Tahun": 1,
                       ">1 Tahun": 2}}
        return kredit, na

    def kegiatan(self):
        kredit = {"Rentang Waktu":
                           {"<=1 Hari": 1,
                            "2-3 Hari": 2,
                            ">3 Hari": 3},
                       "Posisi":
                           {"Peserta": 1,
                            "Panitia": 2,
                            "Panitia Inti": 3},
                       "Skala":
                           {"Departemem": 1,
                            "Fakultas": 2,
                            "Institut": 3}}
        na = 4
        return kredit, na

    def LKMM(self):
        na = 4
        kredit = {"LKMM":
                      {"LKMM Pra TD": 2,
                      "LKMM TD / LKMW TD": 10,
                      "LKMM TM / LKMW TM": 20,
                      "LKMM TL": 30}}
        return kredit, na

    def questioner(self, dct):
        while True:
            if type(dct) == dict:
                for n, i in enumerate(dct, 1):
                    print(str(n) + ". " + i)

                try:
                    opt = int(input()) - 1
                    if opt < len(dct) and opt >= 0:
                        choice = list(dct)[opt]
                        print(choice)
                        if type(dct[choice]) == dict:
                            self.questioner(dct[choice])
                            break
                        else:
                            if type(dct[choice]) == str:
                                self.na = dct[choice]
                                break
                            elif type(dct[choice]) == int:
                                self.kredit *= dct[choice]
                                break
                except ValueError:
                    pass
            else:
                self.na = dct
                break


    def main(self):
        bidang = [self.kompetisi(), self.magang(), self.wirausaha(), self.organisasi(), self.kegiatan(), self.LKMM()]
        while True:  # Loops if the input is wrong
            try:
                choice = int(input("1. Kompetisi\n2. Magang\n3. Wirausaha\n4. Organisasi\n5. Kegiatan\n6. LKMM\n")) - 1
                if choice < len(bidang) and choice >= 0:
                    break
                else:
                    pass
            except ValueError:
                pass

        if choice != 0:
            kredit, na = bidang[choice]
            print("Nilai Akhir")
            self.questioner(na)
            print("\nKredit")
            for i in kredit:
                self.questioner(kredit[i])
        else:
            na = self.kompetisi()
            self.questioner(na)
            for i in self.kredit_kompetisi:
                self.questioner(self.kredit_kompetisi[i])

        print("Nilai Akhir = ", self.na)
        print("Kredit = ", self.kredit)
        if type(self.na) == int:
            print("Kredit*NA = ", self.kredit*self.na, "\n")
        else:
            print("Kredit*NA = ", self.kredit*self.penilaian[self.na], "\n")
