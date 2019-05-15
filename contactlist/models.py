from django.db import models
from django.utils import timezone


class Contact(models.Model):
    nickname = models.CharField(max_length=50)
    fullname = models.CharField(max_length=400)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    group = models.CharField(max_length=100)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nickname
