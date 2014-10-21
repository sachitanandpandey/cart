from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    brand = models.ForeignKey('Brand')
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)


    def __unicode__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name