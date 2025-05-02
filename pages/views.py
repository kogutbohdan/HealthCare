from dinamic_view.views import PageView
from django.http import JsonResponse
from django.views import View
from .pages_config import pages
from registretion.models import MyUser
from .callbacks import*
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from .models import*
from django.shortcuts import redirect


class RatingsView(View):
    def post(self,request,*args,**kwargs):
        users = MyUser.objects.all().order_by('-rating').values("id","username","rating")
        return JsonResponse(list(users),safe=True)
        
class SaveSizeUserView(View):
    def post(self,request):
        weight=float(request.POST.get("weight"))
        height=float(request.POST.get("height"))
        aime=request.POST.get("aime")
        print(weight)
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
        try:
            validate_password(password, user)
            user.set_password(password)
            user.save()
            return JsonResponse({
                 "status":"ok"
            })
        except ValidationError as e:
            return JsonResponse({
                "status": "error",
                "errors":{
                    "password":[e.messages]
                }
            }, status=400)
        
class ExitView(View):
    def post(self,request):
        logout(request)
        request.session.flush()
        return JsonResponse({
            "status":"ok"
        })
    
class BuyIcon(View):
    def post(self,request,id):
        user=MyUser.objects.get(id=request.session.get("user_id"))
        icon=ShopModel.objects.get(id=id)
        if user.many>=icon.costs and icon not in user.things.all():
            user.many-=icon.costs
            user.things.add(icon)
            user.save()
            return JsonResponse({
                "status":"ok",
                "many":user.many
            })
        return JsonResponse({
            "status":"error"
        })
    
class ChangeIconView(View):
    def post(self,request):
        user=MyUser.objects.get(id=request.session.get("user_id"))
        user.icon=request.POST.get("imageUrl")
        user.save()
        return JsonResponse({
            "status":"ok"
        })

class SaveTask(View):
    def post(self,request,id):
        user=MyUser.objects.get(id=request.session.get("user_id"))
        number=request.POST.get("number")
        if number.isdigit():
            number=int(number)
            task=user.tasks.get(id=id)
            user.many+=task.many*number
            user.points+=task.points*number
            #user.tasks.remove(task)
            user.save()
            previus_statistics=Statistics.objects.filter(task=task).order_by("-counts").first()
            statistic=Statistics(number=number,counts=previus_statistics.counts+1 if previus_statistics else 1,task=task,user=user,coins=task.many*number,points=task.points*number)
            statistic.save()
            return JsonResponse({
                "status":"ok"
            })
        return JsonResponse({
            "errors":["Поле пусте або нечисло або відємне число"]
        })


pages_views=[PageView("home.html",links=pages,callback_dinamic_params=draw_home),
           PageView("personal_office.html",links=pages
                    ,callback_dinamic_params=draw_personall_data),
           PageView("rating.html",links=pages,callback_dinamic_params=draw_rating),
           PageView("activity.html",links=pages,callback_dinamic_params=draw_activity),
           PageView("shop.html",links=pages,
                    callback_dinamic_params=draw_shop)]

for i in range(len(pages)):
    pages[i]["view"]=pages_views[i]

