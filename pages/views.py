from django.shortcuts import render
from dinamic_view.views import PageView
from django.http import JsonResponse,HttpResponse
from django.views import View
from .pages_config import pages
from registretion.models import MyUser
from .callbacks import draw_personall_data

class RatingsView(View):
    def post(self,request,*args,**kwargs):
        users = MyUser.objects.all().order_by('-rating').values("id","username","rating")
        return JsonResponse(list(users),safe=True)
        
class SaveSizeUserView(View):
    def post(self,request):
        weight=float(request.POST.get("weight"))
        height=float(request.POST.get("height"))
        aime=request.POST.get("aime")
        user=MyUser.objects.get(id=request.session.get("user_id"))
        user.weight=weight
        user.height=height
        user.aime=aime
        user.save()
        return JsonResponse({
            "status":"ok"
        })
    
class ChangePasswordView(View):
    def post(self,request):
        password=request.POST.get("password")
        user=MyUser.objects.get(id=request.session.get("user_id"))
        user.set_password(password)
        return JsonResponse({
            "status":"ok"
        })

pages_views=[PageView("home.html",links=pages),
           PageView("personal_office.html",links=pages
                    ,callback_dinamic_params=draw_personall_data),
           PageView("rating.html",links=pages),
           PageView("activity.html",links=pages),
           PageView("shop.html",links=pages)]

for i in range(len(pages)):
    pages[i]["view"]=pages_views[i]

