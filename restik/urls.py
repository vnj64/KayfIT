from django.urls import path, include
from . import views
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'title', views.MenuViewSet)
router.register(r'restriction_age', views.MenuViewSet)


urlpatterns = [
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^', include('shop.urls', namespace='shop')),
]