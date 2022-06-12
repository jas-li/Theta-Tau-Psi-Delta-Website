from django.db import models

class Brother(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False, default='')
    last_name = models.CharField(max_length=30, blank=False, null=False, default='')
    major = models.CharField(max_length=120, blank=False, null=False, default='')
    hometown = models.CharField(max_length=120, blank=True, null=False, default='')
    graduation_year = models.IntegerField()
    email = models.EmailField(max_length=254)
    