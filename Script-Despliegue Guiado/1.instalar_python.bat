@echo off

REM Comprobar si Python ya esta instalado
python --version > nul 2>&1
if %errorlevel% equ 0 (
    echo Python ya esta instalado.
    pause
    exit /b
)

REM Mostrar la ruta actual para depuracion
echo Ruta actual: %cd%

REM Verificar si el instalador de Python existe en la ruta especificada
if not exist "python-3.12.5-amd64.exe" (
    echo No se encontro el instalador de Python en la ubicacion especificada.
    pause
    exit /b
)

REM Ejecutar el instalador de Python en modo silencioso
echo Instalando Python...
"python-3.12.5-amd64.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1

REM Esperar unos segundos para que la instalacion termine
timeout /t 10 > nul

REM Verificar si Python se instalo correctamente
echo Verificando la instalacion de Python...
where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python no se encontro en el PATH.
    echo Asegurate de que la instalacion se completo correctamente.
    pause
    exit /b
)

echo Instalacion completada con exito.
pause
