from django import forms 
from theapp.models  import Thepost, Comment, Reply
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Thepost
        fields = ["title","description","images","type"]
        widgets = {
            "title" : forms.TextInput(attrs={
                'class':'my-class', 'placeholder': 'enter the title',
                 'style': 'font-weight :bold; font-family: Arial, sans-serif;'
            }
            
            ),
            "description": forms.Textarea(
                attrs={
                    'rows': 5, 'cols': 50,
                     'style': 'font-weight :bold; font-family: Arial, sans-serif;'
                }
            ),
            "type": forms.RadioSelect(
             attrs={
                'style':'font-weight:bold; font-family:Arial, sans-serif;'
                 
             }
            ),
        }
        

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class LoginForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["post",] 
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields  = ["line","initial_comment"]