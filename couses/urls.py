from django.urls import path, include
from .api import coursesView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Courses',coursesView)

urlpatterns = [
    path('',include(router.urls)),
]