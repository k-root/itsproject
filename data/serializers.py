from data.models import *
from rest_framework import serializers

class FarmerSerializer(serializers.ModelSerializer):
  class Meta:
    model= Farmer         #TAKE FARMER MODEL
    fields='__all__'      #TAKE ALL FIELDS FROM THE TABLE
    
class CropInfoSerializer(serializers.ModelSerializer):
  class Meta:
     model=CropInfo
     fields='__all__'
        
class FarmSerializer(serializers.ModelSerializer):
  class Meta:
    model= Farm           #TAKE FARM MODEL
    fields='__all__'      #TAKE ALL FIELDS FROM THE TABLE
    
class HouseSerializer(serializers.ModelSerializer):
  class Meta:
    model= House          #TAKE HOUSE MODEL
    fields='__all__'      #TAKE ALL FIELDS FROM THE TABLE
    

class FarmpointsSerializer(serializers.ModelSerializer):
  class Meta:
    model= Farmpoints     #TAKE FARMPOINTS MODEL
    fields='__all__'      #TAKE ALL FIELDS FROM THE TABLE


class WellsSerializer(serializers.ModelSerializer):
  class Meta:
    model= Wells          #TAKE WELLS MODEL
    fields='__all__'      #TAKE ALL FIELDS FROM THE TABLE
    

class CropSerializer(serializers.ModelSerializer):
  class Meta:
    model= Crop           #TAKE CROP MODEL
    fields='__all__'      #TAKE ALL FIELDS FROM THE TABLE


class MembersSerializer(serializers.ModelSerializer):
  class Meta:
    model= Members        #TAKE MEMBERS MODEL
    fields='__all__'      #TAKE ALL FIELDS FROM THE TABLE
    
class PublicPlacesSerializer(serializers.ModelSerializer):
  class Meta:
    model= PublicPlaces    #TAKE PUBLICPLACES MODEL
    fields='__all__'      #TAKE ALL FIELDS FROM THE TABLE
