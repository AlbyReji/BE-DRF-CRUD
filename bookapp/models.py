from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length = 100)
    description =models.CharField(max_length = 250)
    author = models.CharField(max_length = 100)
    Created_at = models.DateTimeField(auto_now_add = True)
    
    