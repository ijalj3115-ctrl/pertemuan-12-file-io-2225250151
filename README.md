Pertemuan 12 - File I/O dan Error Handling

Nama: Rijal Munawarudin
NIM: 2225250151
Kelas: 3F

Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

Format File Input

File "data/nilai.txt" menggunakan format "NIM,nilai".

Contoh:

A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88

Cara Menjalankan

Jalankan program melalui terminal VS Code dari folder utama proyek.

python tugas/rekap_nilai_file.py

Jika tidak berhasil, gunakan "python3 tugas/rekap_nilai_file.py".

Error yang Ditangani

- "FileNotFoundError": terjadi ketika file input tidak ditemukan.
- "ValueError": terjadi ketika nilai tidak dapat dikonversi menjadi angka atau format baris tidak sesuai.

Test Case

Kasus| Kondisi| Hasil yang Diharapkan
Normal| Semua baris valid| Semua data diproses dan rekap benar.
File hilang| File "nilai.txt" tidak tersedia| Pesan file tidak ditemukan; program tidak crash.
Nilai invalid| "A004,abc"| Baris invalid dilewati; data lain tetap diproses.
Baris kosong| Ada baris kosong| Baris kosong dilewati.
Batas lulus| Nilai 60| Nilai 60 dihitung sebagai lulus.

Refleksi

Melalui praktikum ini, saya mempelajari cara membaca, menulis, dan mengolah data file menggunakan Python. Saya juga memahami penggunaan mode "r", "w", dan "a", serta fungsi "strip()" dan "split()" untuk memproses data. Selain itu, saya mempelajari penggunaan "try-except" untuk menangani "FileNotFoundError" dan "ValueError" agar program dapat memberikan pesan kesalahan yang jelas dan tetap memproses data valid lainnya.