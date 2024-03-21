# from django.db import models
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Tag(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Article(models.Model):
#     title = models.CharField(max_length=200)
#     date = models.DateTimeField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
#     image_url = models.URLField(null=True)
#     content = models.TextField()
#
#     def __str__(self):
#         return self.title
#

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    link = models.URLField()

    def __str__(self):
        return self.title