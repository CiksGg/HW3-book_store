from django.db import models

# Create your models here.
class Book(models.Model):
    category = models.TextField()
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    published = models.DateTimeField()