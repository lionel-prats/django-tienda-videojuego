#!/bin/bash

# Verificar que exista el entorno virtual
if [ ! -f "env/Scripts/activate" ]; then
    echo "❌ No se encontró el entorno virtual en 'env'"
    exit 1
fi

# Activar entorno virtual
source env/Scripts/activate
echo "✅ Entorno virtual activado"

# Verificar que exista manage.py
if [ ! -f "tienda_videojuegos/manage.py" ]; then
    echo "❌ No se encontró manage.py (ejecutá el script desde la raíz del proyecto)"
    exit 1
fi

# Levantar servidor de desarrollo
echo "🚀 Iniciando servidor de desarrollo..."
python tienda_videojuegos/manage.py runserver 9000