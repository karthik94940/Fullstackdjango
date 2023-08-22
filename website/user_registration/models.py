from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    user_name = models.CharField(max_length=100, unique=True)
    user_mail = models.EmailField(unique=True)
    mobile_number = models.IntegerField(unique=True)
    password = models.CharField(max_length=15)
    re_password = models.CharField(max_length=15)

