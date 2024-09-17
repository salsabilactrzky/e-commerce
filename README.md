Link deploy PWS: http://salsabila-caturizky-ecommerce.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step:
   Pertama buat project django baru, lalu membuat folder/aplikasi main denfan python manage.py startapp main yang isinya views.py, models.py, urls.py,
lalu routing pada urls.py di project utama menghubungkan aplikasi ke proyek, membuat product dalam models.py serta atribut2nya, lalu membuat fungsi showmain pada views.py
, yg mengirimkan ke template html, menghubungkan routing show_main ke url. Lalu, membuat template main.html, lalu membuat unittest. Lalu, pada awal2
membuat project django saya langsung men-deploy ke PWS terlebih dahulu.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   Client browser --> urls.py --> views.py --> models.py --> templates html --> lalu respon di render
   Client send request  dari browser ke views, lalu views.py ambil data dari model dan mengembalikan hasil dalam bentuk template html

3. skan fungsi git dalam pengembangan perangkat lunak!
   Git berfungsi mengelola versi kode, kolaborasi, dan backup kode. BIsa melacak perubahan kode, membuat project kolaboratif.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  Karena django lebih simple, mudah dipelajari, dan mencakup banyak fungsi. Selain itu, juga karena Django punya banyak fitur bawaan,
seperti routing, ORM. Bahasa pemrograman django juga menggunakan Python, yang mana mudah digunakan untuk pemula.  

5. Mengapa model pada Django disebut sebagai ORM?
   Karena Django berinteraksi dengan database menggunakan python, bukan SQL. Secara otomatis ORM memetakan model python ke tabel database.
  Dengan ORM, pengguna bisa meng-insert, update, delete dengan kode python, tanpa menulis SQL, yang mengurangi risiko kesalahan SQL.
