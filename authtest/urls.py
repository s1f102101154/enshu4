from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('priv', views.IndexView.as_view(), name='priv'),
    path('pub', views.public_page, name='pub'),
]