from django.shortcuts import render, redirect
from main.forms import FreshBakesForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

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

def create_fresh_bakes_entry(request):
    form = FreshBakesForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_fresh_bakes_entry.html", context)

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