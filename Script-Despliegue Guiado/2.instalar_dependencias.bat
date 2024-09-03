@echo off

REM Verificar si Python está instalado
echo Verificando la instalación de Python...
where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python no se encontró en el PATH.
    echo Asegúrate de que Python esté instalado correctamente antes de ejecutar este script.
    pause
    exit /b
)

REM Actualizar pip e instalar dependencias necesarias
echo Instalando dependencias...
python -m pip install --upgrade pip
python -m pip install psutil
python -m pip install openpyxl

echo Instalación de dependencias completada con éxito.
pause
