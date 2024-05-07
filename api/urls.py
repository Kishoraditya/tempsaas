from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pages', views.PageAPIViewSet, basename='pages')

urlpatterns = [
    path('', include(router.urls)),
]
