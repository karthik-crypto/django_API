from django.shortcuts import render
from rest_framework import viewsets
from .models import lang
from lang import serializers

class langview(viewsets.ModelViewSet):
    queryset = lang.objects.all()
    serializer_class = serializers.langserializer

    

