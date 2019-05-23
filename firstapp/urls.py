# coding=utf-8
from django.urls import path
from firstapp.views import *

urlpatterns = [
    path('user/', UserRoot.as_view()),
]
