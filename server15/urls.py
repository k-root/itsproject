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
from data import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^admin/', admin.site.urls),                                                   #admin site to add, update or delete data
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),     
    url(r'^house/', views.houselist, name= 'houselist'),                                #get all house table data
    url(r'^cropinfo/', views.cropinfolist, name= 'cropinfolist'),
    url(r'^farmer/',views.farmerlist, name= 'farmerlist'),                              #get all farmer table data
    url(r'^farm/',views.farmlist, name= 'farmlist'),                                    #get all farm table data
    url(r'^farmpoints/',views.farmpointslist, name= 'farmpointslist'),                  #get all farmpoints table data
    url(r'^wells/',views.wellslist, name= 'wellslist'),                                 #get all wells table data
    url(r'^publicplaces/',views.publicplaceslist, name= 'publicplaceslist'),            #get all publicplaces table data
    url(r'^members/',views.memberslist, name= 'memberslist'),                           #get all members table data
    url(r'^crop/',views.croplist, name= 'croplist'),                                    #get all crop table data
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)                  #add static url to get media (photos, audio clips)
