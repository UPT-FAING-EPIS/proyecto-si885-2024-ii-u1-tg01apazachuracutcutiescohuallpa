@echo off
:: Cambiar la codificación a UTF-8
chcp 65001 >nul

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
echo.

:: Obtener las direcciones IPv4 de los adaptadores de red
echo Listando las direcciones IPv4 disponibles...
setlocal EnableDelayedExpansion
set index=1
for /f "tokens=2 delims=:" %%A in ('ipconfig ^| findstr "Direcci.n IPv4"') do (
    set "ip[!index!]=%%A"
    echo !index!. %%A
    set /a index+=1
)

:: Agregar la opción 0 para ingresar la IP manualmente
echo 0. Ingresar IP manualmente

:: Bucle para pedir al usuario que elija una opción válida
:choose_ip
echo.
set /p choice=Elija el número de la dirección IPv4 que desea guardar en ip.txt (o presione ENTER para no crear el archivo):

:: Verificar si se ingresó un número válido
if "%choice%"=="0" (
    set /p manual_ip=Ingrese la dirección IP manualmente:
    set selected_ip=!manual_ip!
) else (
    if not defined ip[%choice%] (
        echo No se seleccionó una opción válida. Inténtelo nuevamente.
        goto choose_ip
    )
    set selected_ip=!ip[%choice%]!
)

:: Guardar la IP seleccionada en ip.txt en la misma ubicación del script
echo Guardando la dirección IP seleccionada en ip.txt...
echo %selected_ip% > "%~dp03/ip.txt"

:: Comprobar si el archivo fue creado correctamente
if exist "%~dp0ip.txt" (
    echo La dirección IP %selected_ip% ha sido guardada en ip.txt.
) else (
    echo Error: No se pudo crear el archivo ip.txt.
)

echo.
:: Selección de aula
echo Seleccione el aula:
echo 1. Lab_A (P306)
echo 2. Lab_B (P311)
echo 3. Lab_C (P310)
echo 4. Lab_D (Q302)
echo 5. Lab_E (Q306)

:choose_aula
echo.
set /p aula_choice=Elija el número del aula que desea guardar en aula.txt (o presione ENTER para no crear el archivo):

:: Quitar espacios en blanco
set "aula_choice=%aula_choice: =%"

:: Verificar si se ingresó un número válido
if "%aula_choice%"=="1" (
    set "selected_aula=Lab_A (P306)"
) else if "%aula_choice%"=="2" (
    set "selected_aula=Lab_B (P311)"
) else if "%aula_choice%"=="3" (
    set "selected_aula=Lab_C (P310)"
) else if "%aula_choice%"=="4" (
    set "selected_aula=Lab_D (Q302)"
) else if "%aula_choice%"=="5" (
    set "selected_aula=Lab_E (Q306)"
) else (
    echo No se seleccionó una opción válida. Inténtelo nuevamente.
    goto choose_aula
)

:: Guardar el aula seleccionada en aula.txt en la misma ubicación del script
echo Guardando el aula seleccionada en aula.txt...
echo %selected_aula% > "%~dp03/aula.txt"

:: Comprobar si el archivo fue creado correctamente
if exist "%~dp0aula.txt" (
    echo El aula %selected_aula% ha sido guardada en aula.txt.
) else (
    echo Error: No se pudo crear el archivo aula.txt.
)

pause
