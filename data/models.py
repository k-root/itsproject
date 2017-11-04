from django.contrib.gis.db import models

# Create your models here
class Farmer(models.Model):
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=6)
    DoB=models.DateField()
    Aadhar=models.CharField(max_length=12)
    Number=models.CharField(max_length=10)
    Income=models.IntegerField()
    Photo=models.CharField(max_length=70)
    Audio=models.FileField(blank=True)

    def __str__(self):
        return self.Name                                                                    #REFERENCE THIS AS ID IN DJANGO ADMIN

class House(models.Model):
    Poi=models.PointField(default="")
    NoP=models.IntegerField()
    F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)
    Village=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.F_id.Name                                                               #REFERENCE THIS AS ID IN DJANGO ADMIN

class Members(models.Model):
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=7)
    DoB=models.DateField()
    Aadhar=models.CharField(max_length=12)
    Photo=models.CharField(max_length=50)
    Relation=models.CharField(max_length=12)
    Audio=models.FileField(blank=True)
    F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name                                                                   #REFERENCE THIS AS ID IN DJANGO ADMIN

class PublicPlaces(models.Model):
    Poi=models.PointField(default="")
    Type=models.CharField(max_length=20)
    Name=models.CharField(max_length=30)
    Village=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.Name                                                                    #REFERENCE THIS AS ID IN DJANGO ADMIN

class Farm(models.Model):
    Area=models.FloatField()
    Income=models.IntegerField()
    F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)
    Village=models.CharField(max_length=20)

    def __str__(self):
        return self.F_id.Name + str(self.id)                                               #REFERENCE THIS AS ID IN DJANGO ADMIN

class Farmpoints(models.Model):
    Seqno=models.IntegerField()
    Polygon=models.PolygonField(default="")
    Farm_id=models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.Farm_id.F_id.Name                                                     #REFERENCE THIS AS ID IN DJANGO ADMIN

class Wells(models.Model):
    Poi=models.PointField(default="")
    Depth=models.FloatField()
    Status=models.BooleanField()
    AvgYield=models.FloatField()
    Photo=models.CharField(max_length=70)
    Farm_id=models.ForeignKey(Farm, on_delete=models.CASCADE)
    Village=models.CharField(max_length=20, default="")
    
    def __str__(self):
        return self.Farm_id.Village                                                      #REFERENCE THIS AS ID IN DJANGO ADMIN

    
class CropInfo(models.Model):
    Name=models.CharField(max_length=20)
    month1=models.FloatField()
    month2=models.FloatField()
    month3=models.FloatField()
    month4=models.FloatField()
    month5=models.FloatField()
    month6=models.FloatField()
    month7=models.FloatField()
    month8=models.FloatField()
    month9=models.FloatField()
    imagelink=models.CharField(max_length=200,default="")
    
    def __str__(self):
        return self.Name
    
class Crop(models.Model):
    Season=models.CharField(max_length=10)
    Year=models.IntegerField()
    Name=models.CharField(max_length=20)
    Percentage=models.FloatField()
    Income=models.IntegerField()
    Photo=models.CharField(max_length=70)
    Farm_id=models.ForeignKey(Farm, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Farm_id.F_id.Name + str(self.id)                                     #REFERENCE THIS AS ID IN DJANGO ADMIN

 class Store(models.model):
    Name=models.CharField(max_length=20)
    Category=models.CharField(max_length=20)
    Price=models.IntegerField()
    Availability=models.BooleanField()
    Img=models.CharField(max_length=200, default="")
    
    def __str__(self):
        return self.Name + str(self.Category)
