from django.db import models

# Create your models here.
class Clasiffier(models.Model):
    texto = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)