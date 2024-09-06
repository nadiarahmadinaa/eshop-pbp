from django.shortcuts import render

def show_main(request):
    context = {
        'appname' : 'YumYum Bakeshop',
        'name': 'Nadia Rahmadina Aristawati',
        'class': 'PBP D',
        'npm': '2306207972'
    }

    return render(request, "main.html", context)