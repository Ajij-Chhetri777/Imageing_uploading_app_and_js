from django.contrib import admin
from theapp.models import Type , Thepost, Comment
# Register your models here.


admin.site.register(Thepost)
admin.site.register(Type)
admin.site.register(Comment)