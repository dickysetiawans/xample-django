from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,"login/index.html")

def konfirmasi(request):
	return HttpResponse("<h1> Silahkan Konfirmasi </h1>")