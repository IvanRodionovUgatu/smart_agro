from django.urls import path

from core.views import create_field

urlpatterns = [path('', create_field)]
