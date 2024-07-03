from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
from .models import *
from .models import reader
def home(request):
    return render(request,"home.html",context={"current_tab":"home"})

def readers_tab(request):
    readers_count = reader.objects.count()
    return render(request,"readers.html",context={"readers_count": readers_count})

def shopping(request):
    return HttpResponse("Welcome to Shopping")

def save_student(request):
    student_name = request.POST['student_name']
    return render(request,"welcome.html",context={'student_name':student_name})

def readers_tab(request):
    readers = reader.objects.all()
    return render(request,"readers.html",context={"current_tab": "readers", "readers":readers})