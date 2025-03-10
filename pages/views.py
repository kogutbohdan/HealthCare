from django.shortcuts import render
from dinamic_view.views import PageView

home_page=PageView("home.html")
personal_office_page=PageView("personal_office.html")
rating_page=PageView("rating.html")
activity_page=PageView("activity.html")
shop_page=PageView("shop.html")