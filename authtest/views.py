from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views import generic
from django.conf import settings
from newsapi import NewsApiClient

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html', {})

@login_required
class IndexView(generic.TemplateView):
    template_name = "authtest/private.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        newsapi = NewsApiClient(api_key=settings.NEWSAPI)
        context['top_headlines'] = newsapi.get_everything(domains = "yahoo.co.jp")
        print(context['top_headlines'])
        return context
"""def private_page(request):
    return render(request, 'authtest/private.html', {})"""

def public_page(request):
    return render(request, 'authtest/index.html', {})
