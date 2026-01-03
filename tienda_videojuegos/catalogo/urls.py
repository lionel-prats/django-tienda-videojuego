from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_juegos, name="lista_juegos"),
    # path('contacto/', views.contacto, name="contacto"),
]