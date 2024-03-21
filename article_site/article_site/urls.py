# from django.urls import path
# from articles.views import article_list, parse_articles
#
# urlpatterns = [
#     path('', article_list, name='article_list'),
#     path('parse_articles/', parse_articles, name='parse_articles'),  # Добавляем URL для парсинга статей
# ]

from django.urls import path
from articles.views import display_articles, parse_articles

urlpatterns = [
    path('', display_articles, name='display_articles'),
    path('load_articles/', parse_articles, name='load_articles'),
]

