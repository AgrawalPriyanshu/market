from django.urls import path

from . import views

urlpatterns = [
    path('add_page/', views.add_page, name='add_page'),
    path('', views.index, name='index'),

]