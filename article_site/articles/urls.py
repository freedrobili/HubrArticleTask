from django.urls import path
from .views import display_articles, parse_articles

urlpatterns = [
    path('articles/', display_articles, name='display_articles'),
    path('parse_articles/', parse_articles, name='parse_articles'),
]


