from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    
    title = models.CharField(max_length=500)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    description = models.TextField(max_length=1000)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'