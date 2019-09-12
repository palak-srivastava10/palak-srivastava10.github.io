from django.contrib import admin
from .models import Incidences, IND_adm1,newwater
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    #pass
    list_display = ('name','location')

class IND_adm1Admin(LeafletGeoAdmin):
    #pass
    list_display = ('name_1','id_1')

class newwaterAdmin(LeafletGeoAdmin):
    #pass
    list_display = ('town','area')


admin.site.register(Incidences,IncidencesAdmin)
admin.site.register(IND_adm1,IND_adm1Admin)
admin.site.register(newwater,newwaterAdmin)
