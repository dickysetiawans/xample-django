from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	context = {
		'judul':'Blog',
		'sub':'blog',
		'kalimat':'Ini Adalah Blog',
		'nav': [
			['/','Home'],
			['/blog/cerita/','cerita'],
			['/blog/berita/','news'],
			['/blog/recent/','recent'],
			['/login','Login'],
		]
	}
	return render(request,"blog/index.html",context)

def berita(request):
	context = {
		'judul':'berita',
		'sub':'Berita',
		'kalimat':'Ini Adalah Berita',
	}
	return render(request,"blog/index.html",context)

def cerita(request):
	context = {
		'judul':'cerita',
		'sub':'cerita',
		'kalimat':'Ini Adalah cerita',
	}
	return render(request,"blog/index.html",context)


def recent(request):
	return HttpResponse("<h1> Ini Adalah recent</h1>")