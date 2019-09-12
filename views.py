from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import IND_adm1,newwater
# Create your views here.


class HomePageView(TemplateView):
	template_name = 'login.html'
	
def ind_datasets(request):
	ind_adm1 = serialize('geojson', IND_adm1.objects.all())
	return HttpResponse(ind_adm1,content_type='json')

def newwater_datasets(request):
	water = serialize('geojson', newwater.objects.all())
	return HttpResponse(water,content_type='json')
def index(request):
	return render_to_response("index.html")

