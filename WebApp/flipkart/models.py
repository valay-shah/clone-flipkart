from django.db import models

# Create your models here.

class Cart(models.Model):
    name = models.CharField(max_length=32, blank=True)
    price = models.FloatField(blank=True)
    product = models.CharField(max_length=32, blank=True)
    email = models.CharField(max_length=32, blank=True)
    datetime = models.DateTimeField(auto_now=True, blank=True)
    seller = models.CharField(max_length=32, blank=True)

class Feedback(models.Model):

    RATING_CHOICES = (
        ('1','1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    name = models.CharField(max_length=34)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    rating = models.CharField(max_length=4, choices=RATING_CHOICES)
    feedback = models.TextField()

class ProductInformation(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    COUNTRY_OF_ORIGIN = (
        ('India', 'India'),
        ('America', 'America'),
        ('Russia', 'Russia'),
        ('Paris', 'Paris'),
    )

    CATEGORY_CHOICES = (
        ('Electronics','Electronics'),
        ('Clothing', 'Clothing'),
        ('Medical', 'Medical'),
        ('Accessories', 'Accessories'),
        ('Furniture', 'Furniture'),
        ('Home Essentials','Home Essentials')
    )

    name = models.CharField(max_length=32)
    price = models.FloatField()
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    country_of_origin = models.CharField(max_length=32, blank=True, choices = COUNTRY_OF_ORIGIN)
    seller = models.CharField(max_length=32)
    rating = models.CharField(max_length=32, blank=True, choices=RATING_CHOICES)