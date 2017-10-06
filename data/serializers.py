from data.models import *
from rest_framework import serializers

class FarmerSerializer(serializers.ModelSerializer):
  class Meta:
    model= Farmer
    fields='__all__'
    
class FarmSerializer(serializers.ModelSerializer):
  class Meta:
    model= Farm
    fields='__all__'
    
class HouseSerializer(serializers.ModelSerializer):
  class Meta:
    model= House
    fields='__all__'
    

class FarmpointsSerializer(serializers.ModelSerializer):
  class Meta:
    model= Farmpoints
    fields='__all__'


class WellsSerializer(serializers.ModelSerializer):
  class Meta:
    model= Wells
    fields='__all__'
    

class CropSerializer(serializers.ModelSerializer):
  class Meta:
    model= Crop
    fields='__all__'


class MembersSerializer(serializers.ModelSerializer):
  class Meta:
    model= Members
    fields='__all__'
    
class PublicPlacesSerializer(serializers.ModelSerializer):
  class Meta:
    model= PublicPlaces
    fields='__all__'
