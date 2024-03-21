from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Article
from .parser import parse_habr_articles
from django.http import JsonResponse
from django.core import serializers


def display_articles(request):
    article_list = Article.objects.all().order_by('-date')
    paginator = Paginator(article_list, 5)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'articles/article_list.html', {'articles': articles})


def parse_articles(request):
    parse_habr_articles()

    latest_articles = Article.objects.order_by('-date')[:5]

    articles_data = serializers.serialize('json', latest_articles)

    return JsonResponse({"articles": articles_data})
