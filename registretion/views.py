from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .forms import RegistaritionForm
from random import randint
from django.core.mail import send_mail
from verification.models import UserVerification
from django.db.models import Q
from dinamic_view.views import PageView

class IndexView(TemplateView):
    template_name = "base.html"

        
   
class UserRegistrationsView(View):
    def __save_user(self,code,form_data):
        UserVerification.objects.filter(username=form_data["username"]).delete()
        UserVerification.objects.create(code=code, 
                                            email=form_data["email"], 
                                            password=form_data["password1"],
                                            username=form_data["username"])
    def post(self, request, *args, **kwargs):
        code=str(randint(100000,999999))
        form = RegistaritionForm(request.POST)
        if form.is_valid():
            request.session["form_data"]=form.cleaned_data
            send_mail(
                "Код підтвердження",
                f"Ваш код підтвердження: {code}",
                "bodakogut1000@gmail.com",
                [request.POST["email"]]
            )
            self.__save_user(code, form.cleaned_data)
            return JsonResponse({"page":"/check_code"},status=200)
        return JsonResponse({"errors":form.errors},status=400)


registrationView=PageView("form-registaration.html",title="Регістрація",
                                         url="save_user_bd/", 
                                         text="Реєстрація",
                                         text_link="Вхід",
                                         link="autorization/")

authorizationView=PageView("form-autorization.html",title="Авторизація",  
                                          text_link="Реєстрація",
                                          text="Вхід",
                                          link="registration/")

