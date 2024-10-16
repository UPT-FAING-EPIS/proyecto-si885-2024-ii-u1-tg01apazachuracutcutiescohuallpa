@echo off
setlocal EnableDelayedExpansion

:: Preguntar si desea instalar Python manualmente
set /p install_python="¿Desea instalar Python manualmente? (S/N): "
if /i "!install_python!"=="S" (
    call "1.instalar_python.bat"
) else (
    echo Saltando la instalación de Python.
)

:: Llamar al script para instalar dependencias
call "2.instalar_dependencias.bat"

:: Buscar el archivo de tarea programada y ejecutarlo como administrador
set "script_path=3\3.tarea_Programada.bat"
if exist "!script_path!" (
    echo Ejecutando 3.tarea_Programada.bat como administrador...
    powershell -Command "Start-Process cmd -ArgumentList '/c !script_path!' -Verb RunAs"
) else (
    echo El archivo 3.tarea_Programada.bat no fue encontrado.
)

endlocal
