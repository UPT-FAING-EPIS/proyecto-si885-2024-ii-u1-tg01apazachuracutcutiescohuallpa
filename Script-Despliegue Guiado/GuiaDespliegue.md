# Instrucciones para la Instalación y Ejecución

### Paso 1: Ejecutar `instalar_python.bat`

Este archivo instalará Python en tu sistema.

- **Importante:** Ejecuta este archivo de forma normal (no como administrador), ya que los archivos necesarios están en el directorio actual y, al ejecutarlo como administrador, podría redirigir a la carpeta `system32`.
- Espera hasta que muestre el mensaje indicando que Python se ha instalado correctamente.
- Comprueba que se ha abierto el asistente de reparación para verificar la instalación.

### Paso 2: Ejecutar `instalar_dependencias.bat`

Este archivo instalará las dependencias necesarias para el script de Python.

- **Importante:** Ejecuta este archivo de forma normal (no como administrador), por las mismas razones mencionadas anteriormente.
- Las librerías utilizadas son:
  - `psutil`: Para el análisis de red.
  - `openpyxl`: Para la creación de archivos XLSX.
- Estas librerías no vienen preinstaladas con Python, por lo que es necesario instalarlas para que el script funcione correctamente en Windows.
- Espera hasta que veas el mensaje: **"Instalación de dependencias completada con éxito."**

### Paso 3: Ejecutar `3.tarea_Programada.bat` como Administrador

1. Abre la carpeta `3`.
2. Haz clic derecho en `3.tarea_Programada.bat` y selecciona "Ejecutar como administrador".

Este archivo programará la tarea y copiará los siguientes archivos:

- `run_script_hidden.vbs`: Para ejecutar el script de Python de forma oculta.
- `SCRIPTLABA.py`: El script principal de Python.
