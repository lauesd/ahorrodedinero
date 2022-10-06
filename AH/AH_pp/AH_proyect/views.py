from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def PaginaPrincipal(request):
    return render(request, 'front-end/PaginaPrincipal.html')
def Iniciar_sesion(request):
    return render(request, 'front-end/Iniciar_sesion.html')
