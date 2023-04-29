from django.urls import path
from . import views
from .autocomplete_view import AuthorAutocomplete, GenreAutocomplete


urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_genre/', views.add_genre, name='add_genre'),

    path('author-autocomplete/', AuthorAutocomplete.as_view(), name='author-autocomplete'),
    path('genre-autocomplete/', GenreAutocomplete.as_view(), name='genre-autocomplete'),
]