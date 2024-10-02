# eshop-pbp: YumYum Bakehouse
Web: http://nadia-rahmadina31-eshoppbp.pbp.cs.ui.ac.id/

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
- Menjalankan ```python manage.py runserver```
- Melakukan registrasi untuk 2 user berbeda pada localhost
- Login ke akun masing-masing user
- Create Fresh Bakes sebanyak 3 kali dengan 3 Product berbeda
- Cek ulang pada main page, memastikan bahwa data hanya visible terhadap diri sendiri dan seluruh data yang dimiliki ditampilkan dengan baik.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
- Membuat context nama dari main page dinamis sesuai user yang logged in dengan mengubah name sebagai berikut pada views.py show_main() bagian context
```
'name': request.user.username,
```
- Melakukan set cookie pada views.py login_user() sesuai jam login ketika form login valid dengan command
```
response.set_cookie('last_login', str(datetime.datetime.now()))
```
- Memastikan bahwa cookies last login ini dihapus ketika user log out di views.py logout_user()
```
response.delete_cookie('last_login')
```

## Tugas 5 Pertanyaan:
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan prioritas CSS selector dari most hingga least priority:
- Inline CSS
- ID selector
- Class, pseudo-class, attribute selector
- Tag selector / element
- Universal selector

Dengan beberapa aturan sebagai berikut:
- ```!important``` akan selalu didahulukan di atas segalanya
- Jika ada 2 rule dengan derajat yang sama, yang muncul belakangan akan diprioritaskan
- Selector yang lebih spesifik akan didahulukan dibandingkan yang kurang spesifik


2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design penting karena dengannya, aplikasi akan tampil dengan baik di berbagai perangkat dan ukuran screen sehingga memberi pengalaman yang baik pula bagi penggunanya.

Contoh web dengan design responsive:
```https://www.jakarta.go.id/```

Contoh web dengan design tidak responsive:
```https://tni-ad.mil.id/```


3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

- Margin: ruang di luar elemen yang memisahkan elemen tersebut dengan elemen lain di sekitarnya. Contoh penerapannya:
```
div {
  margin: 20px;
}
```
- Border: garis yang mengelilingi elemen dan memisahkan konten elemen dari margin. Contoh penerapannya:
```
div {
  border: 2px solid black;
}
```
- Padding: ruang tambahan di dalam elemen antara konten elemen dan bordernya. Contoh penerapannya:
```
div {
  padding: 20px;
}
```

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

- Flex box layout: metode menyusun elemen dalam satu dimensi (baris atau kolom). Dalam satu alignment, misal baris, kolomnya tidak ikut dibagi secara merata melainkan dapat memperbesar atau memperkecil content sesuai dengan ruang yang tersisa. 

Kegunaan: navigation bar yang responsif, dimana akan berupa menu horizontal pada desktop dan vertikal pada mobile.

- Grid layout: metode menyusun elemen dengan membagi suatu webpage menjadi 12 kolom secara merata. Kolom ini dapat dibagi lagi menjadi baris dan kolom, sehingga grid layout ini menyusun elemen dalam dua dimensi.

Kegunaan: menampilkan cards seperti pada proyek ini, dengan rapih dan tersusun dalam 2 dimensi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Implementasikan fungsi untuk menghapus dan mengedit product.

Tambahkan function untuk edit dan delete di views.py dalam main:
```
def edit_fresh_bakes(request,id):
    fresh_bakes = Product.objects.get(pk=id)
    form = FreshBakesForm(request.POST or None, instance=fresh_bakes)
    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_fresh_bakes.html", context)

def delete_fresh_bakes(request, id):
    fresh_bakes = Product.objects.get(pk=id)
    fresh_bakes.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
Kemudian buat htmlnya juga untuk edit dan delete cards, dan tambahkan button atau hyperlink pada main.html untuk menuju ke opsi delete dan edit ini. Import function dari  views.py dan tambahkan pada urlpatterns di urls.py dari direktori main.

- Kustomisasi halaman login, register, dan tambah product semenarik mungkin. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive.

Tambahkan kustomisasi berupa tailwind css login, register, add product, dan main html:
Login:
```
<div class="min-h-screen flex items-center justify-center w-screen bg-orange-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-orange-900">
        Welcome bakers! Login here
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST" action="">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        <div>
          <label for="username" class="sr-only">Username</label>
          <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-orange-300 placeholder-orange-500 text-orange-900 rounded-t-md focus:outline-none focus:ring-rose-500 focus:border-rose-500 focus:z-10 sm:text-sm" placeholder="Username">
        </div>
        <div>
          <label for="password" class="sr-only">Password</label>
          <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-orange-300 placeholder-orange-500 text-orange-900 rounded-b-md focus:outline-none focus:ring-rose-500 focus:border-rose-500 focus:z-10 sm:text-sm" placeholder="Password">
        </div>
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-rose-600 hover:bg-rose-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-rose-500">
          Sign in
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Don't have an account yet?
        <a href="{% url 'main:register' %}" class="font-medium text-rose-500 hover:text-rose-300">
          Register Now
        </a>
      </p>
    </div>
  </div>
</div>
```

Register:
```
<div class="min-h-screen flex items-center justify-center bg-orange-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <div class="relative">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-orange-900">
        Start your baking journey
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px relative">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-orange-900">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-rose-600 hover:bg-rose-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-rose-500">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-rose-500 hover:text-rose-300">
          Login here
        </a>
      </p>
    </div>
  </div>
```

Add product:
```
<div class="flex flex-col min-h-screen bg-orange-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-rose-800">Add Fresh Bakes</h1>
  
    <div class="bg-white shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-orange-700">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-orange-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-rose-800 text-white font-semibold px-6 py-3 rounded-lg hover:bg-rose-700 transition duration-300 ease-in-out w-full">
            Add Fresh Bakes
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
```

Main:
```
<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-orange-100 flex flex-col">
  <div class="p-2 mb-6 relative">
    <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
      {% include "card_info.html" with title='NPM' value=npm %}
      {% include "card_info.html" with title='Name' value=name %}
      {% include "card_info.html" with title='Class' value=class %}
    </div>
    <div class="w-full px-6  absolute top-[44px] left-0 z-20 hidden md:flex">
      <div class="w-full min-h-4 bg-rose-700">
      </div>
    </div>
    <div class="h-full w-full py-6  absolute top-0 left-0 z-20 md:hidden flex ">
      <div class="h-full min-w-4 bg-rose-700 mx-auto">
      </div>
    </div>
</div>
    <div class="px-3 mb-4">
      <div class="flex rounded-md items-center bg-rose-600 py-2 px-4 w-fit">
        <h1 class="text-white text-center">Last Login: {{last_login}}</h1>
      </div>
    </div>
    <div class="flex justify-end mb-6">
      <a href="{% url 'main:create_fresh_bakes_entry' %}" class="bg-rose-600 hover:bg-rose-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
        <button>Add New Fresh Bakes</button>
      </a>
    </div>
```

- Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.

Membuat html dengan logic ketika fresh_bakes ada dan tidak ada:
```
    {% if not fresh_bakes %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/sad_image.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
        <p class="text-center text-orange-600 mt-4">You don't have any bakes yet.</p>
    </div>
    {% else %}
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
        {% for bakes in fresh_bakes %}
            {% include 'card_bakes.html' with fresh_bakes=bakes %}
        {% endfor %}
    </div>
    {% endif %}
```

- Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).

Buat card_bakes.html pada templates dalam direktori main:
```
    <div class="relative top-5 w-120 h-60 bg-orange-100 shadow-lg rounded-lg mb-6 flex flex-col border-2 border-orange-300 transform rotate-1 hover:rotate-0 hover:scale-105 hover:animate-shake transition-transform duration-300 overflow-hidden">
        <div class="bg-rose-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-orange-300">
          <h3 class="font-bold text-xl mb-2">{{ fresh_bakes.name }}</h3>
          <p class="text-gray-600">{{ fresh_bakes.production_date }}</p>
        </div>
      
        <div class="p-4 bg-orange-50 flip-card-back w-full h-full transition-transform duration-700 ease-in-out hover:rotate-y-180">
          <div class="flip-content-front">
            <p class="font-semibold text-lg mb-2">Description</p>
            <p class="text-gray-700 mb-2 truncate whitespace-nowrap">{{ fresh_bakes.description }}</p>
          </div>
          <div class="flip-content-back absolute inset-0 flex items-center justify-center transform rotate-y-180">
            <div>
              <p class="font-semibold text-lg mb-2">Price</p>
              <p class="text-gray-700 font-bold text-2xl">{{ fresh_bakes.price }}</p>
            </div>
          </div>
        </div>
    </div>
```
Karena kita ingin buat card ini flippable, tambahkan script:
```
  <style>
    @keyframes shake {
      0% { transform: rotate(1deg); }
      25% { transform: rotate(-1deg); }
      50% { transform: rotate(1deg); }
      75% { transform: rotate(-1deg); }
      100% { transform: rotate(1deg); }
    }
    .animate-shake {
      animation: shake 0.5s ease-in-out infinite;
    }
  
    .flip-card-back {
      transform-style: preserve-3d;
      perspective: 1000px;
      position: relative;
    }
    .flip-content-front, .flip-content-back {
      backface-visibility: hidden;
      position: absolute;
      width: 100%;
      height: 100%;
    }
    .flip-content-back {
      transform: rotateY(180deg);
    }
    .hover\:rotate-y-180:hover {
      transform: rotateY(180deg);
    }
  </style>
```

- Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!

Tambahkan code berikut pada card_bakes.html:
```
    <div class="absolute top-0 -right-4 flex space-x-1">
      <a href="{% url 'main:edit_fresh_bakes' fresh_bakes.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
      </a>
      <a href="{% url 'main:delete_fresh_bakes' fresh_bakes.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
```

- Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

Pada templates dalam root directory, buat navbar.html. Di dalam tag ```<nav> </nav>```, masukkan div untuk menu utama pada desktop: 
```
      <div class="hidden md:flex items-center">
        {% if user.is_authenticated %}
          <span class="block text-center text-orange-100 font-bold py-2 px-6 rounded transition duration-300">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:show_main' %}" class="text-center text-white font-bold py-2 px-4 rounded transition duration-300">Home</a>
          <a href="{% url 'main:create_fresh_bakes_entry' %}" class="text-center text-white font-bold py-2 px-4 rounded transition duration-300">New Fresh Bakes</a>
          <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">Logout</a>
        {% else %}
          <a href="{% url 'main:show_main' %}" class="text-center text-white font-bold py-2 px-4 rounded transition duration-300">Home</a>
          <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">Login</a>
          <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">Register</a>
        {% endif %}
      </div>
```
Tambahkan juga menu untuk mobile:
```
<div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
    <div class="pt-2 pb-3 space-y-1 mx-auto">
      {% if user.is_authenticated %}
        <a class="block text-center text-yellow-100 font-bold py-2 px-6 rounded transition duration-300">Welcome, {{ user.username }}</a>
        <a href="{% url 'main:show_main' %}" class="block text-center text-white font-bold py-2 px-4 rounded transition duration-300">Home</a>
        <a href="{% url 'main:create_fresh_bakes_entry' %}" class="block text-center text-white font-bold py-2 px-4 rounded transition duration-300">New Fresh Bakes</a>
        <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">Logout</a>
      {% else %}
        <a href="{% url 'main:show_main' %}" class="block text-center text-white font-bold py-2 px-4 rounded transition duration-300">Home</a>
        <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">Login</a>
        <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">Register</a>
      {% endif %}
    </div>
</div>
```
Dan script untuk membuka menu tersebut pada mobile:
```
<script>
const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");

btn.addEventListener("click", () => {
  menu.classList.toggle("hidden");
});
</script>
```