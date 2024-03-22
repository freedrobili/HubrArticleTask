import datetime
import requests
from .models import Author, Tag, Article
from django.utils import timezone
from bs4 import BeautifulSoup


def parse_habr_articles():
    print("Начало парсинга статей...")
    url = 'https://habr.com/ru/articles/'
    response = requests.get(url).text
    data = BeautifulSoup(response, 'html.parser')

    for article in data.find_all('h2', class_='tm-title tm-title_h2')[:5]:
        title = article.a.span.text
        link = 'https://habr.com' + article.a['href']
        print("Сохранение статьи:")
        print("Заголовок:", title)
        print("Ссылка:", link)

        article_response = requests.get(link).text
        article_data = BeautifulSoup(article_response, 'html.parser')

        figure_element = article_data.find('figure', class_='full-width')
        if figure_element:
            image_element = figure_element.find('img')
            if image_element:
                image_url = image_element.get('src')
                print("URL изображения:", image_url)
            else:
                print("Изображение не найдено")
        else:
            print("Тег <figure> не найден")

        author_element = article_data.find('a', class_='tm-user-info__username')
        if author_element:
            author_name = author_element.get_text(strip=True)
        else:
            author_name = "No author available"
        print("Автор:", author_name)

        time_element = article_data.find('time')
        if time_element:
            time_published = time_element['title']
        else:
            time_published = "Unknown"
        print("Время публикации:", time_published)

        content = (article_data.find('div', class_='tm-article-body').text.strip())[:500]
        print("Содержание:", content)

        tags_element = article_data.find('div', class_='tm-article-presenter__meta-list')
        if tags_element:
            tags = [tag.text.strip() for tag in tags_element.find_all('a', class_='tm-tags-list__link')]
        else:
            tags = []

        print("Теги:", tags)

        for tag_name in tags:
            tag_articles_count = Article.objects.filter(tags__name=tag_name).count()
            print(f"({tag_articles_count} статей с тегом '{tag_name}')")

        try:
            existing_article = Article.objects.filter(title=title).first()
            if existing_article:
                continue

            author, created = Author.objects.get_or_create(name=author_name)

            new_article = Article.objects.create(
                title=title,
                link=link,
                date=timezone.now() if time_published == "Unknown" else timezone.make_aware(
                    datetime.datetime.strptime(time_published, "%Y-%m-%d, %H:%M")),
                author=author,
                image_url=image_url,
                content=content,
            )

            for tag_name in tags:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                if tag:
                    new_article.tags.add(tag)
                else:
                    print(f"Тег {tag_name} не найден")
        except Exception as e:
            print(f"Ошибка сохранения статьи в базе данных: {e}")