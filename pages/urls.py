from django.urls import path
from .views import*

urlpatterns_pages = [path(page["url"],page["view"].as_view(),name=page["name"]) for page in pages]
urlpatterns=[
    *urlpatterns_pages,
    path("save_size_user/",SaveSizeUserView.as_view(),name="save_size_user")
]