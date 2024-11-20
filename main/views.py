from main.forms import FreshBakesForm
from main.models import Product
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import datetime
from django.urls import reverse
import json
from django.http import JsonResponse

@csrf_exempt
def create_mood_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_bakes = Product.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"]
        )

        new_bakes.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def create_fresh_bakes_entry(request):
    form = FreshBakesForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        fresh_bakes = form.save(commit=False)
        fresh_bakes.user = request.user
        fresh_bakes.save()
        return redirect('main:show_main')  

    context = {'form': form}
    return render(request, "create_fresh_bakes_entry.html", context)

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

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yay! We successfully created your account!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@login_required(login_url='/login')
def show_main(request):
    context = {
        'appname' : 'YumYum Bakeshop',
        'name': request.user.username,
        'class': 'PBP D',
        'npm': '2306207972',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

@csrf_exempt
@require_POST
def add_bakes_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    price = request.POST.get("price")
    user = request.user
    if name=="" or description=="":
        return HttpResponse(b"ERROR: Invalid data.", status=400)
    new_bakes = Product(
        name=name, description=description,
        price=price,
        user=user
    )
    new_bakes.save()
    return HttpResponse(b"CREATED", status=201)


def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")