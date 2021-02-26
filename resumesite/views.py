from django.shortcuts import render

def homepage(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'index2.html', {})	

def advice(request):
	return render(request, 'index3.html', {})

def blog(request):
	return render(request, 'home.html', {})