from decorators.checked_request import check_request
from django.shortcuts import render,redirect


class PageView:
    def __init__(self, path,callback_redirect=None,callback_dinamic_params=None, **params):
        self.path = path
        self.params = params
        self.callback_redirect=callback_redirect
        self.callback_dinamic_params=callback_dinamic_params

    
    def __view(self,request):
        if self.callback_redirect:
            is_redirect,url=self.callback_redirect(request)
            if is_redirect:return redirect(url)
        if self.callback_dinamic_params:self.callback_dinamic_params(request,self.params)
        return render(request, self.path,self.params)
        

    def as_view(self):
        new_view = lambda request:self.__view(request)
        return new_view