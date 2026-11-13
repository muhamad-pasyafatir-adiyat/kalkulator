Latihan Mandiri 1:
Saat menggunakan git add -p dan memilih 'y' pada komentar pertama serta 'n' pada komentar kedua:
- Keluaran git diff hanya menampilkan komentar kedua karena masih berada di working directory (belum di-stage).
- Keluaran git diff --staged hanya menampilkan komentar pertama karena sudah masuk ke staging area.

Latihan Mandiri 2:
Setelah menambahkan venv/ dan *.tmp ke dalam .gitignore lalu membuat file coba.tmp, hasil git status menunjukkan bahwa file coba.tmp tidak muncul sebagai untracked file. Ini membuktikan pola .gitignore sudah bekerja mengabaikan file berakhiran .tmp.

Latihan Mandiri 3:
Perintah git diff HEAD~3 HEAD --stat menampilkan ringkasan statistik perubahan file antara 3 commit sebelumnya (HEAD~3) dengan commit terakhir saat ini (HEAD). Keluarannya berisi daftar nama file yang berubah, jumlah baris yang diubah pada tiap file (tanda + untuk penambahan dan - untuk penghapusan), serta total keseluruhan file dan baris yang berubah di baris paling bawah.