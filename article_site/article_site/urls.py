from django.urls import path
from articles.views import display_articles, parse_articles

urlpatterns = [
    path('', display_articles, name='display_articles'),
    path('load_articles/', parse_articles, name='load_articles'),
]

