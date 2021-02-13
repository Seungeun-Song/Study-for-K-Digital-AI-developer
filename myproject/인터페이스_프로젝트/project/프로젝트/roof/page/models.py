from django.db import models
from django.urls import reverse

from page.fields import ThumbnailImageField

class Tag(models.Model):
    title = models.CharField('TITLE' ,max_length=10)
    slug = models.SlugField('SLUG', primary_key=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT', blank=True)
    
    def __str__(self):
        return self.title   

class Category(models.Model):
    title = models.CharField('TITLE' ,max_length=10)
    slug = models.SlugField('SLUG', primary_key=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT', blank=True)
    
    def __str__(self):
        return self.title    

class Member(models.Model):
    name = models.CharField('NAME' ,max_length=10)
    slug = models.SlugField('SLUG', primary_key=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT', blank=True)
    category = models.ManyToManyField('Category')
    
    def __str__(self):
        return self.name  

class Post(models.Model):
    title = models.CharField('TITLE' ,max_length=25)
    slug = models.SlugField('SLUG', primary_key=True, allow_unicode=True, help_text='one word for title alias.')
    content = models.TextField('CONTENT', blank=True)
    date = models.DateTimeField('TIME', auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

class Photo(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    title = models.CharField('TITLE' ,max_length=25)
    slug = models.SlugField('SLUG', primary_key=True, allow_unicode=True, help_text='one word for title alias.')
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    content = models.TextField('CONTENT', blank=True)

    def __str__(self):
        return self.title