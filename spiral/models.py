from django.db import models
from django.utils import timezone

class Person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    full_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    birthday = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    activated_date = models.DateTimeField(blank=True, null=True)

    def activate(self):
        self.activated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.full_name

class Address(models.Model):
    street_name_1 = models.CharField(max_length=100)
    street_name_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.text
