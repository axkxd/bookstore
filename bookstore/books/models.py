from django.db import models
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField('Author', help_text='Автор книги')
    genre = models.ManyToManyField('Genre', help_text='Жанр книги')
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    summary = models.TextField(max_length=1500, blank=True, null=True, help_text='Краткое описание книги (до 1500 символов)')

    def __str__(self) -> str:
        return self.title
    

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Укажите жанр книги.')

    def __str__(self) -> str:
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1500, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
