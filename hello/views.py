from django.shortcuts import render
from django.http import HttpResponse 
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'index.html')


def greet(request, name):
    hour = timezone.localtime().hour
    return render(request, 'greet.html', {
        'name': name.title(), 
        'hour': hour
        })