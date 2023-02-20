from django.db import models
from django.conf import settings

# Create your models here.
class Listing(models.Model):
    shoe = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # author = models.CharField(max_length=50)
    shoe_size = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.shoe} by {self.author.name}'