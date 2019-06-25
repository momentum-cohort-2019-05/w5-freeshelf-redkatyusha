import uuid
from django.db import models
from django.urls import reverse
import datetime

class Book(models.Model):
    """
    A model for each book in the library.
    """

    title = models.CharField(max_length=500, help_text='Enter the full title of the book.')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    link = models.URLField(max_length=500, help_text='Enter a link to the book online.')
    description = models.TextField(max_length=2000, help_text='Enter a short description of the book to summarize it.')
    when_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def get_absolute_url(self):
        """Returns the URL to access a specific instance of Book."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing Book."""
        return self.title


class Author(models.Model):
    """
    A model for each author of a book or books in the library.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Category(models.Model):
    """
    A model representing categories that each instance of the Book model may a part of.
    """

    name = models.CharField(max_length=200, help_text='Enter a category of book')

    def __str__(self):
        """String for representing Category."""
        return self.name