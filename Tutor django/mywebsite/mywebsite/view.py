from django.http import HttpResponse
from django.shortcuts import render

def index(requet):
	context = {
		'Judul':'Sharing Coffee',
		'subjudul':'Selamat Datang',
		'nav':[
			['/','Home'],
			['/blog','Blog'],
			['/about','About'],
		]
	}
	return render(requet, 'indeex.html',context)

def index2(requet):
	return HttpResponse("halo ini home")