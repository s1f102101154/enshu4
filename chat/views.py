from django.shortcuts import render
#
from django.views import generic
from django.conf import settings
from newsapi import NewsApiClient
#

# Create your views here.
def index(request):
    return render(request, "chat/index.html")
"""
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
"""

def news1(request):
    return render(request, "news/news1.html")

#
class IndexView(generic.TemplateView):
    template_name = "chat/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp",page_size = 5)
        print(context['top_headlines'])
        return context
#

class IndexView2(generic.TemplateView):
    template_name = "chat/sport.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView2, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp", q='スポーツ', page_size = 5)
        print(context['top_headlines'])
        return context

class IndexView3(generic.TemplateView):
    template_name = "chat/it.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView3, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains="yahoo.co.jp", q = "it", page_size = 5)
        print(context['top_headlines'])
        return context

class IndexView4(generic.TemplateView):
    template_name = "news/news1.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView4, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp")
        print(context['top_headlines'])
        return context

class IndexView5(generic.TemplateView):
    template_name = "chat/politics.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView5, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains="yahoo.co.jp", q = "政治", page_size = 5)
        print(context['top_headlines'])
        return context

