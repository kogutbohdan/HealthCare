from django.urls import path
from .views import*

urlpatterns = [path(page["url"],page["view"].as_view(),name=page["name"]) for page in pages]