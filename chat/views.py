from django.shortcuts import render
#
from django.views import generic
from django.conf import settings
from newsapi import NewsApiClient
#

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

#
class IndexView(generic.TemplateView):
    template_name = "chat/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(q='乃木坂46', from_param='2022-11-21',)
        print(context['top_headlines'])
        return context
#