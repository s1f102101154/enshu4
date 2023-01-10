from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("priv", views.IndexView2.as_view(), name="priv"),
    path("priv2", views.IndexView3.as_view(), name="priv2"),
    path("priv3", views.IndexView3.as_view(), name="priv3"),
    path('pub', views.IndexView.as_view(), name='pub'),
    path("", views.IndexView.as_view(), name="index"),
]