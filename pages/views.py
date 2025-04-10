from django.shortcuts import render
from dinamic_view.views import PageView
from django.http import JsonResponse
from django.views import View
from .pages_config import pages
from registretion.models import MyUser

class RatingsViews(View):
    def post(self,request,*args,**kwargs):
        users = MyUser.objects.all().order_by('-rating').values("id","username","rating")
        return JsonResponse(list(users),safe=True)
        

pages_views=[PageView("home.html",links=pages),
           PageView("personal_office.html",links=pages),
           PageView("rating.html",links=pages),
           PageView("activity.html",links=pages),
           PageView("shop.html",links=pages)]

for i in range(len(pages)):
    pages[i]["view"]=pages_views[i]

