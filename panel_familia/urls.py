from django.urls import path
from panel_familia.views import FamilyList, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar

urlpatterns= [
    path('', FamiliarList.as_view(), name="familiar-list"), # NUEVA RUTA PARA actualizar FAMILIAR
    path('crear',FamiliarCrear.as_view(),name="familiar-crear"),
    path('<int:pk>/borrar', FamiliarBorrar.as_view(), name="familiar-borrar"),
    path('<int:pk>/actualizar', FamiliarActualizar.as_view(), name="familiar-actualizar"),
    path('family', FamilyList.as_view(), name="family"),
]