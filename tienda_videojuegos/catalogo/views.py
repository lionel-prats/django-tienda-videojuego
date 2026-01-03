from django.shortcuts import render

def lista_juegos(request):
    juegos = [
        {'nombre': 'Dogo Racing', 'precio': 29.99, 'plataforma': 'PC, PS5, Xbox Series X'},
        {'nombre': 'Platform', 'precio': 14.99, 'plataforma': 'PC, Switch'},
        {'nombre': 'Urban Darkness', 'precio': 39.99, 'plataforma': 'PC, PS5'},
        {'nombre': 'Highspeed', 'precio': 49.99, 'plataforma': 'PC, Xbox Series X'},
        {'nombre': 'Night Mode', 'precio': 19.99, 'plataforma': 'PC, PS4, Xbox One'},
        {'nombre': 'The Grand Thief', 'precio': 59.99, 'plataforma': 'PC, PS5, Xbox Series X'},
        {'nombre': 'Sunset Vibe', 'precio': 24.99, 'plataforma': 'PC, Switch, Mobile'},
        {'nombre': 'Dark Whispers', 'precio': 34.99, 'plataforma': 'PC, PS5, Xbox Series X'},
        {'nombre': 'Space Zero', 'precio': 44.99, 'plataforma': 'PC, PS5'},
        {'nombre': 'Medieval Saga', 'precio': 54.99, 'plataforma': 'PC, Xbox Series X, Switch'}
    ]
    contexto_catalogo_juegos = {'lista_juegos': juegos}
    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)