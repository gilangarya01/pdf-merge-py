## Merge PDF

Proyek ini adalah aplikasi sederhana yang memanfaatkan dua library Python, yaitu customtkinter untuk antarmuka pengguna dan PyPDF2 untuk manipulasi file PDF. Tujuan utama dari proyek ini adalah menyediakan alat yang digunakan oleh pengguna untuk menggabungkan file-file PDF menjadi satu dengan tampilan antarmuka yang masih sederhana.

##### Teknologi

- Python (customtkinter & PyPDF2)

##### Cara Menggunakan Aplikasi:

- Buat dan aktifkan lingkungan virtual `venv` :
  ```bash
  python -m venv venv
  source venv/bin/activate  # Untuk Windows gunakan: venv\Scripts\activate
  ```
- Instal dependensi dari `requirements.txt` :
  ```bash
  pip install -r requirements.txt
  ```
- Jalankan program `python app.py` dan tekan tombol "Cari Folder" dan pilih folder yang ingin diatur
- Pilih file PDF yang ingin Anda gabungkan dengan menekan tombol "Browser File" untuk setiap file.
- Klik tombol "Merge" untuk memulai proses penggabungan.
- File PDF hasil gabungan akan disimpan pada path yang sudah anda pilih dengan nama `output.pdf`
