from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def biografia(request):
    return render(request,"pages/biografia.html",{})

def inicio(request):
    return render(request,"pages/inicio.html",{})

#def biografia(request):
#    return render(request,"pages/biografia.html",{})

@login_required
def contact(request):
    return render(request,"pages/contact.html",{})

def registro(request):
    return render(request,"registration/registro.html",{})