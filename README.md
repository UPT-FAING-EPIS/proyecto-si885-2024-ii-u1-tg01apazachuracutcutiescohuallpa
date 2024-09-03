# Proyecto Formatos 011

### Integrantes

| Nombre                             | Insights Totales |
|------------------------------------|-------------------|
| Escobar Rejas, Carlos Andrés  | (2021070016) |
| Apaza Ccalle, Albert Kenyi   | (2021071075) |
| Ricardo Cutipa Gutierrez     | (2021069827) |
| Erick Churacutipa Blass     | (2020067578) |
| Jesus Huallpa Maron          | (2021071085) |

[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15560310)

## Contexto del Proyecto

Hablamos con el personal de soporte de los turnos de mañana y tarde. En particular, discutimos con el encargado del turno de la tarde sobre la posibilidad de realizar un análisis detallado del consumo de internet por laboratorio. Se destacó que este análisis permitiría evaluar rápidamente si los problemas en un laboratorio podrían estar relacionados con el alto consumo de internet en otros laboratorios. Además, facilitaría la elaboración de informes sobre el consumo de internet para el laboratorio específico en cuestión.

Se estuvo de acuerdo con esta propuesta, pero se recomendó consultar con el ingeniero encargado para obtener la autorización necesaria para el despliegue del sistema en uno de los laboratorios.

## ¿Cómo lo haremos?

* Utilizaremos un script de Python 
* Tarea programada de Windows

### Librerías utilizadas en el código

- **psutil**: Para obtener estadísticas de uso de recursos del sistema, como CPU, memoria y red.
- **time**: Para manejar operaciones relacionadas con tiempo, como pausas en la ejecución del script.
- **openpyxl**: Para trabajar con archivos Excel.
- **from openpyxl import Workbook, load_workbook**: Para crear y manipular hojas de cálculo de Excel.
- **socket**: Para obtener información de red, como la IP del equipo.
- **ctypes**: Para realizar llamadas a funciones del sistema operativo Windows.

### Problemas encontrados

- **Uso de Python en lugar de PowerShell (.ps1)**: Inicialmente, se intentó realizar el script en PowerShell, pero no proporcionaba correctamente el consumo de red, por lo que decidimos optar por Python, un intérprete muy conocido y con una amplia comunidad de ayuda en foros.
- **Falta de Python en algunas PCs de los laboratorios**: Algunas PCs no tienen Python instalado, lo que dificultaría la instalación del script.
- **Dependencias adicionales**: Ciertas librerías necesarias (como `psutil` y `openpyxl`) no vienen instaladas de forma predeterminada con Python.
- **Riesgo de eliminación del script**: Es fácil para los estudiantes eliminar el contenido del script en cualquier ordenador.
- **Mover archivos manualmente**: Trasladar archivos a directorios de forma manual lleva tiempo y puede implicar errores humanos.

### Soluciones

- **Archivos BAT para instalación**:
  - `instalar_python.bat`: Buscará el archivo `python-3.12.5-amd64.exe` en el lugar donde se encuentre, sin buscar en otras carpetas, y procederá a su instalación.
  - `instalar_dependencias.bat`: Deberá ejecutarse después de finalizar `instalar_python.bat` para instalar las dependencias necesarias.
  - **Tercer archivo BAT**: Copiará un archivo `.vbs` y el script `.py` en un lugar menos accesible para los estudiantes.
  - **Uso de VBS**: Se utiliza un archivo VBS para que al ejecutarse el script no se muestre una consola o ventana de compilación, evitando que el alumno la cierre e interrumpa el proceso de compilación.

### ¿Cómo funciona?

El script crea un archivo `trafico_red.xlsx`, que es entendible para nuestro programa Tableau, dividiendo la información en columnas y obteniendo los siguientes datos:

- Fecha
- Hora
- Minuto
- Segundo
- Bytes Enviados (MB)
- Bytes Recibidos (MB)
- Total Enviado (MB)
- Total Recibido (MB)
- Total General (MB)
- IP
- Aplicación Activa

Lo más importante es el total recibido y enviado junto al total general de ambos.

El archivo será enviado desde `sosahijas@gmail.com` a `sosahijas@gmail.com`, usando como nombre de archivo la fecha y la IP del ordenador desde el cual se envía.

Habrá un archivo por cada fecha, y si el sistema detecta una nueva fecha (por ejemplo, al apagar y comenzar de nuevo), recopilará los datos y enviará el correo electrónico.

### Imágenes

- ![Python](https://www.python.org/static/community_logos/python-logo-generic.svg)
- ![Tableau](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Tableau_Software_logo.svg/1200px-Tableau_Software_logo.svg.png)
- ![Windows Task Scheduler](https://docs.microsoft.com/en-us/windows-server/administration/images/schedule-tasks.png)

