from pathlib import Path
import os
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    return HttpResponse("<h1>My First application</h1>")

def index(request):
    return HttpResponse("<h1>this is index page</h1>")

def users(request):
    return HttpResponse("<h1>this is user page</h1>")

def ht(request):
    result=os.path.join(BASE_DIR,"templates")
    print(result)
    return render(request,'home.html',{'name':'nive'})
    


