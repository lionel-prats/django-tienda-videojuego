#!/bin/bash

if [ ! -f "env/Scripts/activate" ]; then
    echo "❌ No se encontro el entorno virtual en 'env'"
    exit 1
fi

source env/Scripts/activate
echo "✅ Entorno virtual activado"
