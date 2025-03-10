from django.urls import path
from .views import*

urlpatterns = [
    path("home/",home_page.as_view(),name="home"),
    path("personal_office/",personal_office_page.as_view(),name="personal"),
    path("rating/",rating_page.as_view(),name="rating"),
    path("activity/",activity_page.as_view(),name="activity"),
    path("shop/",shop_page.as_view(),name="shop"),
]