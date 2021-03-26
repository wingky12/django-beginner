from django.http import HttpResponse

def home(request):
      return HttpResponse("ini home")

def about(request):
	return HttpResponse("ini halaman about")