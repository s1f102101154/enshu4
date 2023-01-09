from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("priv", views.IndexView2.as_view(), name="priv"),
    path('pub', views.IndexView.as_view(), name='pub'),
    path("", views.IndexView.as_view(), name="index"),
]