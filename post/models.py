from django.db import models

# Create your models here.
from django.utils.timezone import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    reporter = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    tag =  models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    