"""
URL Dispatcher best practices.
Created this url dispatcher file to handle main_app.
From the main project url folder, moved the views.index to this file
with the pattern below.
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [url(r'^$', views.index),] 
