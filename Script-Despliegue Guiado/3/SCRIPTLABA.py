import psutil
import time
import mysql.connector
import socket
import ctypes
from ctypes import wintypes
import os
import winreg
# Definición de variables para los  cursos
curso_interaccion_diseno_interfaces = "INTERACCION Y DISEÑO DE INTERFACES"
curso_programacion_i = "PROGRAMACION I"
curso_sin_clases = "SIN CLASES"
curso_gestion_proyectos = "GESTION DE PROYECTOS"
curso_sistemas_operativos_i = "SISTEMAS OPERATIVOS I"
curso_tecnicas_programacion = "TECNICAS DE PROGRAMACION"
curso_diseno_base_datos = "DISEÑO DE BASE DE DATOS"
curso_programacion_iii = "PROGRAMACION III"
curso_programacion_web_ii = "PROGRAMACION WEB II"
curso_inteligencia_negocios = "INTELIGENCIA DE NEGOCIOS"
curso_diseno_modelamiento_virtual = "DISEÑO Y MODELAMIENTO VIRTUAL"
curso_inteligencia_artifical = "INTELIGENCIA ARTIFICAL"
curso_soluciones_moviles_i = "SOLUCIONES MOVILES I"
curso_des_competencias_digitales = "DES. COMPETENCIAS DIGITALES"
curso_estadistica_inferencial = "ESTADISTICA INFERENCIAL Y ANALISIS"
curso_gestion_conf_adm_sw = "GESTION DE LA CONF. Y ADM DE SW"
curso_programacion_web_i = "PROGRAMACION WEB I"
curso_redes_comunic_datos_ii = "REDES Y COMUNIC DE DATOS II"
curso_calidad_prueba_software = "CALIDAD Y PRUEBA DE SOFTWARE"
curso_topicos_base_datos_avanzado_i = "TOPICOS DE BASE DE DATOS AVANZADO I"

# Definición de variables para los docentes
docente_i_chaparro = "I.CHAPARRO"
docente_h_sisa = "H.SISA"
docente_renzo_taco = "RENZO TACO"
docente_e_rodriguez = "E.RODRIGUEZ"
docente_p_cuadros = "P.CUADROS"
docente_n_quispe = "N.QUISPE"
docente_martha_paredes = "MARTHA PAREDES"
docente_l_fernandez = "L.FERNANDEZ"
docente_t_ale = "T.ALE"
docente_m_alcantara = "M.ALCANTARA"
docente_g_choque = "G.CHOQUE"
docente_ricardo_valcarcel = "RICARDO VALCARCEL"

# Horario del Laboratorio B en formato de diccionario
horario_lab_b = {
    "Lunes": [
        {"hora": "8:00-9:40", "curso": curso_interaccion_diseno_interfaces, "seccion": "B", "docente": "NULL"},
        {"hora": "9:40-11:20", "curso": curso_programacion_i, "seccion": "A", "docente": docente_i_chaparro},
        {"hora": "11:20-15:50", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "15:50-17:30", "curso": curso_gestion_proyectos, "seccion": "UNICA", "docente": docente_martha_paredes},
        {"hora": "17:30-18:20", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "18:20-20:00", "curso": curso_sistemas_operativos_i, "seccion": "A", "docente": docente_renzo_taco}
    ],
    "Martes": [
        {"hora": "8:00-10:30", "curso": curso_tecnicas_programacion, "seccion": "A", "docente": docente_g_choque},
        {"hora": "10:30-11:20", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "11:20-13:00", "curso": curso_diseno_base_datos, "seccion": "NULL", "docente": docente_h_sisa},
        {"hora": "13:00-15:00", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "15:00-16:40", "curso": curso_programacion_iii, "seccion": "A", "docente": docente_e_rodriguez},
        {"hora": "16:40-18:20", "curso": curso_soluciones_moviles_i, "seccion": "A", "docente": docente_e_rodriguez},
        {"hora": "18:20-21:40", "curso": curso_inteligencia_negocios, "seccion": "NULL", "docente": docente_p_cuadros}
    ],
    "Miércoles": [
        {"hora": "8:00-9:40", "curso": curso_diseno_modelamiento_virtual, "seccion": "A", "docente": "NULL"},
        {"hora": "9:40-15:00", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "15:00-16:40", "curso": curso_inteligencia_artifical, "seccion": "A", "docente": docente_i_chaparro},
        {"hora": "16:40-18:20", "curso": curso_programacion_web_ii, "seccion": "B", "docente": docente_n_quispe},
        {"hora": "18:20-20:00", "curso": curso_soluciones_moviles_i, "seccion": "A", "docente": docente_e_rodriguez}
    ],
    "Jueves": [
        {"hora": "8:00-9:40", "curso": curso_diseno_modelamiento_virtual, "seccion": "A", "docente": "NULL"},
        {"hora": "9:40-10:30", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "10:30-12:10", "curso": curso_des_competencias_digitales, "seccion": "D", "docente": docente_g_choque},
        {"hora": "12:10-15:00", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "15:00-16:40", "curso": curso_programacion_iii, "seccion": "A", "docente": docente_e_rodriguez},
        {"hora": "16:40-18:20", "curso": curso_estadistica_inferencial, "seccion": "A", "docente": docente_l_fernandez},
        {"hora": "18:20-20:00", "curso": curso_gestion_conf_adm_sw, "seccion": "A", "docente": docente_ricardo_valcarcel},
        {"hora": "20:00-21:40", "curso": curso_sistemas_operativos_i, "seccion": "A", "docente": docente_renzo_taco}
    ],
    "Viernes": [
        {"hora": "8:00-9:40", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "9:40-11:20", "curso": curso_programacion_i, "seccion": "A", "docente": docente_i_chaparro},
        {"hora": "11:20-13:00", "curso": curso_diseno_base_datos, "seccion": "A", "docente": docente_h_sisa},
        {"hora": "13:00-16:40", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "16:40-18:20", "curso": curso_programacion_web_i, "seccion": "A", "docente": docente_t_ale},
        {"hora": "18:20-20:00", "curso": curso_sistemas_operativos_i, "seccion": "A", "docente": docente_renzo_taco},
        {"hora": "20:00-21:40", "curso": curso_redes_comunic_datos_ii, "seccion": "A", "docente": docente_t_ale}
    ],
    "Sábado": [
        {"hora": "8:00-9:40", "curso": curso_calidad_prueba_software, "seccion": "A", "docente": docente_p_cuadros},
        {"hora": "9:40-11:20", "curso": curso_inteligencia_negocios, "seccion": "A", "docente": docente_p_cuadros},
        {"hora": "11:20-13:00", "curso": curso_topicos_base_datos_avanzado_i, "seccion": "B", "docente": docente_p_cuadros},
        {"hora": "13:00-14:10", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
        {"hora": "14:10-17:30", "curso": curso_topicos_base_datos_avanzado_i, "seccion": "A", "docente": docente_p_cuadros},
        {"hora": "17:30-20:00", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
    ],
    "Domingo": [
        {"hora": "8:00-20:00", "curso": curso_sin_clases, "seccion": "NULL", "docente": "NULL"},
    ]
}
date_file = 'last_date.txt'

def bytes_to_mb(bytes):
    """Convert bytes to megabytes"""
    return bytes / (1024 * 1024)

def get_network_traffic():
    """Get the current network traffic in megabytes"""
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_received = net_io.bytes_recv
    return bytes_sent, bytes_received

import os

def get_ip_address():
    """Get the IP address from ip.txt in the same directory as the script."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ip_file_path = os.path.join(script_dir, 'ip.txt')
        
        with open(ip_file_path, 'r') as file:
            ip_address = file.readline().strip()
        
        if not ip_address:
            ip_address = 'Desconocida'
    except Exception:
        ip_address = 'Desconocida'
    
    return ip_address

def get_aula():
    """Obtiene el nombre del aula desde el archivo aula.txt en el mismo directorio que el script."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        aula_file_path = os.path.join(script_dir, 'aula.txt')
        
        with open(aula_file_path, 'r') as file:
            aula = file.readline().strip()
        
        if not aula:
            aula = 'Desconocida'
    except Exception:
        aula = 'Desconocida'
    
    return aula


def get_active_window_name():
    """Get the name of the currently active window"""
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32

    hwnd = user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    
    try:
        process = psutil.Process(pid.value)
        return process.name()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return 'Desconocido'

def create_db_connection():
    """Create a connection to the MySQL database"""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='trafico_red_db'
    ) 

def fetch_current_traffic_data(cursor, date, ip_address, class_name, schedule_time):
    """Fetch the current traffic data from the database"""
    query = """
    SELECT id, total_enviado_mb, total_recibido_mb
    FROM trafico_red
    WHERE fecha = %s AND ip = %s AND clase = %s AND horario = %s
    """
    cursor.execute(query, (date, ip_address, class_name, schedule_time))
    result = cursor.fetchall()
    return result[0] if result else None

def update_traffic_data(cursor, total_sent_mb, total_received_mb, row_id):
    """Update the traffic data in the database"""
    query = """
    UPDATE trafico_red
    SET total_enviado_mb = total_enviado_mb + %s,
        total_recibido_mb = total_recibido_mb + %s
    WHERE id = %s
    """
    cursor.execute(query, (total_sent_mb, total_received_mb, row_id))

def insert_traffic_data(cursor, date, ip_address, class_name, schedule_time, day_of_week, shift, total_sent_mb, total_received_mb, lab_info, theme, browser, section, teacher):
    """Insert new traffic data into the database"""
    query = """
    INSERT INTO trafico_red 
    (fecha, ip, clase, horario, dia, turno, laboratorio, total_enviado_mb, total_recibido_mb, tema, navegador, seccion, docente) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (date, ip_address, class_name, schedule_time, day_of_week, shift, lab_info, total_sent_mb, total_received_mb, theme, browser, section, teacher)
    cursor.execute(query, values)

def read_last_date_from_file(file_path):
    """Read the last recorded date from a file"""
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file:
        return file.read().strip()

def write_current_date_to_file(file_path):
    """Write the current date to a file"""
    with open(file_path, 'w') as file:
        file.write(time.strftime('%Y-%m-%d'))

def get_class_schedule(day_of_week):
    """Get the class schedule for the current time."""
    current_hour = time.localtime().tm_hour
    current_minute = time.localtime().tm_min

    day_schedule = horario_lab_b.get(day_of_week, [])

    for entry in day_schedule:
        start_time, end_time = entry['hora'].split('-')
        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))

        # Verifica si la hora actual está dentro del rango del horario de clases
        if (start_hour < current_hour < end_hour) or \
           (start_hour == current_hour and start_minute <= current_minute) or \
           (end_hour == current_hour and end_minute >= current_minute):
            return entry['curso'], entry['seccion'], entry['docente'], entry['hora']

    return "Fuera de horario", "NULL", "NULL", "N/A"

def get_day_of_week():
    """Get the current day of the week"""
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return days[time.localtime().tm_wday]

def get_shift():
    """Determine the shift based on the current time"""
    current_hour = time.localtime().tm_hour
    if 7 <= current_hour < 13:
        return "MAÑANA"
    elif 13 <= current_hour < 22:
        return "TARDE"
    else:
        return "FUERA DE HORARIO UNIVERSITARIO"

def get_system_preferences():
    """Get system preferences including theme and default browser"""
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize')
        theme_value = winreg.QueryValueEx(reg_key, 'SystemUsesLightTheme')[0]
        theme = "CLARO" if theme_value == 1 else "OSCURO"
        winreg.CloseKey(reg_key)
    except Exception as e:
        theme = "Desconocido"
        print(f"Error al obtener tema del sistema: {e}")

    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice')
        browser = winreg.QueryValueEx(reg_key, 'Progid')[0]
        browser = browser.split('.')[0]  # Simplify browser name
        winreg.CloseKey(reg_key)
    except Exception as e:
        browser = "Desconocido"
        print(f"Error al obtener navegador predeterminado: {e}")

    return theme, browser

def main():
    interval = 1
    total_sent = 0
    total_received = 0
    last_date = time.strftime('%Y-%m-%d')
    last_class = ""
    ip_address = get_ip_address()
    lab_info = get_aula()
    print(f"IP de la máquina: {ip_address}")
    print("Monitoreando tráfico de red. Presiona Ctrl+C para detener.")

    last_recorded_date = read_last_date_from_file(date_file)

    if last_recorded_date != last_date:
        write_current_date_to_file(date_file)

    db_connection = None
    cursor = None

    while True:
        try:
            if db_connection is None or not db_connection.is_connected():
                db_connection = create_db_connection()
                cursor = db_connection.cursor()
                print("Conexión a la base de datos establecida.")

            current_date = time.strftime('%Y-%m-%d')
            class_name, section, teacher, schedule_time = get_class_schedule(get_day_of_week())
            day_of_week = get_day_of_week()
            shift = get_shift()
            theme, browser = get_system_preferences()

            if current_date != last_date or class_name != last_class:
                if last_class:
                    db_connection.commit()
                    print(f"\nNuevo día detectado o clase cambiada. Datos actualizados en la base de datos.")
                
                total_sent = 0
                total_received = 0
                last_class = class_name

            row = fetch_current_traffic_data(cursor, current_date, ip_address, class_name, schedule_time)
            if row:
                row_id = row[0]
            else:
                row_id = None

            bytes_sent_before, bytes_received_before = get_network_traffic()
            time.sleep(interval)
            bytes_sent_after, bytes_received_after = get_network_traffic()

            delta_sent = bytes_to_mb(bytes_sent_after - bytes_sent_before)
            delta_received = bytes_to_mb(bytes_received_after - bytes_received_before)

            total_sent += delta_sent
            total_received += delta_received

            if row_id:
                update_traffic_data(cursor, total_sent, total_received, row_id)
            else:
                insert_traffic_data(cursor, current_date, ip_address, class_name, schedule_time, day_of_week, shift, total_sent, total_received, lab_info, theme, browser, section, teacher)

            print(f"Fecha: {current_date}, IP: {ip_address}, Clase: {class_name}, Horario: {schedule_time}")
            print(f"Total Enviado (MB): {total_sent:.2f}, Total Recibido (MB): {total_received:.2f}")

            total_sent = 0
            total_received = 0

            db_connection.commit()

        except (mysql.connector.errors.DatabaseError, mysql.connector.errors.InterfaceError) as e:
            print(f"\nError de conexión a la base de datos: {e}")
            if db_connection:
                try:
                    db_connection.close()
                except:
                    pass
            db_connection = None
            cursor = None
            print("Intentando reconectar en 10 segundos...")
            time.sleep(10)
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Continuando la ejecución...")
        except KeyboardInterrupt:
            print("\nInterrupción por teclado. Cerrando...")
            if db_connection:
                db_connection.close()
            break

if __name__ == "__main__":
    main()
