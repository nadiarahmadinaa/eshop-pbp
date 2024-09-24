# eshop-pbp: YumYum Bakehouse
Web: http://nadia-rahmadina31-eshoppbp.pbp.cs.ui.ac.id/
http://nadia-rahmadina31-eshoppbp2.pbp.cs.ui.ac.id/
(belum tahu mana link yang akan jalan, masih error karena problem PWS)

## Tugas 2 Pertanyaan:
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

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py:
Membuat file urls.py di dalam aplikasi main, mengimport path dan show_main. Menghubungkan fungsi (dalam kasus ini namanya show_main) dengan menambahkan path('', show_main, name='show_main') pada list urlpatterns di urls.py.

- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet:
Membuat proyek baru di PWS, lalu pada local git project menjalankan command:
```
git remote add pws http://pbp.cs.ui.ac.id/nadia.rahmadina31/eshoppbp
```
Command tersebut akan menghubungkan local git dengan PWS. Kemudian lakukan git add, commit, push pws master.

2.
![alt text](https://github.com/nadiarahmadinaa/eshop-pbp/blob/main/bagan.png)

Ketika client membuat request ke server, aplikasi django akan merefer ke urls.py untuk melihat konten dari adress yang diminta. urls.py kemudian merefer ke fungsi yang berada di views.py. Fungsi tersebut akan memanggil html file yang akan di render serta informasi yang ingin ditampilkan. Informasi yang ditampilkan bisa berupa data dari database yang terhubung melalui models.py, sehingga views.py bisa menggabungkan template html dan data dari models.py. Kemudian, tampilan yang telah dipanggil oleh views.py akan dikirim ke server dan ditampilkan ke client sebagai response.

4. Fungsi git dalam pengembangan perangkat lunak:
- Memudahkan version control atau pelacakan perubahan pada suatu proyek.
- Mempermudah kolaborasi dengan adanya branch untuk memastikan setiap kontribusi tidak bertabrakan dengan kode yang sudah ada.
- Sebagai backup dari suatu proyek, dari versi awal hingga terkini.
- Memudahkan distribusi kode secara publik.

4. Mengapa Django menjadi permulaan pengembangan perangkat lunak:
- Django menggunakan Python, bahasa high-level yang mudah untuk dipelajari dan diterapkan.
- Django memiliki pengguna yang banyak, komunitas luas, dokumentasi baik, sehingga dapat mendukung proses pembelajaran.
- Django memiliki templates yang dapat dipakai sehingga tidak mulai dari nol ketika membangun suatu web application.
- Django memiliki arsitektur yang terstruktur dengan dipisahnya setiap bagian dari aplikasi ke file python yang berbeda.

5. Mengapa model Django disebut ORM:
ORM adalah singkatan Object-Relational Mapper yang memudahkan interaksi dengan database dari kode kita. Django disebut ORM karena memiliki models.py yang berfungsi membuat table pada database dengan nama classnya. Isi dari table tersebut adalah variabel yang terdapat di dalam class. Dengan models, kita tidak perlu memasukkan query ke database secara manual dan bisa langsung dari code kita, sehingga dapat disebut sebuah ORM.

## Tugas 3 Pertanyaan:
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery penting dalam pengimplementasian suatu platform karena akan memudahkan dan meningkatkan efisiensi pertukaran data antar aplikasi, platform, atau sistem dalam bentuk yang terstandardisasi. 

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih populer dan lebih baik dibandingkan XML karena:
- Format yang lebih simple dan fleksibel sehingga mudah dibaca oleh manusia dan diparsing oleh mesin
- Ukuran JSON yang lebih kecil dibandingkan XML karena terdapat lebih banyak karakter seperti tags pada XML
- Karena simpel, kecil, mudah diparsing, dan fleksibel, JSON lebih cepat dan mudah untuk digunakan di berbagai aplikasi

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memvalidasi data seperti tipe data dan ada atau tidaknya data. Method ini diperlukan untuk menghindari error pada sistem dengan adanya data yang tidak valid atau kosong. Dengan method ini, user akan diberikan feedback terkait data inputnya yang masih salah.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token diperlukan dalam form untuk menghindari adanya action dari user yang tidak terautentikasi. Tanpa csrf_token, user di luar autentikasi website bisa membuat POST request terhadap aplikasi sesukanya. Dengan demikian, penyerang bisa mengubah data, menambahkan data, menghilangkan data, bahkan memasukkan file atau payload berbahaya.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
-  Membuat input form untuk menambahkan objek model pada app sebelumnya
Kita edit dahulu objek modelnya untuk memiliki id yang di generate secara otomatis dan tidak bisa diubah dengan uuid:
```
import uuid # Tambahkan import di atas models.py
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # Tambahkan baris ini di dalam class Product

```
Kemudian buat input form dengan forms.py di dalam main:
```
from django.forms import ModelForm
from main.models import Product

class FreshBakesForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]
```
Buat laman htmlnya di create_fresh_bakes_entry.html:
```
<h1>Add New Fresh Bakes</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Fresh Bakes" />
      </td>
    </tr>
  </table>
</form>
```
Tambahkan laman tersebut ke urlpatterns di dalam urls.py:
```
path('create_fresh_bakes_entry', create_fresh_bakes_entry, name='create_fresh_bakes_entry'),
```
Buat routenya di views.py juga:
```
def create_fresh_bakes_entry(request):
    form = FreshBakesForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_fresh_bakes_entry.html", context)
```
Edit fungsi main juga untuk menampilkan fresh bakes:
```
def show_main(request):
    fresh_bakes = Product.objects.all()
    context = {
        'appname' : 'YumYum Bakeshop',
        'name': 'Nadia Rahmadina Aristawati',
        'class': 'PBP D',
        'npm': '2306207972',
        'fresh_bakes': fresh_bakes
    }

    return render(request, "main.html", context)
```
Dan terakhir menambahkan baris-baris berikut di akhir main.html untuk membuat bakes baru dan menampilkan bakes yang ada dalam suatu tabel:
```
<a href="{% url 'main:create_fresh_bakes_entry' %}">
    <button>Add New Fresh Bakes</button>
  </a>
{% if not fresh_bakes %}
<p>No fresh bakes yet.</p>
{% else %}
<table>
  <tr>
    <th>Fresh Bakes Name</th>
    <th>Description</th>
    <th>Price</th>
    <th>Production Date</th>
  </tr>
 
  {% for bakes in fresh_bakes %}
  <tr>
    <td>{{bakes.name}}</td>
    <td>{{bakes.description}}</td>
    <td>{{bakes.price}}</td>
    <td>{{bakes.production_date}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}
```

- Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Melakukan import HttpResponse dan serializers, serta menambahkan 4 fungsi views tersebut:
```
from django.http import HttpResponse
from django.core import serializers
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Menambahkan baris-baris berikut ke dalam urlpatterns di urls.py:
```
path('json/', show_json, name='show_json'),
path('xml/', show_xml, name='show_xml'),
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```

6. Akses URL untuk XML, JSON, XML by ID, dan JSON by ID:
- XML:
![alt text](https://github.com/nadiarahmadinaa/eshop-pbp/blob/main/xml.png)
- JSON:
![alt text](https://github.com/nadiarahmadinaa/eshop-pbp/blob/main/json.png)
- XML by ID:
![alt text](https://github.com/nadiarahmadinaa/eshop-pbp/blob/main/xmlid.png)
- JSON by ID:
![alt text](https://github.com/nadiarahmadinaa/eshop-pbp/blob/main/jsonid.png)

## Tugas 4 Pertanyaan:
1.  Apa perbedaan antara HttpResponseRedirect() dan redirect()

HttpResponseRedirect() hanya menerima input berupa url, sedangkan redirect() lebih fleksibel dan bisa menerima input model, view, maupun url.

2.  Jelaskan cara kerja penghubungan model Product dengan User!
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Dengan membuat relasi ForeignKey ke model User. ForeignKey memungkinkan satu Product dikaitkan ke satu User, tapi seorang User bisa memiliki banyak Product.
on_delete=models.CASCADE untuk mengkonfigurasi ketika User dihapus, semua Product yang terkait dengannya juga dihapus.

3.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication adalah proses untuk memverifikasi identitas pengguna, layaknya dalam proses login. Authorization adalah proses untuk memverifikasi apakah pengguna yang telah terautentikasi memiliki izin untuk mengakses atau melakukan tindakan tertentu.
Django mengimplementasikan autentikasi melalui authenticate(), dan login():
```
from django.contrib.auth import authenticate, login
```
Django mengimplementasikan authorization melalui decorators @permission_required atau is_authenticated:
```
from django.contrib.auth.decorators import login_required

@login_required
def logged_in_users_only(request):
```

4.  Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django bisa mengingat pengguna yang telah login dengan session ID di cookies. Cookies bisa menyimpan informasi lain seperti preferensi, items yang terikat kepada user logged-in seperti barang di keranjang, detail login, halaman website yang telah divisit, dan lain sebagainya. 
Cookies sendiri tidak berbahaya, namun data di dalam cookies bisa mengandung informasi sensitif. Selain itu, jika website rentan terhadap cross-site scripting (XSS), ada kemungkinan cookies kita dicuri dan digunakan oleh attacker untuk mengautentikasi diri mereka sebagai kita dan mendapatkan hak akses kita.

5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- Membuat registration form bagi User dengan UserCreationForm yang diimplementasikan di dalam function register dalam views.py
- Mengimplementasikan AuthenticationForm pada function login_user dalam views.py untuk autentikasi login seorang user
- Menghubungkan register dengan register.html, login_user dengan login.html melalui fungsi render
- Menghubungkan logout_user dengan main menu melalui HttpResponseRedirect
- Membuat path url untuk register, login, dan logout di urlpatterns dalam urls.py dari main

- [x] Menghubungkan model Product dengan User.
- Mengimport User pada models.py, lalu tambahkan variabel user pada model Product sebagai berikut 
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
- Mengambil data user melalui request.user saat suatu POST form terkirim untuk membuat model Product, dan menghubungkannya dengan Product yang dibuat.
- Agar data hanya bisa dilihat oleh User yang memilikinya, pastikan dengan melakukan filter data
```
fresh_bakes = Product.objects.filter(user=request.user)
```


- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
- Melakukan registrasi untuk 2 user berbeda
- Login ke akun masing-masing user
- Create Fresh Bakes sebanyak 3 kali dengan 3 Product berbeda
- Cek ulang pada main page, memastikan bahwa data hanya visible terhadap diri sendiri dan seluruh data yang dimiliki ditampilkan dengan baik.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
- Membuat context nama dari main page dinamis sesuai user yang logged in dengan mengubah name sebagai berikut
```
'name': request.user.username,
```
- Melakukan set cookie sesuai jam login ketika form login valid dengan command
```
response.set_cookie('last_login', str(datetime.datetime.now()))
```
- Memastikan bahwa cookies last login ini dihapus ketika user log out
```
response.delete_cookie('last_login')
```