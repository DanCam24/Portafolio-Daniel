from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Proyecto
# Create your views here.

@login_required
def proyectos(request):
    mis_proyectos = Proyecto.objects.all()
    return render (request,"pages/proyectos.html",{"proyectos":mis_proyectos})