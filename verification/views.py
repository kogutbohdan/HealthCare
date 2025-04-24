from django.shortcuts import redirect
from django.views.generic import  View
from decorators.checked_request import*
from dinamic_view.views import PageView
from registretion.forms import RegistaritionForm
from .models import UserVerification
from django.http import JsonResponse

class ToBackView(View):
    @check_request
    def get(self, request, *args, **kwargs):
        if "form_data" in request.session:
            del request.session["form_data"]
        return redirect("/registration/")
    
class UserVerificationView(View):
    def post(self, request, *args, **kwargs):
        form=RegistaritionForm(request.session.get("form_data"))
        user=UserVerification.objects.filter(username=request.session.get("form_data")["username"],code=request.POST["code"])
        if user.exists():
            request.session["user_id"]=form.save().id
            user.delete()
            del request.session["form_data"]
            return JsonResponse({"page":"/personal_office"},status=200)
        return JsonResponse({"errors":{
            "code":["Невірний код"]
        }},status=400)


formVarificationView = PageView("form_varification.html",text="Відправити",url="verification_code/")
