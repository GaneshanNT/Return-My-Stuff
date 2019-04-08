from .models import Post,Request
from django.forms import ModelForm,Textarea 
from django.contrib.auth.models import User


class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","item_type","tag","location","city","state","photo_main","photo_1","photo_2","description")
        labels = {
            "item_type":"Item tpe",
            "photo_main":"Picture Main",
            "photo_1":"Picture-1 (Optional)",
            "photo_2":"Picture-2 (Optional)"
        }
        widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 10}),
        }

class RequestForm(ModelForm):
    
    class Meta:
        model = Request
        fields = ("name","phone","proof")
    
