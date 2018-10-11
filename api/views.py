from django.shortcuts import render
#from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializer import UserSerializer
from users.models import Users




class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.filter(user_type = Users.executor)
    serializer_class = UserSerializer


class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.filter(user_type = Users.purchaser)
    serializer_class = UserSerializer
