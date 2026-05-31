buatkan saya website sederhana uji kualitatif pereaksi kimia organik, isinya bisa dibuat seperti aplikasi edukasi dan identifikasi senyawa organik. Karena tujuan utamanya membantu pengguna mengenali golongan senyawa berdasarkan hasil pengujian. kayak begini kurang lebihnya tapi tolong disempurnakan
# 1. Halaman Awal (Landing Page)
Berisi:
* Judul Website
  > Sistem Identifikasi Senyawa Organik Berdasarkan Uji Kualitatif
* Deskripsi singkat
  > Website ini membantu mengidentifikasi golongan senyawa organik berdasarkan hasil pengujian laboratorium seperti uji kelarutan, uji bromin, uji Baeyer, uji Tollens, dan lainnya.
* Tombol:
  * Mulai Identifikasi
  * Materi Uji Organik
  * Tentang Website
---
# 2. Halaman Menu Utama
Terdapat beberapa menu:
### A. Identifikasi Senyawa
Pengguna menjawab pertanyaan berdasarkan hasil praktikum.
Contoh:
*Apakah sampel larut dalam air?*
* Ya
* Tidak
*Apakah terjadi perubahan warna pada uji bromin?*
* Ya
* Tidak
*Apakah terbentuk cermin perak pada uji Tollens?*
* Ya
* Tidak
Setelah semua pertanyaan dijawab:
### Output
Kemungkinan sampel termasuk:
* Alkohol
* Aldehid
* Keton
* Fenol
* Asam Karboksilat
* Ester
* Alkena
* Alkuna
* Karbohidrat
* Protein
Beserta penjelasannya.
---
### B. Materi Uji Kualitatif
Berisi teori singkat.
Contoh:
## Uji Bromin
Tujuan:
Mendeteksi ikatan rangkap.
Prinsip:
Larutan bromin akan kehilangan warna coklat kemerahan jika bereaksi dengan senyawa tak jenuh.
Reaksi:
Alkena + Br₂ → Dibromoalkana
Hasil Positif:
* Warna bromin hilang.
Hasil Negatif:
* Warna tetap.
---
## Uji Baeyer
Tujuan:
Mendeteksi ketidakjenuhan.
Pereaksi:
KMnO₄ encer.
Hasil Positif:
* Warna ungu hilang.
* Terbentuk endapan coklat MnO₂.
---
## Uji Tollens
Tujuan:
Identifikasi aldehid.
Pereaksi:
[Ag(NH₃)₂]⁺
Hasil Positif:
* Terbentuk cermin perak.
---
# 3. Database Senyawa
Contoh tabel:
| Senyawa     | Rumus    | Golongan         | Uji Positif  |
| ----------- | -------- | ---------------- | ------------ |
| Etanol      | C₂H₅OH   | Alkohol          | Esterifikasi |
| Aseton      | CH₃COCH₃ | Keton            | 2,4-DNPH     |
| Formaldehid | HCHO     | Aldehid          | Tollens      |
| Asam Asetat | CH₃COOH  | Asam Karboksilat | Lakmus       |
Pengguna dapat mencari nama senyawa.
---
# 4. Simulasi Praktikum
Misalnya:
Pilih sampel:
* Etanol
* Benzena
* Aseton
* Formaldehid
Pilih uji:
* Bromin
* Tollens
* Baeyer
Kemudian website menampilkan:
### Hasil Simulasi
Sampel: Formaldehid
Uji Tollens:
✔️ Terbentuk cermin perak
Kesimpulan:
Sampel mengandung gugus aldehid.
---
# 5. Kuis
Contoh:
*Suatu senyawa memberikan hasil positif pada uji Tollens tetapi negatif pada uji Iodoform. Golongan senyawa tersebut adalah?*
* Alkohol
* Aldehid ✅
* Ester
* Fenol
Nilai langsung muncul.
 tampilan ui nya menggunakan html dan css, pake python
