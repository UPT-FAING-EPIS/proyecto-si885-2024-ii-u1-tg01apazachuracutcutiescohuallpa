<center>

[comment]: <img src="./media/media/image1.png" style="width:1.088in;height:1.46256in" alt="escudo.png" />

![./media/media/image1.png](./media/logo-upt.png)

**UNIVERSIDAD PRIVADA DE TACNA**

**FACULTAD DE INGENIERIA**

**Escuela Profesional de Ingeniería de Sistemas**

**Proyecto *Herramienta de Seguimiento y Evaluación del Desempeño de Red y Hardware en Computadoras UPT***

**Curso:** Inteligencia de Negocios

**Docente:** Mag. Patrick Cuadros Quiroga

**Integrantes:**

Escobar Rejas, Carlos Andrés (2021070016)  
Apaza Ccalle, Albert Kenyi (2021071075)  
Ricardo Cutipa Gutierrez (2021069827)  
Erick Churacutipa Blass (2020067578)  
Jesus Huallpa Maron (2021071085) 

**Tacna – Perú**

**2024**

</center>
<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|Apaza|ELV|ARV|24/08/2024|Versión Original|












**Sistema *Herramienta de Seguimiento y Evaluación del Desempeño de Red y Hardware en Computadoras UPT***

**Documento de Visión**

**Versión *{1.0}***
**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

|CONTROL DE VERSIONES||||||
| :-: | :- | :- | :- | :- | :- |
|Versión|Hecha por|Revisada por|Aprobada por|Fecha|Motivo|
|1\.0|MPV|ELV|ARV|10/10/2020|Versión Original|


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


### **ÍNDICE GENERAL**

1. [Introducción](#introduccion)  
    1.1 [Propósito](#proposito)  
    1.2 [Alcance](#alcance)  
    1.3 [Definiciones, Siglas y Abreviaturas](#definiciones)  
    1.4 [Referencias](#referencias)  
    1.5 [Visión General](#vision-general)  
2. [Posicionamiento](#posicionamiento)  
    2.1 [Oportunidad de negocio](#oportunidad-de-negocio)  
    2.2 [Definición del problema](#definicion-del-problema)  
3. [Descripción de los interesados y usuarios](#descripcion-de-interesados)  
    3.1 [Resumen de los interesados](#resumen-interesados)  
    3.2 [Resumen de los usuarios](#resumen-usuarios)  
    3.3 [Entorno de usuario](#entorno-usuario)  
    3.4 [Perfiles de los interesados](#perfiles-interesados)  
    3.5 [Perfiles de los Usuarios](#perfiles-usuarios)  
    3.6 [Necesidades de los interesados y usuarios](#necesidades-interesados-usuarios)  
4. [Vista General del Producto](#vista-general-producto)  
    4.1 [Perspectiva del producto](#perspectiva-producto)  
    4.2 [Resumen de capacidades](#resumen-capacidades)  
    4.3 [Suposiciones y dependencias](#suposiciones-dependencias)  
    4.4 [Costos y precios](#costos-precios)  
    4.5 [Licenciamiento e instalación](#licenciamiento-instalacion)  
5. [Características del producto](#caracteristicas-producto)  
6. [Restricciones](#restricciones)  
7. [Rangos de calidad](#rangos-calidad)  
 

[8.	Precedencia y Prioridad](#_Toc52661353)

[9.	Otros requerimientos del producto](#_Toc52661354)

b) Estandares legales

c) Estandares de comunicación	](#_toc394513800)37

d) Estandaraes de cumplimiento de la plataforma	](#_toc394513800)42

e) Estandaraes de calidad y seguridad	](#_toc394513800)42

[CONCLUSIONES](#_Toc52661355)

[RECOMENDACIONES](#_Toc52661356)

[BIBLIOGRAFIA](#_Toc52661357)

[WEBGRAFIA](#_Toc52661358)


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

**<u>Informe de Visión</u>**


## 1. Introducción <span id="introduccion" class="anchor"></span>

    Este documento de visión presenta el proyecto "Herramienta de Seguimiento y Evaluación del Desempeño de Red y Hardware en Computadoras UPT", cuyo objetivo es mejorar la gestión y optimización de los recursos tecnológicos en los laboratorios de la Universidad Privada de Tacna. La herramienta permitirá un monitoreo continuo y análisis detallado del rendimiento de los equipos, proporcionando datos críticos para la toma de decisiones en la administración de la infraestructura tecnológica.

### 1.1 Propósito <span id="proposito" class="anchor"></span>

    Recopilar y analizar datos del sistema: Obtener información detallada sobre el uso de recursos de las computadoras en los laboratorios de la universidad, con el fin de identificar patrones y áreas de mejora.
    
    Evaluar el rendimiento y el consumo: Identificar el consumo de energía y el rendimiento en términos de uso de CPU, RAM, GPU, así como el consumo de internet, para optimizar la eficiencia operativa.
    
    Optimización del soporte: Proporcionar datos útiles para mejorar el soporte técnico, el mantenimiento preventivo y correctivo de las computadoras, y asegurar su óptimo funcionamiento.

### 1.2 Alcance <span id="alcance" class="anchor"></span>

    Área de estudio: Computadoras en los laboratorios de la Universidad Privada de Tacna.
    
    Datos a recopilar: Temperatura durante las sesiones, número de sesiones, consumo de internet (Mbps), número de clics, programas más utilizados, y software con mayor consumo de recursos (CPU, RAM, GPU).
    
    Metodología: Utilización de un script en Python con la biblioteca psutil para recopilar datos de rendimiento y actividad, que serán almacenados y analizados para generar reportes de desempeño.

### 1.3 Definiciones, Siglas y Abreviaturas <span id="definiciones" class="anchor"></span>

    CPU: Unidad Central de Procesamiento (Central Processing Unit).
    
    RAM: Memoria de Acceso Aleatorio (Random Access Memory).
    
    GPU: Unidad de Procesamiento Gráfico (Graphics Processing Unit).
    
    Mbps: Megabits por segundo, unidad de medida de velocidad de transferencia de datos en redes.
    
    psutil: Biblioteca de Python para la recopilación de información del sistema y el monitoreo de recursos.

### 1.4 Referencias <span id="referencias" class="anchor"></span>

    Documentación de psutil: https://psutil.readthedocs.io
    
    Guías de Python: https://docs.python.org
    
    Manual de la Universidad Privada de Tacna: Normas y permisos para el uso de laboratorios.

### 1.5 Visión General <span id="vision-general" class="anchor"></span>

    Implementación del script: El script en Python se ejecutará en las computadoras de los laboratorios, capturando datos necesarios para el análisis de rendimiento y consumo de recursos.
    
    Análisis de datos: Evaluar los datos recopilados para identificar tendencias, problemas recurrentes y áreas que requieren optimización.
    
    Informe de resultados: Presentar un informe detallado con los hallazgos y recomendaciones, facilitando la toma de decisiones para optimizar el uso de los recursos en las computadoras de la universidad.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 2. Posicionamiento <span id="posicionamiento" class="anchor"></span>

### 2.1 Oportunidad de negocio <span id="oportunidad-de-negocio" class="anchor"></span>

    Optimización de recursos: Mejorar la eficiencia operativa y reducir los costos asociados con el mantenimiento y soporte técnico de los laboratorios de computación.
    
    Mejora en la experiencia educativa: Asegurar que los estudiantes cuenten con un entorno de laboratorio confiable y de alto rendimiento, lo que contribuye a una mejor experiencia de aprendizaje.
    
    Sostenibilidad: Contribuir a la reducción del consumo energético y al uso eficiente de los recursos tecnológicos en la universidad.

### 2.2 Definición del problema <span id="definicion-del-problema" class="anchor"></span>

| **LA FALTA** | La ausencia de un sistema automatizado de monitoreo de red y hardware en las computadoras del laboratorio conlleva a dificultades para detectar problemas de rendimiento, ineficiencias en la gestión de recursos y mantenimiento reactivo. |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LA NECESIDAD** | La necesidad de un monitoreo continuo y detallado se vuelve crucial para asegurar la eficiencia operativa, la optimización de recursos y la reducción de tiempos de inactividad, mejorando la calidad del soporte técnico. |
| **EL PROBLEMA** | La falta de un sistema de monitoreo automatizado provoca una falta de visibilidad sobre el uso de recursos, lo que puede llevar a un uso ineficiente de las computadoras, mayor consumo de energía, y un soporte técnico reactivo. |
| **LA SOLUCIÓN** | Implementar una herramienta de monitoreo que permita la evaluación continua del rendimiento de red y hardware, proporcionando datos en tiempo real y alertas que faciliten la gestión proactiva y la optimización de recursos. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 3. Descripción de los interesados y usuarios <span id="descripcion-de-interesados" class="anchor"></span>

### 3.1 Resumen de los interesados <span id="resumen-interesados" class="anchor"></span>

| **Nombre**      | **Descripción** | **Responsabilidad** |
|-----------------|-----------------|---------------------|
| **Área de TI**  | Encargada de la gestión y mantenimiento de la infraestructura tecnológica. | Gestionar y optimizar los recursos tecnológicos, asegurar el funcionamiento continuo de los equipos. |
| **Soporte Técnico** | Personal que realiza el mantenimiento y soporte de las computadoras en los laboratorios. | Diagnosticar y resolver problemas técnicos, realizar mantenimientos preventivos y correctivos. |
| **Estudiantes** | Usuarios finales que utilizan las computadoras para sus actividades académicas. | Realizar actividades académicas utilizando los recursos tecnológicos proporcionados. |
| **Administración** | Encargada de la supervisión general de las operaciones de la universidad. | Optimizar los costos operativos, mejorar la calidad del servicio educativo. |

### 3.2 Resumen de los usuarios <span id="resumen-usuarios" class="anchor"></span>

| **Nombre**      | **Descripción** | **Responsabilidad** |
|-----------------|-----------------|---------------------|
| **Soporte Técnico** | Interactúa con todas las funcionalidades del sistema para el monitoreo, diagnóstico y resolución de problemas. | Monitorear el rendimiento de las computadoras, realizar mantenimientos preventivos y correctivos. |
| **Área de TI**  | Utiliza los reportes generados por el sistema para la planificación del mantenimiento y las actualizaciones. | Gestionar los recursos tecnológicos, planificar mantenimientos y actualizaciones. |
| **Estudiantes** | Utilizan las computadoras para realizar actividades académicas, beneficiándose de un mejor rendimiento y menos interrupciones. | Utilizar los recursos tecnológicos para actividades académicas y proyectos prácticos. |

### 3.3 Entorno de usuario <span id="entorno-usuario" class="anchor"></span>

    Los usuarios interactúan con el sistema a través de una interfaz web intuitiva y fácil de usar. El sistema estará accesible desde navegadores web, permitiendo el monitoreo en tiempo real, la generación de informes y la configuración de alertas.

### 3.4 Perfiles de los interesados <span id="perfiles-interesados" class="anchor"></span>

| **Representante** | **Descripción** | **Tipo** | **Responsabilidades** | **Criterios de éxito** |
|-------------------|-----------------|----------|-----------------------|------------------------|
| **Área de TI**    | Encargados de la administración y mantenimiento de la infraestructura tecnológica. | Administrador | Configurar usuarios, permisos, horarios y generar informes. | Gestionar con éxito las funcionalidades del sistema. |
| **Administración** | Supervisores de las operaciones generales de la universidad y la gestión presupuestaria. | Supervisor | Asegurar que los costos operativos sean optimizados y la calidad del servicio educativo se mantenga alta. | Eficiencia en la operación de la infraestructura tecnológica. |

### 3.5 Perfiles de los Usuarios <span id="perfiles-usuarios" class="anchor"></span>

| **Representante** | **Descripción** | **Tipo** | **Responsabilidades** | **Criterios de éxito** | **Implicación** |
|-------------------|-----------------|----------|-----------------------|------------------------|----------------|
| **Soporte Técnico** | Personal técnico encargado del monitoreo, diagnóstico y resolución de problemas. | Técnico | Configurar el sistema, gestionar el rendimiento de los equipos. | Eficacia en la resolución de problemas y mantenimiento de equipos. | Participación activa en la gestión diaria de los recursos tecnológicos. |
| **Estudiantes** | Usuarios finales que utilizan las computadoras para sus actividades académicas. | Usuario final | Utilizar los recursos tecnológicos para tareas académicas. | Eficiencia y efectividad en el uso de los recursos tecnológicos. | Uso regular de los equipos en sus actividades académicas. |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 4. Vista General del Producto <span id="vista-general-producto" class="anchor"></span>

### 4.1 Perspectiva del producto <span id="perspectiva-producto" class="anchor"></span>

    El sistema de monitoreo proporcionará una solución integral para el seguimiento y evaluación del rendimiento de las computadoras de los laboratorios, facilitando la gestión proactiva de la infraestructura tecnológica.

### 4.2 Resumen de capacidades <span id="resumen-capacidades" class="anchor"></span>

| **Beneficios para el Área de TI y Soporte Técnico** | **Principales características** |
|----------------------------------------------------|---------------------------------|
| **Monitoreo en tiempo real** | Permite el seguimiento continuo del rendimiento de CPU, RAM, GPU y red, así como la identificación de posibles cuellos de botella en el uso de recursos. |
| **Alertas automáticas** | Genera notificaciones en tiempo real ante cualquier anomalía detectada, facilitando una respuesta rápida y efectiva. |
| **Reportes detallados** | Genera informes automatizados y personalizables sobre el uso de los recursos, el rendimiento de las computadoras y el consumo de ancho de banda, lo que permite una toma de decisiones informada. |
| **Análisis comparativo** | Posibilidad de comparar el rendimiento entre distintos laboratorios para identificar cuáles hacen un mayor uso del ancho de banda o presentan más problemas técnicos. |

### 4.3 Suposiciones y dependencias <span id="suposiciones-dependencias" class="anchor"></span>

    Acceso a la infraestructura: Se asume que el Área de TI proporcionará el acceso necesario a las computadoras y la red para la implementación del sistema de monitoreo.
    
    Estabilidad del sistema: Se asume que el script de monitoreo será lo suficientemente ligero para no afectar el rendimiento normal de las computadoras.
    
    Disponibilidad de recursos: Se presupone que los recursos técnicos y humanos necesarios para el desarrollo e implementación del sistema estarán disponibles según lo planificado.

### 4.4 Costos y precios <span id="costos-precios" class="anchor"></span>

| **Concepto**  | **Costo Total (S/.)** |
|---------------|------------------------|
| **Costos Generales** | Aún nada | 0 |
| **Costos Operativos durante el Desarrollo** | Aún nada | 0 |
| **Costos del Ambiente** | Aún nada | 0 |
| **Costos de Personal** | Aún nada | 0 |
| **Total** | 0 |

### 4.5 Licenciamiento e instalación <span id="licenciamiento-instalacion" class="anchor"></span>

    Licenciamiento: La herramienta se distribuirá bajo una licencia de software libre para su uso interno en la universidad.
    
    Instalación: La instalación del sistema se llevará a cabo en los laboratorios de informática, con soporte técnico a cargo del Área de TI, asegurando una implementación sin contratiempos.

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 5. Características del producto <span id="caracteristicas-producto" class="anchor"></span>

    Monitoreo en tiempo real: Seguimiento continuo del rendimiento de CPU, RAM, GPU, temperatura y consumo de red en las computadoras de los laboratorios.
    
    Evaluación del consumo de energía: Identificación de patrones de consumo energético para optimizar el rendimiento y prevenir sobrecalentamientos.
    
    Análisis de la red: Supervisión del uso de internet y ancho de banda, con la capacidad de identificar cuellos de botella y optimizar la conectividad.
    
    Generación de reportes automatizados: Creación de informes personalizados sobre el estado y uso de los recursos, facilitando la toma de decisiones informadas.
    
    Alertas automáticas: Notificaciones instantáneas en caso de detectar anomalías en el rendimiento, permitiendo una rápida intervención.

## 6. Restricciones <span id="restricciones" class="anchor"></span>

    Acceso limitado a la infraestructura: El proyecto dependerá del acceso proporcionado por el Área de TI, lo que podría limitar la implementación y el monitoreo completo de los equipos.
    
    Recursos computacionales: El script de monitoreo debe ser lo suficientemente ligero para no afectar negativamente el rendimiento de las computadoras durante su operación.
    
    Compatibilidad de software: La herramienta debe ser compatible con el entorno operativo actual de la universidad, lo que podría restringir las tecnologías y plataformas que pueden ser utilizadas.

## 7. Rangos de calidad <span id="rangos-calidad" class="anchor"></span>

    Exactitud de los datos: Se requiere un nivel alto de precisión en la recopilación y procesamiento de datos para asegurar su utilidad y fiabilidad en la toma de decisiones.
    
    Disponibilidad del sistema: El sistema debe estar operativo al menos un 95% del tiempo para garantizar un monitoreo continuo y confiable.
    
    Usabilidad: La interfaz del sistema debe ser intuitiva y fácil de usar para los técnicos y el personal del Área de TI.
    
    Escalabilidad: El sistema debe ser escalable para soportar el crecimiento de la infraestructura tecnológica de la universidad, permitiendo la incorporación de nuevos laboratorios y equipos sin comprometer el rendimiento.


8. <span id="_Toc52661353" class="anchor"></span>**Precedencia y Prioridad**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

9. <span id="_Toc52661354" class="anchor"></span>**Otros requerimientos del producto**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661355" class="anchor"></span>**CONCLUSIONES**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661356" class="anchor"></span>**RECOMENDACIONES**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661357" class="anchor"></span>**BIBLIOGRAFIA**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

<span id="_Toc52661358" class="anchor"></span>**WEBGRAFIA**

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>
