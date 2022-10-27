"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import (FamiliarList, index, index_2, index_3,imc, 
                            mostrar_familiares,BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
from blog.views import index as blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
    path('saludar/<nombre>/<apellido>/',index_2),
    path('mostrar-notas/',index_3),
    path('calculo-imc/<int:peso>/<int:altura>/',imc),
    path('mi-familia/', mostrar_familiares), # nueva vista
    path('blog/', blog_index),
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/alta', AltaFamiliar.as_view()), # NUEVA RUTA PARA dar de alta FAMILIAR 
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()), # NUEVA RUTA PARA actualizar FAMILIAR
    path('panel-familia/crear/',FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
     path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
]