from django import forms
from .models import Book, Author, Genre

from dal import autocomplete


class BookForm(forms.ModelForm):
    author = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='author-autocomplete')
    )
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='genre-autocomplete')
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'isbn', 'summary']


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ('title', 'author', 'genre', 'isbn', 'summary')
#         lables = {
#             'title': 'Name',
#             'author': 'Author',
#             'genre': 'Genre',
#             'isbn': 'ISBN',
#             'summary': 'Summary'
#         }
#         widgets = {
#             'author': forms.ModelMultipleChoiceField(
#                 queryset=Author.objects.all(),
#                 widget=autocomplete.ModelSelect2Multiple(url='author_autocomplete')/
#             ),
#             'genre': forms.ModelMultipleChoiceField(
#                 queryset=Genre.objects.all(),
#                 widget=autocomplete.ModelSelect2Multiple(url='genre_autocomplete')
#             ),
#         }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'description')
        labels = {
            'name': 'Имя и Фамилия',
            'description': 'Описание'
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)
        labels = {'name': 'Genre'}