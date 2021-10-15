from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'About Us',
		'subjudul':'About Us',
	}
	return render(request,"about/index.html", context)


