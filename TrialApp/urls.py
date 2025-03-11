from django.contrib import admin
from django.urls import path
from TrialApp import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('park', views.park, name='park'),
    path('contact', views.contact, name='contact'),
    path('link1', views.link1, name='link1'),
    path('link2', views.link2, name='link2'),
    path('link3', views.link3, name='link3')
    

]