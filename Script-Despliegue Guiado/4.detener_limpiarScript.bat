@echo off

:: Detener tareas programadas
echo Deteniendo tareas programadas...
schtasks /End /TN "RunScriptLaba_OnLogon"
schtasks /End /TN "RunScriptLaba_OnStart"
schtasks /End /TN "CambiarFecha_Diario"
schtasks /End /TN "MonitorRunScriptLaba"

:: Eliminar tareas programadas
echo Eliminando tareas programadas...
schtasks /Delete /TN "RunScriptLaba_OnLogon" /F
schtasks /Delete /TN "RunScriptLaba_OnStart" /F
schtasks /Delete /TN "CambiarFecha_Diario" /F
schtasks /Delete /TN "MonitorRunScriptLaba" /F

:: Detener procesos de Python relacionados al script
echo Deteniendo procesos de Python relacionados...
taskkill /F /IM python.exe /FI "WINDOWTITLE eq SCRIPTLABA.py"

:: Eliminar archivos específicos en C:\Windows\System32
echo Eliminando archivos de C:\Windows\System32...
del /F /Q "C:\Windows\System32\run_script_hidden.vbs"
del /F /Q "C:\Windows\System32\SCRIPTLABA.py"
del /F /Q "C:\Windows\System32\cambiar_fecha.ps1"
del /F /Q "C:\Windows\System32\fecha_log.txt"
del /F /Q "C:\Windows\System32\trafico_red.xlsx"
del /F /Q "C:\Windows\System32\monitor_script_log.txt"

echo Tareas completadas.
pause
