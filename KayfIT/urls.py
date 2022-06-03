"""KayfIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.auth import views as authViews
from django.conf import settings
from restik import views
from restik.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('exit/', authViews.LogoutView.as_view(next_page='home'), name='exit'),
    path('basket/', views.basket, name='basket'),
    path('profile/', views.profileuser, name='profileuser'),
    path('payment/', views.payment, name='payment'),

    # Restik
    path('', views.home, name='home'),
    path('current/', views.currentrestik, name='currentrestik'),
    re_path('map/', views.mapbox_map,  name='main'),

    # REST
    path('api/v1/product/', views.ProductAPIList.as_view()),
    path('api/v1/client/', views.ClientAPIList.as_view()),
    path('api/v1/order/', views.OrderAPIList.as_view()), # TODO need to fix, cant add an order
    path('api/v1/menu/', views.MenuAPIList.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth-token/', include('djoser.urls.authtoken')),
    path('api/v1/user/', include('user.urls')),


]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Добавить наличие продукта
# Изменить restriction_age to DateField or DateTimeField
# TODO авторизация REST API 
# Фикс багов ( добавить заказ, продукт )
# 