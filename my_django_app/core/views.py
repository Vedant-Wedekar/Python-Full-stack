from django.http import HttpResponse
from django.shortcuts import render

def home(request):
     return render(request,'websites/index.html', {'message': 'Template loaded!'})

def about(request):
     return HttpResponse('<h1>about</h1>')

def contact(request):
     return HttpResponse('<h1>contact</h1>') 