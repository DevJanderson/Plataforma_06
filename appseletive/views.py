from django.shortcuts import render

# Create your views here.

def seletivehome(request):
    return render(request, 'home.html')