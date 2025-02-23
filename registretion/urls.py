from django.urls import path
from . import views

urlpatterns=[
    path("",views.IndexView.as_view(), name="home"),
    path("registration/",views.RegistrationView.as_view(),name="registration"),
    path("autorization/",views.AuthorizationView.as_view(),name="autorization"),
    path("check_code/",views.FormVarificationView.as_view(), name="form_varification"),
    path("save_user_bd/",views.UserRegistrationsView.as_view(), name="save_user_bd"),
    path("to_back/",views.ToBackView.as_view(),name="return")
]