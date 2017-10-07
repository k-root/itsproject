from django.contrib.gis.db import models

# Create your models here
class Farmer(models.Model):
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=6)
    DoB=models.DateField()
    Aadhar=models.CharField(max_length=12)
    Number=models.CharField(max_length=10)
    Income=models.IntegerField()
    Photo=models.FileField(blank=True)
    Audio=models.FileField(blank=True)

    def __str__(self):
        return self.Name

class House(models.Model):
    Poi=models.PointField(default="")
    NoP=models.IntegerField()
    F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)
    Village=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.F_id.Name

class Members(models.Model):
    Name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=7)
    DoB=models.DateField()
    Aadhar=models.CharField(max_length=12)
    Photo=models.FileField(blank=True)
    Relation=models.CharField(max_length=12)
    Audio=models.FileField(blank=True)
    F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class PublicPlaces(models.Model):
    Poi=models.PointField(default="")
    Type=models.CharField(max_length=20)
    Name=models.CharField(max_length=30)
    Village=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.Name

class Farm(models.Model):
    Area=models.FloatField()
    Income=models.IntegerField()
    F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)
    Village=models.CharField(max_length=20)

    def __str__(self):
        return self.F_id.Name

class Farmpoints(models.Model):
    Seqno=models.IntegerField()
    Polygon=models.PolygonField(default="")
    Farm_id=models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        return self.Farm_id.F_id.Name

class Wells(models.Model):
    Poi=models.PointField(default="")
    Depth=models.FloatField()
    Status=models.BooleanField()
    AvgYield=models.FloatField()
    Photo=models.FileField()
    Farm_id=models.ForeignKey(Farm, on_delete=models.CASCADE)
    Village=models.CharField(max_length=20, default="")
    
    def __str__(self):
        return self.Farm_id.Village

class Crop(models.Model):
    Season=models.CharField(max_length=10)
    Year=models.IntegerField()
    Name=models.CharField(max_length=20)
    Percentage=models.FloatField()
    Income=models.IntegerField()
    Photo=models.FileField()
    Farm_id=models.ForeignKey(Farm, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Farm_id.F_id.Name + str(self.id)
