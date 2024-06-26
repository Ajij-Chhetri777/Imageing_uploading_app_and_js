from django.urls import path
from api.views import ThepostAPI, CommentAPI, postviewAPI, CommentviewByPostAPI, TypeviewByUserAPI
urlpatterns = [
    path('posts/',ThepostAPI.as_view()),
    path('comments/',CommentAPI.as_view()),
    path('posts/<int:pk>', postviewAPI.as_view()),

    path('posts/comments/<int:pk>',CommentviewByPostAPI.as_view()),
    path('posts/type/<int:pk>',TypeviewByUserAPI.as_view()),
]

