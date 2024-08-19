from django.urls import path
from .views import sg

urlpatterns = [
    path("", sg, name="sg"),
]
