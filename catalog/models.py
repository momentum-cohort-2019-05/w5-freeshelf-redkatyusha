from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    """Model describing the categories of books, which in this case refers usually to the language or OS being taught."""
    
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

class Book(models.Model):
    """Model used for each book in the Freeshelf catalog."""
    
    title = models.CharField(max_length=500)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    description = models.TextField(max_length=1000)
    category = models.ManyToManyField(Category)
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['author', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    """Model describing the author of one or more books in the catalog."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    favorite_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    unique_together = [['user', 'favorite_book']]

    def __str__(self):
        pass