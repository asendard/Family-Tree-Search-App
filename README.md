# Aplikasi Pencarian Silsilah Keluarga

Aplikasi ini adalah alat bantu untuk menelusuri hubungan keluarga dalam sebuah silsilah. Dengan menggunakan aplikasi ini, Anda dapat mencari jalur hubungan antara dua anggota keluarga, seperti mencari nenek moyang bersama. Aplikasi ini menggunakan dua metode pencarian: **BFS (Breadth-First Search)** dan **A** **(A-Star)**, yang membantu menemukan jalur hubungan dengan cepat dan efisien.

## Apa yang Bisa Dilakukan dengan Aplikasi Ini?

1. **Cari Hubungan Keluarga**:
   - Anda bisa memasukkan nama dua anggota keluarga (misalnya, "Abdul Muthalib" dan "Harits") untuk mencari hubungan di antara mereka.
   - Aplikasi akan menampilkan jalur hubungan, seperti "Abdul Muthalib -> Harits".

2. **Dua Metode Pencarian**:
   - **BFS (Blind Search)**: Metode ini mencari semua kemungkinan hubungan secara sistematis.
   - **A (Heuristic Search)**: Metode ini lebih cerdas dan menggunakan perkiraan untuk menemukan jalur terpendek dengan lebih cepat.

3. **Informasi Tambahan**:
   - Aplikasi juga menampilkan berapa banyak anggota keluarga yang diperiksa (simpul yang dieksplorasi) dan waktu yang dibutuhkan untuk menemukan jalur.

## Teknologi yang Digunakan
- Python
- Streamlit
- MySQL
- Algoritma BFS dan A*

## Cara Menggunakan Aplikasi

1. **Buka Aplikasi**:
   - Jalankan aplikasi dengan mengetik perintah `streamlit run app.py` di terminal.
   - Buka browser dan akses `http://localhost:8501`.

2. **Masukkan Nama Anggota Keluarga**:
     Contoh :
   - Di kolom "Masukkan Anggota Keluarga (Awal)", ketik nama anggota keluarga awal (misalnya, "Abdul Muthalib").
   - Di kolom "Masukkan Anggota Keluarga (Tujuan)", ketik nama anggota keluarga tujuan (misalnya, "Harits").

3. **Pilih Metode Pencarian**:
   - Pilih metode pencarian yang ingin digunakan: **BFS** atau **A***
