from django.shortcuts import render

# Create your views here.

def seletivehome(request):
    return render(request, 'home.html')

def nova_empresa(request):
    return render(request, 'nova_empresa.html')