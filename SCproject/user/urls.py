from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
		path('', views.index, name ='index'),
        path('creditForm/',views.creditForm_page,name='creditForm'),
        path('Dashboard/',views.Dashboard_page,name='Dashboard')
        
]
