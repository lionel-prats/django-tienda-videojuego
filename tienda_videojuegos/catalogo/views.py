from django.shortcuts import render
from .models import Juego

def lista_juegos(request):
    juegos = Juego.objects.all() # querySet del ORM de Django
    contexto_catalogo_juegos = {'lista_juegos': juegos}
    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)