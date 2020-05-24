from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200)
    share_value = models.IntegerField()
    