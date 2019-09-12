from django.conf.urls import include,url
from reporter.views import HomePageView,ind_datasets,newwater_datasets,index

urlpatterns = [    
 url(r'^$',HomePageView.as_view(), name = 'home'),
url(r'^ind_adm1_data/$',ind_datasets, name = 'name_1'),
url(r'^newwater_data/$',newwater_datasets,name = 'area'),
url(r'^index.html/$',index,name = 'index'),

]

