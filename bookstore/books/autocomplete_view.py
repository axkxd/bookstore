from dal import autocomplete
from .models import Author, Genre

class AuthorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Author.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

class GenreAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Genre.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs