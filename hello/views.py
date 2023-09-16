from django.shortcuts import render
from django.http import HttpResponse 
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')


def greet(request, name):
    hour = timezone.localtime().hour
    return render(request, 'hello/greet.html', {
        'name': name.title(), 
        'hour': hour
        })