from django.db import models


class Ecommerce(models.Model):
 produto = models.CharField(max_length=200)
 foto = models.ImageField(upload_to='fotos/')
 
 def __str__(self):
    return self.produto
