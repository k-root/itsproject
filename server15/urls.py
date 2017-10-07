"""server15 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from data.models import *
from django.conf import settings
from django.conf.urls.static import static

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^house/', views.housetable, name= 'housetable'),
    url(r'^farmer/',views.farmertable, name= 'farmertable'),
    url(r'^farm/',views.farmtable, name= 'farmtable'),
    url(r'^farmpoints/',views.farmpointstable, name= 'farmpointstable'),
    url(r'^wells/',views.wellstable, name= 'wellstable'),
    url(r'^publicplaces/',views.publicplacestable, name= 'publicplacestable'),
    url(r'^members/',views.memberstable, name= 'memberstable'),
    url(r'^crop/',views.croptable, name= 'croptable'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
