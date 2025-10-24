from django.shortcuts import render

def all_chai(request):
    return render(request, 'cdd/all_chai.html')
