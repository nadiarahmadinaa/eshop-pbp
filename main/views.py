from django.shortcuts import render, redirect, reverse
from main.forms import FreshBakesForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

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
    fresh_bakes = Product.objects.filter(user=request.user)
    context = {
        'appname' : 'YumYum Bakeshop',
        'name': request.user.username,
        'class': 'PBP D',
        'npm': '2306207972',
        'fresh_bakes': fresh_bakes,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)


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