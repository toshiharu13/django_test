from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('click/', views.get_click, name='getclick')
]
