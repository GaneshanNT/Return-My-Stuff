from django.db import models
# Create your models here.
from django.core.validators import RegexValidator
from django.utils.timezone import datetime
from django.contrib.auth.models import User


class Post(models.Model):
    reporter = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,
        help_text='ex :Macbook or wallets etc')
    item_type = models.CharField(max_length=100,
        help_text='ex :laptop or mobiles etc')
    tag =  models.CharField(choices=(
        ("Electronics","Electronics"),
        ("Documents and Govt.Proof","Documents and Govt.Proof"),
        ("Banking accessories and Wallets","Banking accessories and Wallets"),
        ("Clothes","Clothes"),
        ("Others","Others")),max_length=100, null=True, blank=True)
    location = models.CharField(max_length=180,
        help_text='Mention place where you found')
    city = models.CharField(max_length=50)
    state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    state = models.CharField(choices=state_choices,max_length=50, null=True, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Request(models.Model):
    requester = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    proof = models.ImageField(upload_to='proof/%Y/%m/%d/',help_text='(ex : bills)Upload valid proof to get that item')
    viewed = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

