from django.urls import path
from . import viewsets
from rest_framework.routers import DefaultRouter

app_name = "rooms"

router = DefaultRouter()
router.register("", viewsets.RoomViewset, basename="room")


urlpatterns = router.urls
