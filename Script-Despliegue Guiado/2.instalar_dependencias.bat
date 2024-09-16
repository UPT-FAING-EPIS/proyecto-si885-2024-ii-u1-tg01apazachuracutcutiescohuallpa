@echo off
:: Comprueba si el script tiene privilegios de administrador
:: Si no los tiene, pide la elevación a administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requiere permisos de administrador. Intentando ejecutar con elevación...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Inicia la instalación de dependencias
echo Instalando dependencias de Python...

:: Instalación de psutil
pip install psutil

:: Instalación de mysql-connector-python
pip install mysql-connector-python

echo Instalación completa.
pause
