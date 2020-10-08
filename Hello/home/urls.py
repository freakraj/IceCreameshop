# self creating urls file in home app urls.py
from django.contrib import admin
from django.urls import path 
from home import views 

urlpatterns = [
    
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path('services',views.services,name='sevices'),
    path('contact',views.contact,name='contact')


]
