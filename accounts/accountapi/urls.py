from django.urls import path, re_path
from rest_framework import routers 
from django.conf.urls import include
from .views import UserViewSet

from django.views.decorators.csrf import csrf_exempt

app_name = "auth"

router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]