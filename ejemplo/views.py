from django.shortcuts import render
from ejemplo.models import Familiar

# Create your views here.
def index(request):
    return render(request, "ejemplo/saludar.html",
    {"nombre":"Yoni",
    "apellido": "Riffo",
    })

def index_2(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html",
    {"nombre":nombre,
    "apellido": apellido,
    })

def index_3(request):
    return render(request, "ejemplo/saludar.html",
    {"notas":[1,2,3,4,5,6,7,8]}
    )

def imc (request,peso,altura):
    peso_en_kilos=peso/100
    altura_en_metros=altura/100
    imc= peso_en_kilos/(altura_en_metros*altura_en_metros) #calcular el imc
    return render (request, "ejemplo/imc.html",{"imc": imc})

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", 
                {"lista_familiares": lista_familiares})