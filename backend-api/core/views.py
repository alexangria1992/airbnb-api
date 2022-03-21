from django.shortcuts import render
from django.core import serializers
from rooms.models import Room
from django.http import HttpResponse
# Create your views here.
def list_rooms(request):
    data = serializers.serialize("json",Room.objects.all())
    # print(rooms)
    response = HttpResponse(content=data)
    return response