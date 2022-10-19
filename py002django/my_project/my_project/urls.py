"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from my_app_1.views import my_view, MyFirstModelViewSet, vue_app_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-page/', my_view),  # http://127.0.0.1:8000/my-page/
    path('vue/', vue_app_view),  # http://127.0.0.1:8000/vue/
]

router = SimpleRouter()
router.register('api/my_app_1', MyFirstModelViewSet)

urlpatterns += router.urls

