from django.urls import path
from .views import*

urlpatterns_pages = [path(page["url"],page["view"].as_view(),name=page["name"]) for page in pages]
urlpatterns=[
    *urlpatterns_pages,
    path("save_size_user/",SaveSizeUserView.as_view(),name="save_size_user"),
    path("save_password/",ChangePasswordView.as_view(),name="save_user"),
    path("exit/",ExitView.as_view(),name="exit"),
    path("buy_icon/<int:id>",BuyIcon.as_view(),name="buy"),
    path("change_icon/",ChangeIconView.as_view(),name="change_icon"),
    path("save_task/<int:id>",SaveTask.as_view(),name="save_task")
]