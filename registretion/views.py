from django.views.generic import TemplateView, View
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import RegistaritionForm
from my_project.decorators.checked_request import check_request
from random import randint
from django.core.mail import send_mail
from .models import MyUser
from django.db.models import Q

class IndexView(TemplateView):
    template_name = "base.html"


def create_view(path,**params):
    class AuthenticationView(View):
        @check_request
        def get(self, request, *args, **kwargs):
            return render(request, path,params)
    return AuthenticationView
    
        
   
class UserRegistrationsView(View):
    def post(self, request, *args, **kwargs):
        post=request.POST.copy()
        post["code"]=str(randint(100000,999999))
        form = RegistaritionForm(post)
        if form.is_valid():
            request.session["username"]=post["username"]
            send_mail(
                "Код підтвердження",
                f"Ваш код підтвердження: {post['code']}",
                "bodakogut1000@gmail.com",
                [post["email"]]
            )
            form.save()
            return JsonResponse({"page":"/check_code"},status=200)
        return JsonResponse(form.errors,status=400)

class ToBackView(View):
    @check_request
    def get(self, request, *args, **kwargs):
        print(request.session["username"])
        MyUser.objects.filter(username=request.session["username"]).filter(~Q(code="0")).delete()
        return redirect("/registration/")


RegistrationView=create_view("form.html",title="Регістрація", 
                                         registretion=True, 
                                         text="регістрація",
                                         function="registration")

AuthorizationView=create_view("form.html",title="Авторизація", 
                                          registretion=False, 
                                          text="авторизація")

FormVarificationView = create_view("form_varification.html",text="відправити")