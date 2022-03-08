from django.db import models

# Create your models here.
class Drink(models.Model):
    owner = models.ForeignKey('auth.User', related_name='drinks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)