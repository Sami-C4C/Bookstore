from django.db import models
from booklists.models import Booklist  



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ISBN_number = models.CharField(max_length=13, unique=True)
    booklists = models.ManyToManyField(Booklist, related_name='books', blank=True)


    def __str__(self):
        return self.title
