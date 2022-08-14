from django.db import models

# Create your models here.

class FractionalValue(models.Model):
    name = models.FloatField(default='1.0')
    answer= models.CharField(default='1', max_length=200)

    def __str__(self):
        return str(self.name)
