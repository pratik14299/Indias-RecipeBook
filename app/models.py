from django.conf import settings
from django.db import models

# Create your models here.

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'starter'),
        ('Paneer', 'Paneer'),
        ('Rice', 'Rice'),
        ('Chineese', 'Chineese'),
        ('StreetFood', 'StreetFood'),
        ('StateSpecial', 'StateSpecial'), 
    ] 
    Title  = models.CharField(max_length = 150)
    Discreption = models.TextField()
    Category = models.CharField(max_length =20,choices = CATEGORY_CHOICES) 
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.Title} , {self.author}' 
    

