# Proyecto Formatos 011

### Integrantes

| Nombre                             | Insights Totales |
|------------------------------------|-------------------|
| Escobar Rejas, Carlos Andrés (2021070016) | [Insights Totales] |
| Apaza Ccalle, Albert Kenyi (2021071075)  | [Insights Totales] |
| Ricardo Cutipa Gutierrez (2021069827)    | [Insights Totales] |
| Erick Churacutipa Blass (2020067578)     | [Insights Totales] |
| Jesus Huallpa Maron (2021071085)         | [Insights Totales] |

[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15560310)

## Contexto del Proyecto

Hablamos con los dos chicos de soporte, el de turno de mañana (no sabemos su nombre) y el que vemos siempre en las tardes, Kenyi Chino. Nos comentó que sería beneficioso conocer el consumo de internet por laboratorios, para tener un análisis rápido sobre si el problema en un laboratorio es causado porque en otro laboratorio se está consumiendo mucho internet. También, para que él pueda reportar el consumo de internet por laboratorio, en este caso, solo uno: el laboratorio A.

Kenyi nos dijo que sí, pero que deberíamos hablar con Lanchipa para que nos dé el visto bueno para el despliegue en algún laboratorio, ya que él es el encargado.

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

- ![Python](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python_logo_2020.svg)
- ![Tableau](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Tableau_Software_logo.svg/1200px-Tableau_Software_logo.svg.png)
- ![Windows Task Scheduler](https://docs.microsoft.com/en-us/windows-server/administration/images/schedule-tasks.png)

