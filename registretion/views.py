from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .forms import RegistaritionForm
from random import randint
from django.core.mail import send_mail
from verification.models import UserVerification
from django.db.models import Q
from dinamic_view.views import PageView
from django.contrib.auth import authenticate, login
from .models import MyUser
class IndexView(TemplateView):
    template_name = "base.html"

        
   
class UserRegistrationsView(View):
    def __save_user(self,code,form_data):
        UserVerification.objects.filter(username=form_data["username"]).delete()
        UserVerification.objects.create(code=code, 
                                            email=form_data["email"], 
                                            password=form_data["password1"],
                                            username=form_data["username"])
    def __send_mail(self,code,request):
        send_mail(
                "Код підтвердження",
                f"Ваш код підтвердження: {code}",
                "bodakogut1000@gmail.com",
                [request.POST["email"]]
        )
    def post(self, request, *args, **kwargs):
        code=str(randint(100000,999999))
        form = RegistaritionForm(request.POST)
        if form.is_valid():
            request.session["form_data"]=form.cleaned_data
            self.__send_mail(code, request)
            self.__save_user(code, form.cleaned_data)
            return JsonResponse({"page":"/check_code"},status=200)
        return JsonResponse({"errors":form.errors},status=400)
    

class AurhorizationView(View):
    def post(self, request, *args, **kwargs):
        username=request.POST["username"]
        password=request.POST["password1"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session["user_id"]=MyUser.objects.get(username=username).id
            return JsonResponse({"page":"/personal_office"},status=200)
        return JsonResponse({"errors":{
            "username":["Невірний логін"],
            "password1":[" або невірний пароль"]
        }},status=400)


registrationView=PageView("form-registaration.html",title="Регістрація",
                                         url="save_user_bd/", 
                                         text="Реєстрація",
                                         text_link="Вхід",
                                         link="autorization/",
                                         callback_redirect=lambda request:(request.session.get("user_id"),"/personal_office"))

authorizationView=PageView("form-autorization.html",title="Авторизація",  
                                          text_link="Реєстрація",
                                          url="login/",
                                          text="Вхід",
                                          link="registration/")

