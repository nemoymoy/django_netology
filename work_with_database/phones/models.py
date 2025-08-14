from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length = 50, null = False)
    price = models.IntegerField()
    image = models.FilePathField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length = 50)
