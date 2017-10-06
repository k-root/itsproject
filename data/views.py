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

def farmerlist(request):
  if request.method == 'POST':
    farmer=Farmer.objects.all()
    farmer=FarmerSerializer(farmer,many=True)
    return JSONResponse(farmer.farmer, status=201,safe=False)
  
def farmlist(request):
  if request.method == 'POST':
    farm=Farm.objects.all()
    farm=FarmSerializer(farm, many=True)
    return JSONResponse(farm.farm,status=201,safe=False)

def houselist(request):
  if request.method =='POST':
    house=House.objects.all()
    house=HouseSerializer(house, many=True)
    return JSONResponse(house.house,status=201,safe=False)
  
def publicplaceslist(request):
  if request.method == 'POST':
    publicplaces=PublicPlaces.objects.all()
    publicplaces=PublicPlacesSerializer(publicplaces, many=True)
    return JSONResponse(publicplaces.publicplaces, status=201, safe=False)
  
def croplist(request):
  if request.method =='POST':
    crop=Crop.objects.all()
    crop=CropSerializer(crop,many=True)
    return JSONResponse(crop.crop, status=201, safe=False)
  
def memberslist(request):
  if request.method == 'POST':
    members=Members.objects.all()
    members=MembersSerializer(members, many=True)
    return JSONResponse(members.members, status=201, safe=False)
  
def farmpointslist(request):
  if request.method == 'POST':
    farmpoints= Farmpoints.objects.all()
    farmpoints= FarmpointsSerializer(farmpoints, many=True)
    return JSONResponse(farmpoints.farmpoints, status=201, safe=False)
  
def wellslist(request):
  if request.method == 'POST':
    wells= Wells.objects.all()
    wells= WellsSerializer(wells, many=True)
    return JSONResponse(wells.wells, status=201, safe=False)
