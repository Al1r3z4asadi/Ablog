from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from PIL import Image
import os
# Create your models here.

    
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valids = ['.jpg' , '.png']
    if ext.lower() not in valids:
        raise ValidationError('unsuported file exteion')

class Article(models.Model):
    title = models.CharField(max_length=128 , null=False , blank=False)
    
    image = models.FileField(default='default.jpg',upload_to='files/article_cover/' ,
     null=False , blank=False , validators=[validate_file_extension])

    content = models.TextField(blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category' ,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self , *args , **kwargs):
        super().save(*args , **kwargs)
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400 :
            output_size = (400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)    

class Category(models.Model):
    title = models.CharField(max_length=128)
    cover = models.FileField(default='default.jpg',upload_to='files/category_cover/',
    validators=[validate_file_extension] )    

    def __str__(self):
        return self.title














