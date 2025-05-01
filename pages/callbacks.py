from registretion.models import MyUser
from .models import*

def draw_personall_data(request,params):
    user=MyUser.objects.get(id=request.session.get("user_id"))
    print(user.statistics_list())
    params["rating"]=user.rating
    params["username"]=user.username
    params["weight"]=user.weight
    params["height"]=user.height
    params["aime"]=user.aime
    params["things"]=list(user.things.all())
    params["icon"]=user.icon.url
    params["statistics_list"]=user.statistics_list()

def draw_shop(request,params):
    user=MyUser.objects.get(id=request.session.get("user_id"))
    icons_list=list(ShopModel.objects.all())
    icons_list=list(filter(lambda icon:icon not in user.things.all(),icons_list))
    params["many"]=user.many
    params["icons"]=icons_list

def draw_activity(request,params):
    user=MyUser.objects.get(id=request.session.get("user_id"))
    tasks=user.tasks.all()
    tasks_list=[]
    for task in list(tasks):
        tasks_list.append({"img":task.image.url,"text":task.text.split("."),
                           "many":task.many,"points":task.points,"id":task.id})
    params["tasks"]=tasks_list