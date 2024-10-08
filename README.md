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



**TUGAS 4**

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
   HttpResponseRedirect() dan redirect() berfungsi untuk mengarahkan pengguna ke URL yang berbeda. redirect() lebih sederhana dan fleksibel. Karena, selain mengarahkan ke URL, bisa juga mengarahkan ke nama view yang didefiniaikan di urls.py, dan objek model. Sedangkan, HttpResponseRedirect() hanya digunakan untuk mengarahkan ke URL tertentu, URL tujuan harus disebutkan secara eksplisit dengan string. HttpResponseRedirect() juga bisa mengarahkan ke nama view, tetapi harus menggunakan reverse() untuk mencari URL dari nama view tsb.

2. Jelaskan cara kerja penghubungan model Product dengan User!
   Caranya dengan menggunakan ForeignKey dari model User, menambahkan field user, jadi tiap produk hanya dimiliki satu pengguna, dan tiap pengguna bisa memiliki banyak produk. ForeignKey(User, on_delete=models.CASCADE) menunjukkan setiap entri produk terhubung dengan satu pengguna. Jika pengguna dihapus, semua produk dari  pengguna tersebut juga akan dihapus. Lalu menghubungkan produk baru dengan pengguna yang sedang login dengan request.user. product.user = request.user menghubungkan produk yang dibuat dengan pengguna yang sedang login. Lalu juga hanya menampilkan daftar pproduk yang dimiliki pengguna yang sedang login dengan cara filter query database, Product.objects.filter(user=request.user).

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
   Authentication adalah proses verifikasi identitas pengguna. Aplikasi memeriksa apakah username dan password pengguna cocok dengan yang di database. Sedangkan, Authorization adalah proses menentukan hak akses pengguna. Apakah pengguna yang telah terautentikasi memiliki izin untuk melakukan suatu tindakan atau mengakses halaman tertentu.
   Saat pengguna login, proses autentikasilah yang dilakukan.
   Saat pengguna login, Django melakukan autentikasi dengan memverifikasi apakah username dan password cocok dengan yang di database dengan authenticate(). Jika berhasil, Django membuat session untuk pengguna dan menyimpan sebagai cookie di browser pengguna. Setelah terautentikasi, Django mengatur authorization untuk menentukan halaman yang bisa diakses pengguna dengan menggunakan decorator @login_required, yang memastikan pengguna hanya bisa mengakses halaman tertentu jika mereka sudah login.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
   Django mengingat pengguna yang telah login dengan menggunakan session. Setelah pengguna berhasil login, Django membuat sebuah session dan menyimpannya di cookies browser pengguna. Cookies berisi session ID yang digunakan untuk mengenali pengguna setiap melakukan request baru. Session ID nantinya dicocokkan dengan informasi di server untuk memastikan bahwa pengguna telah terautentikasi.
   Kegunaan lain dari cookies antara lain, menyimpan preferensi pengguna, melacak sesi belanha di e-commerce, juga menganalisis perilaku pengguna. Tidak semua cookies aman digunakan, cookies yang tak dienkripsi atau yang tidak punya masa expired dapat disalahgunakan. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   Untuk Mengimplementasikan fungsi registrasi, login, dan logout. Di dalam views.py, saya menambahkan fungsi register() yang menggunakan UserCreationForm yang menampilkan form registrasi dengan GET, dan menyimpan data pengguna dengan POST. Lalu, saya juga membuat file register.html.
   Lalu, saya menambahkan fungsi login_user() yang menggunakan AuthenticationForm, menangani autentikasi pengguna. Lalu, juga membuat file login.html
   Untuk logout, saya menambahkan fungsi logout_user() dengan django.contrib.auth.logout, menghapus session pengguna yang sedang login. Memodifikasi main.html juga untuk button logout. Lalu, routing menambahkan path reigster, login, logout di urls.py. Selain itu, juga merestriksi akses halaman main, dengan menggunakan decorato @login_required.
   Lalu menggunakan cookies untuk last login dan menampilkan informasi pengguna yang login dengan memodifikasi views.py set_cookie last_login, di show_main views.py juga menambhakn 'last_login': request.COOKIES.get('last_login') pada context, di fungsi log_out_user juga menambahkan delete_cookie. Lalu menampilkan last_login pada main.html, dan saya juga menambahkan name pada context, untuk menampilkan nama pengguna.
   Menghubungkan Model Product dengan User
   Di dalam models.py Product saya menambahkan ForeignKey ke model User yang menghubungkan produk dengan sang pengguna. Menggunakan request.user di fungsi create_product() untuk memastikan produk yang dibuat terhubung dengan pengguna yang sedang login. Lalu menggunakan filter request.user untuk menampilkan produk di halaman utama.
   Lalu untuk 2 user dan 3 dummy, saya menambahkannya langsung melalui Django Admin http://localhost:8000/

6. 2 User dengan 3 Dummy Product
   ![Alt text](<Screen Shot 2024-09-25 at 11.23.54.png>)
   ![Alt text](<Screen Shot 2024-09-25 at 11.24.21.png>)


**TUGAS 5**

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
   Inline styles (atribut style) memiliki prioritas tertinggi. Lalu, ID selectors (#id) memiliki prioritas lebih tinggi dibandingkan class atau tag. Selanjutnya, Class selectors, attribute selectors, dan pseudo-classes. Setelah itu, Element selectors seperti div atau p. Lalu prioritas terendah adalah Universal selector dan inheritance. Jika terdapat selector dengan tingkat specificity yang sama, selector yang didefinisikan terakhir di dalam stylesheet akan diterapkan  (cascading).
 
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
   Karena, dengan Responsive Design, aplikasi web dapat disesuaikan dengan ukuran layar berbeda (desktop, mobile). Ini penting karena pengguna dapat mengakses web dari berbagai perangkat dengan ukuran layar yang bervariasi, namun tampilan & performa web harus tetap optimal. Tanpa responsive design, aplikasi web dapat terlihat buruk atau tidak berfungsi dengan baik di perangkat tertentu. Contoh aplikasi yang sudah menerapkan Responsive Design: Google, Youtube, Netflix, Shopee. Sedangkan aplikasi yang belum menerapkan Responsive Design mungkin seperti aplikasi yang sudah tua, yang banyak content statis tanpa element interaktif, lalu web yang didesign hanya untuk desktop, teks dan gambarnya terlalu besar atau kecil.
 
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
   Margin adalah jarak ruang di luar elemen.
   Border adalah garis di sekitar konten elemen.
   Padding adalah ruang di dalam elemen, jarak antara konten dan border.
   Implementasiannya, margin: 20px; border: 2px solid black; padding: 10px;.
 
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
   Flex box adalah model layout satu dimensi (baris atau kolom) yang digunakan untuk mengatur tata letak elemen dalam satu arah secara horizontal atau vertikal.
   Grid layout adalah model layout dua dimensi (baris dan kolom) yang digunakan untuk membuat tata letak yang lebih kompleks dengan menggunakan baris dan kolom. Grid cocok untuk design halaman web yang punya banyak komponen.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
   Untuk CSS ssaya menggunakan Tailwind, saya menyambungkan tailwind dengan template django di base.html. 
   Saya menambahkan fitur Edit dan Delete Produk dengan membuat fungsi2nya di views.py, membuat file html, routing urls.py, dan menambahkan tombol buttonnya di main.html.
   Lalu saya mendekorasi design halaman web, dengan menambahkan navigation bar. Saya membuat file htmlnya, lalu menautkan navbar ke file html lainnya. Saya juga mengatur settings untuk konfigurasi static files. Lalu saya mendesign halaman web dengan css tailwind di global.css, design untuk halaman login, register, dan main. Juga menggunakan Flexbox dan Grid Layout untuk menyesuaikan tampilan di semua ukuran layar.



**TUGAS 6**
1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
   JavaScript memungkinkan penambahan elemen interaktif (tombol, animasi, validasi). Lalu, dengan AJAX dapat memperbarui konten secara asinkron tanpa refresh seluruh halaman. Mengontrol elemen HTML atau CSS secara langsung sehingga pengalaman client lebih responsif. Lalu, menjalankan kode juga di browser client sehingga respon aplikasi lebih cepat.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
   await pada fetch() berfungsi untuk menghentikan eksekusi code selanjutnya sampai request fetch selesai. Jadi, await memastikan data yang diambil sudah siap sebelum lanjut ke langkah berikutnya.
   
   Jika tidak menggunakan await, program akan langsung lanjut eksekusi code selanjutnya tanpa menunggu hasil fetch(). Yang mana dapat menimbulkan error, karena program mencoba menggunakan data yang belum tersedia.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
   Karena csrf_exempt menonaktifkan pemeriksaan token CSRF (Cross-Site Request Forgery) di Django. Ini diperlukan ketika request AJAX POST tidak menyertakan token CSRF, yang mana requestnya akan ditolak oleh Django.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
   Karena validasi di frontend dapat dilewati pengguna dengan mematikan JavaScript atau modifikasih HTML melalui browser. Aplikasi menjadi rentan terhadap serangan (XSS atau injection). Pembersihan di backend memastikan data yang disimpan di server aman.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
   Saya menambahkan message error (invalid username or password) pada login, lalu saya pakai AJAX POST untuk menabmahkan produk baru dengan membuat fungsi addProduct di main.html yang mengirimkan data produk ke endpoint add_prodcut_ajax. Lalu routing add_product_ajax di urls.py. Setelah itu, menggunakan AJAX GET untuk menampilkan data produk pakai fetch dan buat fungsi getProducts dan refreshProducts. Lalu, membuat modal dengan Tailwind untuk form input. Setelah itu juga menambhakan validasi backend dengan fungsi strip_tags ysng melindingi dari XSS, menggunakan DOMPurify di frontend untuk membersihkaN data produk yang diambil API sebelum ditampilkan di halaman web.