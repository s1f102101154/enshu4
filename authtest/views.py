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
    #login_url = 'authtest/home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView2, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp")
        print(context['top_headlines'])
        return context

