from registretion.models import MyUser
from .models import ShopModel

def draw_personall_data(request,params):
    user=MyUser.objects.get(id=request.session.get("user_id"))
    params["rating"]=user.rating
    params["username"]=user.username
    params["weight"]=user.weight
    params["height"]=user.height
    params["aime"]=user.aime
    params["things"]=list(user.things.all())
    params["icon"]=user.icon.url

def draw_shop(request,params):
    user=MyUser.objects.get(id=request.session.get("user_id"))
    icons_list=list(ShopModel.objects.all())
    icons_list=list(filter(lambda icon:icon not in user.things.all(),icons_list))
    params["many"]=user.many
    params["icons"]=icons_list