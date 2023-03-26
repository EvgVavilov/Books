from django.db import models
from django.urls import reverse


class Book(models.Model):
    author = models.ManyToManyField("Author", related_name="books", verbose_name="Авторы")
    name = models.TextField(verbose_name="Название")
    about_book = models.TextField(verbose_name="Описание")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    photo = models.ImageField(
        upload_to="books/%Y/%m/",
        blank=True,
        null=True,
        verbose_name="Обложка",
        default='books/2023/03/default_book.jpg'
    )
    link_to_shop = models.TextField(verbose_name="ссылка в магазин", blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book", kwargs={"book_slug": self.slug})


class Author(models.Model):
    name = models.TextField(verbose_name="Имя")
    about_author = models.TextField(verbose_name="Об авторе")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    photo = models.ImageField(
        upload_to="authors/%Y/%m/",
        blank=True,
        null=True,
        verbose_name="Фото",
        default='authors/2023/03/no_avatar.jpg'
    )
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author", kwargs={"author_slug": self.slug})
