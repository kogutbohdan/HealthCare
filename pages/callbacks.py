from registretion.models import MyUser
from .models import ShopModel

def draw_personall_data(request,params):
    user=MyUser.objects.get(id=request.session.get("user_id"))
    params["rating"]=user.rating
    params["username"]=user.username
    params["weight"]=user.weight
    params["height"]=user.height
    params["aime"]=user.aime

def draw_shop(request,params):
    user=MyUser.objects.get(id=request.session.get("user_id"))
    icones=list(ShopModel.objects.all())
    params["many"]=user.many
    params["icons"]=icones