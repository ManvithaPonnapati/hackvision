from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app_vision/index.html', {})

def index2(request):
    return render(request, 'app_vision/index2.html', {})

def index3(request):
    return render(request, 'app_vision/index3.html', {})