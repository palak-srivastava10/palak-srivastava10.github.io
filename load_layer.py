import os
from django.contrib.gis.utils import LayerMapping
from .models import IND_adm1,newwater
ind_adm1_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'type_1': 'TYPE_1',
    'engtype_1': 'ENGTYPE_1',
    'nl_name_1': 'NL_NAME_1',
    'varname_1': 'VARNAME_1',
    'geom': 'MULTIPOLYGON',
}

IND_adm1_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/IND_adm1.shp'))

def run(verbose=True):
    lm = LayerMapping(IND_adm1,IND_adm1_shp,ind_adm1_mapping,transform=False)
    lm.save(strict=True,verbose=verbose)


newwater_mapping = {
    'serial': 'serial',
    'field_2': 'field_2',
    'field_3': 'field_3',
    'field_4': 'field_4',
    'district': 'district',
    'town': 'town',
    'area': 'area',
    'lat': 'lat',
    'lon': 'lon',
    'x': 'x',
    'y': 'y',
    'pre_1': 'pre_1',
    'pre_2': 'pre_2',
    'pre_3': 'pre_3',
    'pre_4': 'pre_4',
    'pre_5': 'pre_5',
    'pre_6': 'pre_6',
    'pre_7': 'pre_7',
    'pre_8': 'pre_8',
    'pre_9': 'pre_9',
    'pre_10': 'pre_10',
    'pre_11': 'pre_11',
    'pre_12': 'pre_12',
    'pre_13': 'pre_13',
    'pre_14': 'pre_14',
    'pre_15': 'pre_15',
    'pre_16': 'pre_16',
    'pre_17': 'pre_17',
    'pre_18': 'pre_18',
    'pre_19': 'pre_19',
    'pre_20': 'pre_20',
    'pre_21': 'pre_21',
    'pre_22': 'pre_22',
    'pre_23': 'pre_23',
    'geom': 'MULTIPOINT',
}

newwater_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data1/newwater.shp'))

def run(verbose=True):
    lm = LayerMapping(newwater,newwater_shp,newwater_mapping,transform=False)
    lm.save(strict=True,verbose=verbose)

