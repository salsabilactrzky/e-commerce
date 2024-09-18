**Salsabila Caturizky Farindarmawan
2306275664**

**TUGAS 2**

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



**TUGAS 3**

 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Kita membutuhkan data delivery karena data delivery berfungsi untuk pengiriman informasi antara server dan user. Dengan cara mengubah status pengiriman, sehingga kita dapat mengetahui paket sudah terkirim atau pending. Dengan data delivery, komunikasi antar komponen sistem dapat berjalan lancar, informasi ditampilkan secara realtime, dan performa platform meningkat.
 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    XML dan JSON sama-sama bagus, punya keunggulan sendiri. Namun JSON banyak dianggap lebih baik, karena JSON punya sintaks yang lebih ringkas dan mudah dibaca (key-value, sedangkan XML banyak tag pembuka penutup). Lalu juga karena JSON tersedia di banyak bahasa pemrograman dan framewirk, ukurannya pun lebih kecil karena tidak pakai tag2 panjang, sehingga pengiriman datanya lebih cepat.
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    method is_valid() berfungsi untuk memvalidasi data yang dikirimkan melalui form, sebelum diproses lebih lanjut dan disimpan ke database. Method is_valid() pada views memastikan data yang diinput memenuhi kriteria pada form atau models. Kita butuh method ini karena method ini menjaga keamanan data, mencegah masuknya data invalid. 
 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    Kita membutuhkan csrf_token karena ini merupakan keamanan yang melindungi web dari serangan CSRF. CSRF merupakan serangan yang memanfaatkan kredensial pengguna yang sudah login untuk disalahgunakan. Token ini disertakan di tiap permintaan form dan hanya dihasilkan dan divalidasi server, sehingga mencegah penyerang membuat permintaan palsu atas nama pengguna. Tanpa csrf_token, penyerang dapat mengeksploitasi web dengan membuat pengguna mengirim permintaan berbahaya yang memodifikasi data tak diinginkan. Dengan token ini, server dapat memverifikasi apakah setiap permintaan berasal dari sumber yang sah, meningkatkan keamanan web.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Pertama membuat base.html terlebih dahulu di dalam folder templates yang root direktori, sebagai kerangka atau template dasar webnya, dan tambahin DIRS di settings.py. Lalu sesuaikan main.html nya karena template dasarnya sudah pakai dari base.html.
    2. Tambahin id di models.py pakai uuid
    3. Buat form di forms.py di dalam direktori main utuk menambahkan objek, import modelform dan model, lalu buat view di views.py untuk tampilkan dan proses form. Lalu membuat template untuk formnya, pada file create_product.html di folder templates, dan menambhakan url routing di urls.py untuk akses view form.
    4. Lalu menambahkan 4 fungsi views baru untuk melihat objek dalam format XML, JSON, XML by ID, dan JSON by ID. Menambahkan fungsi show_xml dan show_json dalam views.py untuk menampilkan objek dalam format xml dan json. Menambahkan lagi fungsi show_xml_by_id dan show_json_by_id dalam views.py untuk menampilkan objek sesuai parameter id nya. Lalu routing url menambahkan path tiap views.
  
6. Screenshot Postman
   Postman XML:
   ![postman_xml](https://github.com/user-attachments/assets/5ed22383-b1c5-4891-87d6-5370f588f577)
   Postman JSON:
   ![postman_json](https://github.com/user-attachments/assets/7c90829c-40a1-4248-9e72-93069e0dbd24)
   Postman XML by id:
   ![postman_xmlid](https://github.com/user-attachments/assets/a5f70a75-d605-41f4-bd3b-a17d8fbafc92)
   Postman JSON by id:
   ![postman_jsonid](https://github.com/user-attachments/assets/b435f2e6-7f98-4711-8467-f9528cc1b006)
