from django.db import models

# Create your models here.
class Fire(models.Model):
    lat=models.FloatField()
    lon=models.FloatField()
    timestamp=models.DateTimeField(auto_now_add=True)

