@echo off
:: Cambiar la codificación a UTF-8
chcp 65001 >nul

:: Comprueba si el script tiene privilegios de administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Requiere permisos de administrador. Intentando ejecutar con elevación...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Inicia la instalación de dependencias
echo Instalando dependencias de Python...
pip install psutil
pip install mysql-connector-python
pip install GPUtil
python -m ensurepip --upgrade
python -m pip install setuptools
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
setlocal EnableDelayedExpansion

:choose_file
:: Listar todos los archivos .py en la ubicación donde se ejecuta el script
echo Listando archivos .py disponibles para copiar:
set index=1
for %%F in ("%~dp0*.py") do (
    echo !index!. %%~nxF
    set "file[!index!]=%%~nxF"
    set /a index+=1
)

:: Verificar si se encontraron archivos .py
if !index! equ 1 (
    echo No se encontraron archivos .py en la ubicación.
    pause
    goto end
)

:: Elegir el archivo a copiar
set /p file_choice=Seleccione el número del archivo que desea copiar a la carpeta 3 (o presione ENTER para cancelar): 

:: Verificar si se ingresó un número válido
if defined file[%file_choice%] (
    set "script_to_copy=!file[%file_choice%]!"
) else (
    echo No se seleccionó un archivo válido. Inténtelo nuevamente.
    goto choose_file  :: Regresar al inicio de la selección de archivo
)

:: Copiar el archivo seleccionado a la carpeta 3
set "filename_no_ext=%script_to_copy:~0,-3%"  :: Extraer el nombre sin extensión
set "extension=.py"                             :: Definir la extensión

:: Cambiar la última letra del nombre a 'A'
set "new_filename=%filename_no_ext:~0,-1%A%extension%"

echo Copiando el archivo %script_to_copy% a la carpeta 3 como %new_filename%...
copy "%~dp0%script_to_copy%" "%~dp03\%new_filename%"
if %errorlevel% equ 0 (
    echo El archivo %script_to_copy% ha sido copiado a la carpeta 3 como %new_filename%.
) else (
    echo Error al copiar %script_to_copy%.
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


:: Pausar para permitir que el usuario vea el mensaje
pause
:end
echo.
pause
