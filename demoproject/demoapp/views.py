from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def name(request):
    name = request.POST['given_name']
    return render(request, 'name.html', {'given_name': name})