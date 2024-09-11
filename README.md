# eshop-pbp: YumYum Bakehouse
Web: http://nadia-rahmadina31-eshoppbp.pbp.cs.ui.ac.id/
http://nadia-rahmadina31-eshoppbp2.pbp.cs.ui.ac.id/
(belum tahu mana link yang akan jalan, masih error karena problem PWS)

Pertanyaan:
1. Bagaimana cara mengimplementasikan checklist step-by-step:
-  Membuat sebuah proyek Django baru: 
Buat repository baru di github, lalu git clone link repo, change directory ke dalam git folder tersebut, dan buat virtual environment dengan:
```
python -m venv venv 
source venv/bin/activate
```
Kemudian mengisi requirements.txt dan menginstallnya.
Lalu buat project django baru dengan:
```
django-admin startproject eshop_pbp
```

- Membuat aplikasi dengan nama main pada proyek tersebut:
Buat aplikasi baru berjudul main dengan menjalankan:
```
python manage.py startapp main
```

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main:
Menambahkan 'main' pada INSTALLED_APPS di dalam settings.py dari proyek eshop_pbp.

- Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib name price description:
Membuat class Product yang menerima input models.Models dan memasang 4 variabel: name dengan input CharField, description dengan input TextField, price dengan input IntegerField, dan production_date dengan input DateField.

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu:
Membuat fungsi dengan context berupa dictionary dengan key appname, name, class, npm, dan value berupa nilai dari masing-masing key. Kemudian fungsi itu akan mereturn fungsi render dari django.shortcuts berisi request, nama template, dan context.

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Membuat file urls.py di dalam aplikasi main, mengimport path dan show_main. Menghubungkan fungsi (dalam kasus ini namanya show_main) dengan menambahkan path('', show_main, name='show_main') pada list urlpatterns di urls.py.

- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Membuat proyek baru di PWS, lalu pada local git project menjalankan command:
```
git remote add pws http://pbp.cs.ui.ac.id/nadia.rahmadina31/eshoppbp
```
Command tersebut akan menghubungkan local git dengan PWS. Kemudian lakukan git add, commit, push pws master.

2.
![alt text](https://github.com/nadiarahmadinaa/eshop-pbp/blob/main/bagan.png)
Ketika client membuat request ke server, aplikasi django akan merefer ke urls.py untuk melihat konten dari adress yang diminta. urls.py kemudian merefer ke fungsi yang berada di views.py. Fungsi tersebut akan memanggil html file yang akan di render serta informasi yang ingin ditampilkan. Informasi yang ditampilkan bisa berupa data dari database yang terhubung melalui models.py, sehingga views.py bisa menggabungkan template html dan data dari models.py.

4. Fungsi git dalam pengembangan perangkat lunak:
- Memudahkan version control atau pelacakan perubahan pada suatu proyek.
- Mempermudah kolaborasi dengan adanya branch untuk memastikan setiap kontribusi tidak bertabrakan dengan kode yang sudah ada.
- Sebagai backup dari suatu proyek, dari versi awal hingga terkini.
- Memudahkan distribusi kode secara publik.

4. Mengapa Django menjadi permulaan pengembangan perangkat lunak:
- Django menggunakan Python, bahasa high-level yang mudah untuk dipelajari dan diterapkan.
- Django memiliki pengguna yang banyak, komunitas luas, dokumentasi baik, sehingga dapat mendukung proses pembelajaran.
- Django memiliki templates yang dapat dipakai sehingga tidak mulai dari nol ketika membangun suatu web application.
- Django memiliki arsitektur yang terstruktur dengan dibedakannya setiap bagian dari aplikasi ke file python yang berbeda.

5. Mengapa model Django disebut ORM:
ORM adalah singkatan Object-Relational Mapper yang memudahkan interaksi dengan database dari kode kita. Django disebut ORM karena memiliki models.py yang berfungsi membuat table pada database dengan nama classnya. Isi dari table tersebut adalah variabel yang terdapat di dalam class. Dengan models, kita tidak perlu memasukkan query ke database secara manual dan bisa langsung dari code kita, sehingga dapat disebut sebuah ORM.
