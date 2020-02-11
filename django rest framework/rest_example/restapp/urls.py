from django.conf.urls import url,include
from django.urls import path ,include
from . import views
urlpatterns = [
    path('', views.UserList.as_view()),
    path('add/', views.UserDetail.as_view()),
]
