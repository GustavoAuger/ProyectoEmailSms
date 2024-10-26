from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html') 
	
	
def login_view(request):
    return render(request, 'myapp/login.html')