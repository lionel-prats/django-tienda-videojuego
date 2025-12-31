from django.shortcuts import render

# vista de la pagina principal
def index(request):
    return render(
        request,
        'home/index.html',
    )

# vista de la pagina de contacto
def contacto(request):
    return render(
        request,
        'home/contacto.html',
    )
