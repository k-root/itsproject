from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from data.models import Farmer, Farm, House, Farmpoints, Crop, Wells, Members,PublicPlaces
from .serializers import HouseSerializer, MembersSerializer, PublicPlacesSerializer, WellsSerializer, FarmSerializer, CropSerializer, FarmerSerializer, FarmpointsSerializer

# Create your views here.
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def farmerlist(request):
  if request.method== 'POST'
