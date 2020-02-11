from django.conf.urls import url,include
from django.urls import path ,include
from . import views
urlpatterns = [
    path('', views.PersonView.as_view()),
    path('add/', views.weatherView.as_view()),
]
