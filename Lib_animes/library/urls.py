from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from anime.api.viewsets import AnimeViewSet

route = routers.DefaultRouter()
route.register(r'anime',AnimeViewSet,basename="anime")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
