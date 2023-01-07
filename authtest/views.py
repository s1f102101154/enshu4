from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html', {})

@login_required
def private_page(request):
    return render(request, 'chat/templates/news/news1.html', {})

def public_page(request):
    return render(request, 'chat/templates/news/news2.html', {})
