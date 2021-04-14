from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from .forms import HelloForm

def index(request):
    data = Friend.objects.all().values_list('id', 'name')
    params = {
        'title': 'Hello',
        'data': data,
        }
    return render(request, 'hello/index.html', params)
    

