from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import userapi
from.serializers import userapiserializer

# Create your views here.
class userapiviewset(ModelViewSet):
    serializer_class = userapiserializer
    queryset = userapi.objects.all()
