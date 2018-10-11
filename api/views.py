from django.shortcuts import render
#from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializer import UserSerializer
from users.models import User




class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(user_type = User.purchaser)
    serializer_class = UserSerializer
