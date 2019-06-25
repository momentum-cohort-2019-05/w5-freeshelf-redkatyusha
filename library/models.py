from django.db import models
from django.urls import reverse

class Book(models.Model):
    """
    A model for each book in the library.
    """

    title = models.CharField(max_length=500, help_text='Enter the full title of the book.')

    def get_absolute_url(self):
        """Returns the URL to access a specific instance of Book."""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing Book."""
        return self.title