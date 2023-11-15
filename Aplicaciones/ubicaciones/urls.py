from django.urls import path
from . import views

urlpatterns = [ 
   path("ubicaciones/", views.sitios_interes, name="ubicaciones"),
]
