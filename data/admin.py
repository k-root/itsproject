from django.contrib.gis import admin
from .models import *

# Register your models here.

admin.site.register(Farmer)
admin.site.register(House,admin.GeoModelAdmin)
admin.site.register(Members)
admin.site.register(PublicPlaces,admin.GeoModelAdmin)
admin.site.register(Farm)
admin.site.register(Crop)
admin.site.register(Wells,admin.GeoModelAdmin)
admin.site.register(Farmpoints,admin.GeoModelAdmin)
