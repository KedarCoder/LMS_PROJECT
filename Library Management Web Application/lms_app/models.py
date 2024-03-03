from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class YourModelName(models.Model):
    # your model fields here

    class Meta:
        verbose_name = 'lms_app'
