from django.db import models
    

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    year_published = models.IntegerField()
    genre = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=1500)
    cover = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    shipping_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self) -> str:
        return f"{self.book} ({self.rating}) by {self.customer}"

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ManyToManyField('Author', help_text='Автор книги')
#     genre = models.ManyToManyField('Genre', help_text='Жанр книги')
#     isbn = models.CharField('ISBN', max_length=13, unique=True)
#     summary = models.TextField(max_length=1500, blank=True, null=True, help_text='Краткое описание книги (до 1500 символов)')

#     def __str__(self) -> str:
#         return self.title
    

# class Genre(models.Model):
#     name = models.CharField(max_length=200, help_text='Укажите жанр книги.')

#     def __str__(self) -> str:
#         return self.name
    

# class Author(models.Model):
#     name = models.CharField(max_length=150)
#     description = models.TextField(max_length=1500, blank=True, null=True)

#     def __str__(self) -> str:
#         return self.name
