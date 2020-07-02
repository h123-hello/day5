from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle
from api.authentications import MyAuth
from api.permissions import MyPermission
from api.throttle import SendMessageRate
from api.models import User
from utils.response import APIResponse


# Create your views here.
class TestAPIView(APIView):
    authentication_classes = [MyAuth]

    def get(self, request, *args, **kwargs):
        user = User.objects.first()
        return APIResponse("OK")


class TextPermissionAPIView(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return APIResponse("登陆访问成功")


class UserLoginOrReadOnly(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")


class SenMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")
