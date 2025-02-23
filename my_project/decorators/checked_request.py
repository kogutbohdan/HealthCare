from django.shortcuts import redirect

def check_request(f):
    def wrapper(self,request, *args, **kwargs):
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return f(self,request, *args, **kwargs)
        return redirect("/")
    return wrapper