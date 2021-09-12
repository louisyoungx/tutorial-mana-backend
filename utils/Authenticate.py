from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.http import JsonResponse
from django.shortcuts import HttpResponse
import hashlib
import time


class Myauthentication(BaseAuthentication):
    '''认证类'''

    def authenticate(self, request):
        token = request._request.GET.get("token")
        token_obj = models.member_token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user, token_obj)  # 这里返回值一次给request.user,request.auth

    def authenticate_header(self, request):
        pass


def make_token(user):
    ctime = str(time.time())
    hash = hashlib.md5(user.encode("utf-8"))
    hash.update(ctime.encode("utf-8"))
    return hash.hexdigest()


class AuthView(APIView):
    """登录认证"""

    def dispatch(self, request, *args, **kwargs):
        return super(AuthView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse('get is ok')

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': "登录成功", 'token': None}
        try:
            user = request._request.POST.get("username")
            pwd = request._request.POST.get("password")
            obj = models.member.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = "用户名或密码错误"
            else:
                token = make_token(user)
                models.member_token.objects.update_or_create(user=obj, defaults={"token": token})
                ret['token'] = token
        except exceptions as e:
            ret['code'] = 1002
            ret['msg'] = "请求异常"

        return JsonResponse(ret)


class OrderView(APIView):
    """查看订单信息"""

    authentication_classes = [Myauthentication, ]  # 添加认证

    def get(self, request, *args, **kwargs):
        # request.user
        # request.auth
        ret = {'code': 1003, 'msg': "你的订单已经完成", 'data': "买了一个媳妇"}
        return JsonResponse(ret, safe=True)