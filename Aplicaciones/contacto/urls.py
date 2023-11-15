from django.urls import path
from . import views 

urlpatterns = [
    path("contact/", views.contacto, name="Contacto"),
    path("enviado/", views.contacto, name="Enviado"),
]