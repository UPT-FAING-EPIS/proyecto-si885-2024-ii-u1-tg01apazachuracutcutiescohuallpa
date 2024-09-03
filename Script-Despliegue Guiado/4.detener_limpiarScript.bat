@echo off

:: Detener tareas programadas
echo Deteniendo tareas programadas...
schtasks /End /TN "RunScriptLaba_OnLogon"
schtasks /End /TN "RunScriptLaba_OnStart"

:: Eliminar tareas programadas
echo Eliminando tareas programadas...
schtasks /Delete /TN "RunScriptLaba_OnLogon" /F
schtasks /Delete /TN "RunScriptLaba_OnStart" /F

:: Detener procesos de Python relacionados al script
echo Deteniendo procesos de Python relacionados...
taskkill /F /IM python.exe /FI "WINDOWTITLE eq SCRIPTLABA.py"

:: Eliminar archivos específicos en C:\Windows\System32
echo Eliminando archivos de C:\Windows\System32...
del /F /Q "C:\Windows\System32\run_script_hidden.vbs"
del /F /Q "C:\Windows\System32\SCRIPTLABA.py"
del /F /Q "C:\Windows\System32\trafico_red.xlsx"

echo Tareas completadas.
pause
