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
@csrf_exempt
def farmerlist(request):
    farmer=Farmer.objects.all()
    farmer=FarmerSerializer(farmer,many=True)
    return JsonResponse(farmer.data, status=201,safe=False)
  
 
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def farmlist(request):
    farm=Farm.objects.all()
    farm=FarmSerializer(farm, many=True)
    return JsonResponse(farm.data,status=201,safe=False)


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def houselist(request):
    house=House.objects.all()
    house=HouseSerializer(house, many=True)
    return JsonResponse(house.data,status=201,safe=False)
  

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def publicplaceslist(request):
#  if request.method == 'POST':
    publicplaces=PublicPlaces.objects.all()
    publicplaces=PublicPlacesSerializer(publicplaces, many=True)
    return JsonResponse(publicplaces.data, status=201, safe=False)
  

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def croplist(request):
 # if request.method =='POST':
    crop=Crop.objects.all()
    crop=CropSerializer(crop,many=True)
    return JsonResponse(crop.data, status=201, safe=False)


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def memberslist(request):
 # if request.method == 'POST':
    members=Members.objects.all()
    members=MembersSerializer(members, many=True)
    return JsonResponse(members.data, status=201, safe=False)


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def farmpointslist(request):
  #if request.method == 'POST':
    farmpoints= Farmpoints.objects.all()
    farmpoints= FarmpointsSerializer(farmpoints, many=True)
    return JsonResponse(farmpoints.data, status=201, safe=False)


@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def wellslist(request):
#  if request.method == 'POST':
    wells= Wells.objects.all()
    wells= WellsSerializer(wells, many=True)
    return JsonResponse(wells.data, status=201, safe=False)
