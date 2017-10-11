from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions,renderers,viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# Create your views here.

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))     
@csrf_exempt                                                        #REQUEST EXEMPTION FROM csrf ERRORS
def farmerlist(request):
    farmer=Farmer.objects.all()                                     #SELECT THE WHOLE DATA IN FARMER TABLE
    farmer=FarmerSerializer(farmer,many=True)                       #SERIALIZE THE DATA
    return JsonResponse(farmer.data, status=201,safe=False)         #GIVE OUT AS JSON RESPONSE
  
 
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt                                                        #REQUEST EXEMPTION FROM csrf ERRORS
def farmlist(request):
    farm=Farm.objects.all()                                         #SELECT THE WHOLE DATA IN FARM TABLE
    farm=FarmSerializer(farm, many=True)                            #SERIALIZE THE DATA
    return JsonResponse(farm.data,status=201,safe=False)            #GIVE OUT AS JSON RESPONSE


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt                                                        #REQUEST EXEMPTION FROM csrf ERRORS
def houselist(request):
    house=House.objects.all()                                       #SELECT THE WHOLE DATA IN HOUSE TABLE
    house=HouseSerializer(house, many=True)                         #SERIALIZE THE DATA
    return JsonResponse(house.data,status=201,safe=False)           #GIVE OUT AS JSON RESPONSE
  

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt                                                        #REQUEST EXEMPTION FROM csrf ERRORS
def publicplaceslist(request):
#  if request.method == 'POST':
    publicplaces=PublicPlaces.objects.all()                         #SELECT THE WHOLE DATA IN PUBLICPLACES TABLE
    publicplaces=PublicPlacesSerializer(publicplaces, many=True)    #SERIALIZE THE DATA
    return JsonResponse(publicplaces.data, status=201, safe=False)  #GIVE OUT AS JSON RESPONSE
  

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt                                                        #REQUEST EXEMPTION FROM csrf ERRORS
def croplist(request):
 # if request.method =='POST':
    crop=Crop.objects.all()                                         #SELECT THE WHOLE DATA IN CROP TABLE
    crop=CropSerializer(crop,many=True)                             #SERIALIZE THE DATA
    return JsonResponse(crop.data, status=201, safe=False)          #GIVE OUT AS JSON RESPONSE


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt                                                        #REQUEST EXEMPTION FROM csrf ERRORS
def memberslist(request):
 # if request.method == 'POST':
    members=Members.objects.all()                                   #SELECT THE WHOLE DATA IN MEMBERS TABLE
    members=MembersSerializer(members, many=True)                   #SERIALIZE THE DATA
    return JsonResponse(members.data, status=201, safe=False)       #GIVE OUT AS JSON RESPONSE


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt                                                        #REQUEST EXEMPTION FROM csrf ERRORS
def farmpointslist(request):
  #if request.method == 'POST':
    farmpoints= Farmpoints.objects.all()                           #SELECT THE WHOLE DATA IN FARMPOINTS TABLE
    farmpoints= FarmpointsSerializer(farmpoints, many=True)        #SERIALIZE THE DATA
    return JsonResponse(farmpoints.data, status=201, safe=False)   #GIVE OUT AS JSON RESPONSE


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt                                                       #REQUEST EXEMPTION FROM csrf ERRORS
def wellslist(request):
#  if request.method == 'POST':
    wells= Wells.objects.all()                                     #SELECT THE WHOLE DATA IN WELLS TABLE
    wells= WellsSerializer(wells, many=True)                       #SERIALIZE THE DATA
    return JsonResponse(wells.data, status=201, safe=False)        #GIVE OUT AS JSON RESPONSE


