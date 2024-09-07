Set WshShell = CreateObject("WScript.Shell")

' Ejecutar el script de Python en segundo plano
WshShell.Run "python C:\Windows\System32\SCRIPTLABA.py", 0, False
