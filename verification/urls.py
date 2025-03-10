from django.urls import path
from .views import*

urlpatterns = [
    path("to_back/",ToBackView.as_view(),name="return"),
    path("check_code/",formVarificationView.as_view(), name="form_varification"),
    path("verification_code/",UserVerificationView.as_view(),name="'verification_code")
]