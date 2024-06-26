from django.urls import path
from theapp.views import home, get_view, register, logins, replycomment

urlpatterns = [
     path('',home,name = 'home'),
     path('<int:id>/',get_view, name = 'get_view'),
     path('register/',register, name= 'register'),
     path('logins/',logins,name= 'logins'),
]

    