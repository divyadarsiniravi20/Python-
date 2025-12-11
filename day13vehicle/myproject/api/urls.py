from django.urls import path
from .views import vehicle
urlpatterns = [
    path('vehicles/', vehicle)
]