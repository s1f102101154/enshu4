from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "chat/index.html")

def weather(request):
    return render(request, "chat/weather.html")

def politics(request):
    return render(request, "chat/politics.html")

def sport(request):
    return render(request, "chat/sport.html")

def it(request):
    return render(request, "chat/it.html")

def animal(request):
    return render(request, "chat/animal.html")

def news1(request):
    return render(request, "news/news1.html")

def news2(request):
    return render(request, "news/news2.html")

def news3(request):
    return render(request, "news/news3.html")