from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = { 'someadj': 'something very cool' }
    return render(request, 'fakeforum.html', content)

def corgi(request):
    return HttpResponse("Corgi's are awesome")