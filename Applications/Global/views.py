import json
from django.http import HttpResponse
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.views import View

# Create your views here.



class Token(View):

    def get(self,request):
        token = get_token(request)
        return HttpResponse(json.dumps({'token': token}), content_type="application/json,charset=utf-8")