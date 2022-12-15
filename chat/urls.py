from django.urls import path
from . import views

urlpatterns = [
    #ヘッダー
    path("", views.index, name="index"),
    path("weather", views.weather, name="weather"),
    path("politics", views.politics, name="politics"),
    path("sport", views.sport, name="sport"),
    path("it", views.it, name="it"),
    path("animal", views.animal, name="animal"),

    #記事
    path("news1", views.news1, name="news1"),
    path("news2", views.news1, name="news2"),
    path("news3", views.news1, name="news3"),
]