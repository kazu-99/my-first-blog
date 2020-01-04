from django.shortcuts import render
from .models import BookModel2
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'f_test/index.html')

def hellodjango():
    return print('Hello Django!')

# 本モデル
def book(request):
    xx = {'x': BookModel2.objects.all(),}
    return render(request,'f_test/booklist.html',xx)
