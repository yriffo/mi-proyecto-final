from django.shortcuts import render
from blog.models import Configuracion

# Create your views here.
def index(request):
    configuracion = Configuracion.objects.first()
    return render (request, 'blog/index.html',{'configuracion': configuracion})