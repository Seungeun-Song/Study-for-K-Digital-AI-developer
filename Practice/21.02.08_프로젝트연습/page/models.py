from django.db import models

class Tag(models.Model):
    tag_id = models.AutoField('Tag ID', primary_key=True)
    title = models.CharField('TITLE' ,max_length=10)
    content = models.TextField('CONTENT')
    def __str__(self):
        return self.title   

class Category(models.Model):
    category_id = models.AutoField('Category ID', primary_key=True)
    title = models.CharField('TITLE' ,max_length=10)
    content = models.TextField('CONTENT')
    def __str__(self):
        return self.title    

class Member(models.Model):
    member_id = models.AutoField('Member ID', primary_key=True)
    name = models.CharField('NAME' ,max_length=10)
    category_id = models.ManyToManyField('Category')
    def __str__(self):
        return self.name    

class Post(models.Model):
    post_id = models.AutoField('Category ID', primary_key=True)
    title = models.CharField('TITLE' ,max_length=25)
    content = models.TextField('CONTENT', null=True, blank=True)
    photo_id = models.ManyToManyField('Photo')
    date = models.DateTimeField('TIME', auto_now=True)
    category_title = models.ForeignKey('Category', on_delete=models.CASCADE)
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE)
    tag_id = models.ManyToManyField('Tag')
    def __str__(self):
        return self.title    
    
    def get_absolute_url(self):
        return reverse('page:member_post_detail', args=(self.slug,))

class Photo(models.Model):
    photo_id = models.AutoField('Photo ID', primary_key=True)
    title = models.CharField('TITLE' ,max_length=25)
    source = models.CharField('Image Source' ,max_length=200)
    member_id = models.ForeignKey('Member', on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post',on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField('CONTENT', null=True, blank=True)
    def __str__(self):
        return self.title