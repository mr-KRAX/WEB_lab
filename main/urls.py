from django.urls import path, include
from . import views
urlpatterns = [
  path('', views.mainBoard, name='home'),
  path('login', views.login, name="login"),
  path('registration', views.registration, name="registration"),
  path('articleLikes/article-<id>', views.likes, name="articleLikes"),
  path('like/article-<id>', views.markLiked, name="like"),

  path('debug_info', views.debug_info, name="debug_info"),

]
