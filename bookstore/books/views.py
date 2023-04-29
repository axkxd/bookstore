from django.shortcuts import render, redirect
from .forms import BookForm, AuthorForm, GenreForm


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('bool_detail', pk=book.id)
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            # return redirect('author_detail', pk=author.pk)
            return redirect('add_author')

    else:
        form = AuthorForm()
    return render(request, 'books/add_author.html', {'form': form})

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            # return redirect('genre_detail', pk=genre.pk)
            return redirect('add_genre')

    else:
        form = GenreForm()
    return render(request, 'books/add_genre.html', {'form': form})