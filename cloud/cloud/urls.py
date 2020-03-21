from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('WebUI.urls')),
    path('', include('edges.urls'))
]
