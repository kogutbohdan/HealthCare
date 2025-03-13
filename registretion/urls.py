from django.urls import path
from .views import* 

urlpatterns=[
    path("",IndexView.as_view(), name="home"),
    path("registration/",registrationView.as_view(),name="registration"),
    path("autorization/",authorizationView.as_view(),name="autorization"),
    path("save_user_bd/",UserRegistrationsView.as_view(), name="save_user_bd"),
    path("login/",AurhorizationView.as_view(), name="login"),
]