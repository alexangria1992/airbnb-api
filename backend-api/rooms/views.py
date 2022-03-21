from rest_framework.generics import ListAPIView
from .models import Room
from .serializers import RoomSerializer
# Create your views here.


class ListRoomsView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
