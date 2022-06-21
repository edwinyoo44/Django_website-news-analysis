from django.contrib import admin
from django.urls import path
from django.urls import include

from views import views



urlpatterns = [
    path('', views.index),
    path('api/', include('api.urls')),
    path('views/', include('views.urls')),

]
