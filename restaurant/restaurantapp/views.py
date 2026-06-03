from django.shortcuts import render

def home(request):
    return render(request, 'rest.html')

def menu(request):
    return render(request, 'menu.html')

def admin_page(request):
    return render(request, 'admin.html')

def contact(request):
    return render(request, 'contact.html')