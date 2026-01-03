from catalogo.models import Juego  # ajustá el import si el modelo está en otra app

juegos = [
    {'nombre': 'Dogo Racing', 'precio': 29.99, 'plataforma': 'PC, PS5, Xbox Series X'},
    {'nombre': 'Platform', 'precio': 14.99, 'plataforma': 'PC, Switch'},
    {'nombre': 'Urban Darkness', 'precio': 39.99, 'plataforma': 'PC, PS5'},
]

for juego in juegos:
    Juego.objects.create(**juego)

print("✅ Juegos insertados correctamente")