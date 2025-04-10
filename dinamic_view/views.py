from decorators.checked_request import check_request
from django.shortcuts import render
from django.shortcuts import redirect

class PageView:
    def __init__(self, path,callback_redirect=None, **params):
        self.path = path
        self.params = params
        self.callback_redirect=callback_redirect

    
    def __view(self,request):
        if self.callback_redirect:
            is_redirect,url=self.callback_redirect(request)
            if is_redirect:return redirect(url)
        return render(request, self.path,self.params)
        

    def as_view(self):
        new_view = lambda request:self.__view(request)
        return new_view