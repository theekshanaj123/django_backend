from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class newspage(models.Model):
    title = models.CharField(max_length=200)
    summery = models.TextField()
    content = models.JSONField()
    image = models.TextField()
    status = models.BooleanField(default=True)
