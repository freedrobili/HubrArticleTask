from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Article
from .parser import parse_habr_articles
from django.http import JsonResponse
from django.core import serializers


def display_articles(request):
    article_list = Article.objects.all().order_by('-date')  # Получаем все статьи, отсортированные по дате (последние сверху)
    paginator = Paginator(article_list, 5)  # Показывать по 5 статей на каждой странице

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, доставляем первую страницу
        articles = paginator.page(1)
    except EmptyPage:
        # Если страница находится за пределами доступного диапазона (например, 9999),
        # доставляем последнюю страницу результатов
        articles = paginator.page(paginator.num_pages)

    return render(request, 'articles/article_list.html', {'articles': articles})  # Используем шаблон с пагинацией


def parse_articles(request):
    # Вызываем функцию парсинга статей
    parse_habr_articles()

    # Получаем последние 5 статей из базы данных
    latest_articles = Article.objects.order_by('-date')[:5]

    # Преобразуем статьи в JSON
    articles_data = serializers.serialize('json', latest_articles)

    # Возвращаем JSON-ответ с данными статей
    return JsonResponse({"articles": articles_data})