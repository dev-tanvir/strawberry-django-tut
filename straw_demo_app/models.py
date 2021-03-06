from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=20)
    color = models.ForeignKey('Color', blank=True, null=True,
            related_name='fruits', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name