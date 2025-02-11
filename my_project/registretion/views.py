from django.shortcuts import render
from  django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def registretion(request):
    form_classes=[
        {"class":"registretion activation","text":"Реєстрація"},
        {"class":"avtorization","text":"Авторизація"}
    ]
    return render(request,"form.html",{"title":"Регістрація","form_classes":form_classes})