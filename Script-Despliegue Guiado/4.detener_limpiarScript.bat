@echo off

:: Detener la tarea programada principal
echo Deteniendo tarea programada...
schtasks /End /TN "RunScriptLaba_OnLogon"

:: Eliminar la tarea programada
echo Eliminando tarea programada...
schtasks /Delete /TN "RunScriptLaba_OnLogon" /F

:: Detener procesos de Python relacionados al script
echo Deteniendo procesos de Python relacionados...
taskkill /F /IM python.exe

:: Eliminar archivos específicos en C:\Windows\System32
echo Eliminando archivos de C:\Windows\System32...
del /F /Q "C:\Windows\System32\run_script_hidden.vbs"
del /F /Q "C:\Windows\System32\SCRIPTLABA.py"
del /F /Q "C:\Windows\System32\last_date.txt"

echo Tareas completadas.
pause
