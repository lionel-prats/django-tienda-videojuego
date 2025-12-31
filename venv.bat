@echo off
REM Activa el entorno virtual Python ubicado en la carpeta "env"

IF NOT EXIST env\Scripts\activate.bat (
    echo ❌ No se encontro el entorno virtual en la carpeta "env"
    pause
    exit /b
)

call env\Scripts\activate.bat

echo ✅ Entorno virtual activado
cmd /k
