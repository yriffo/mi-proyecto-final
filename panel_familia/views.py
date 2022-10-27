from django.shortcuts import render
from django.views.generic import ListView , CreateView, DeleteView, UpdateView # <----- NUEVO IMPORT
from ejemplo.models import Familiar
from panel_familia.models import Familiar as Family

class FamiliarList(ListView):
  model = Familiar

class FamilyList(ListView):
  model = Family

class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia" # cuando creo un familiar vuelvo a esta url
  fields = ["nombre", "direccion", "numero_pasaporte"]

class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]
