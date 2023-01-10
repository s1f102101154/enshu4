from django.urls import path
from . import views

urlpatterns = [
    #ヘッダー
    path("", views.IndexView.as_view(), name="index"),
    path("weather", views.IndexView7.as_view(), name="weather"),
    path("politics", views.IndexView6.as_view(), name="politics"),
    path("sport", views.IndexView2.as_view(), name="sport"),
    path("it", views.IndexView3.as_view(), name="it"),
    path("animal", views.IndexView5.as_view(), name="animal"),
    #path("home", views.IndexView4.as_view(), name="home"),

    #記事
    path("news1", views.IndexView4.as_view(), name="news1"),
    path("news2", views.news1, name="news2"),
    path("news3", views.news1, name="news3"),
]