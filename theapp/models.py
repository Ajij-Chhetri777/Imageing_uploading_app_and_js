from django.db import models
from django.utils.translation import gettext 
from django.contrib.auth.models import  User
# Create your models here.
class Type(models.Model):
    name = models.CharField(gettext('what you categories '), max_length = 100 )
    def __str__(self):
        return self.name 
class Thepost(models.Model):
    title = models.CharField(gettext('title of your creation'),max_length=100)
    description = models.TextField(gettext('Describe you art'))
    images = models.ImageField(gettext('show us your magic'), upload_to='saved/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True )
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='hero')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name = 'types')
    def __str__(self):
        return self.title
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'users')
    belong_to = models.ForeignKey(Thepost,on_delete=models.CASCADE, related_name = 'belongs')
    post = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True, null = True)
    def __str__(self):
        return self.post 

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'us')
    post = models.ForeignKey(Thepost,on_delete= models.CASCADE, related_name ='thepost')
    has_liked = models.BooleanField(default= False)

class Reply(models.Model):
    initial_comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name = 'replies')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='useres')
    line = models.TextField()
    def __str__(self):
        return self.line