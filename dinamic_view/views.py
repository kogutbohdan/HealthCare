from decorators.checked_request import check_request
from django.shortcuts import render
from django.views import View

class PageView:
    def __init__(self, path, **params):
        self.path = path
        self.params = params
    def as_view(self):
        view=check_request(lambda self,request:render(request, self.path,self.params))
        new_view = lambda request:view(self,request)
        return new_view