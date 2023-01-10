from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.conf import settings
from newsapi import NewsApiClient

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html', {})

#@login_required
class IndexView(generic.TemplateView):
    template_name = "authtest/public.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp",page_size = 5)
        print(context['top_headlines'])
        return context

class IndexView2(LoginRequiredMixin,generic.TemplateView):
    template_name = "authtest/private.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView2, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp")
        print(context['top_headlines'])
        return context

class IndexView3(LoginRequiredMixin,generic.TemplateView):
    template_name = "authtest/private2.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView3, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp",q = "sport")
        print(context['top_headlines'])
        return context

class IndexView4(LoginRequiredMixin,generic.TemplateView):
    template_name = "authtest/private3.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView4, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp",q = "it")
        print(context['top_headlines'])
        return context

class IndexView5(LoginRequiredMixin,generic.TemplateView):
    template_name = "authtest/private4.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView5, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp",q = "it")
        print(context['top_headlines'])
        return context

class IndexView6(LoginRequiredMixin,generic.TemplateView):
    template_name = "authtest/private5.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView6, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp",q = "it")
        print(context['top_headlines'])
        return context
