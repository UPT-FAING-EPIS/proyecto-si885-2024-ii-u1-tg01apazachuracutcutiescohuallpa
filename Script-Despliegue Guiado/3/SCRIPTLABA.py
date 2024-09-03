import psutil
import time
import openpyxl
from openpyxl import Workbook, load_workbook
import socket
import ctypes
from ctypes import wintypes
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import shutil
import os

def bytes_to_mb(bytes):
    """Convert bytes to megabytes"""
    return bytes / (1024 * 1024)

def get_network_traffic():
    """Get the current network traffic in megabytes"""
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_received = net_io.bytes_recv
    return bytes_sent, bytes_received

def get_ip_address():
    """Get the current IP address"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = 'Desconocida'
    finally:
        s.close()
    return ip_address

def get_active_window_name():
    """Get the name of the currently active window"""
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32

    # Obtener el handle de la ventana activa
    hwnd = user32.GetForegroundWindow()
    
    # Obtener el ID del proceso de la ventana activa
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    
    # Obtener el proceso por el ID
    try:
        process = psutil.Process(pid.value)
        return process.name()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return 'Desconocido'

def send_email(original_file_path, last_date):
    """Send an email with the specified file attached"""
    from_email = "sosahijas@gmail.com"
    to_email = "sosahijas@gmail.com"
    subject = "Informe de tráfico de red"
    body = "Adjunto el informe de tráfico de red."

    # Configuración del servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    password = "funb tvnf puit wrmh"  # Contraseña de aplicación

    # Obtener IP y fecha actual
    ip_address = get_ip_address()
    current_date = time.strftime('%d-%m')  # Día y mes

    # Crear el nuevo nombre de archivo con la fecha y IP
    new_file_name = f"{last_date},{ip_address}.xlsx"
    new_file_path = f"copia_{new_file_name}"

    # Copiar el archivo original al nuevo archivo con el nombre cambiado
    shutil.copy(original_file_path, new_file_path)
    
    # Crear el mensaje de correo
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Adjuntar el cuerpo del correo con codificación UTF-8
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # Adjuntar el archivo
    with open(new_file_path, "rb") as file:
        part = MIMEApplication(file.read(), Name=new_file_name)
    part['Content-Disposition'] = f'attachment; filename="{new_file_name}"'
    msg.attach(part)

    # Enviar el correo
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        print("Correo electrónico enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        server.quit()

    # Eliminar archivos que comienzan con "copia_"
    remove_copied_files()

def get_last_date_from_excel(xlsx_file):
    """Get the last date from the Excel file"""
    try:
        wb = load_workbook(xlsx_file)
        ws = wb.active
        # Obtener la fecha desde la segunda fila
        if ws.max_row >= 2:
            last_date = ws.cell(row=2, column=1).value
            if isinstance(last_date, str):
                return last_date.split(' ')[0]  # Return only the date part
    except Exception as e:
        print(f"Error al leer la fecha desde el archivo Excel: {e}")
    return time.strftime('%d-%m')  # Default to current date if there's an error

def remove_last_row(xlsx_file):
    """Remove the last row from the Excel file"""
    try:
        wb = load_workbook(xlsx_file)
        ws = wb.active
        ws.delete_rows(ws.max_row)
        wb.save(xlsx_file)
    except Exception as e:
        print(f"Error al eliminar la última fila del archivo Excel: {e}")

def create_new_excel_file(xlsx_file):
    """Create a new Excel file with headers"""
    wb = Workbook()
    ws = wb.active
    ws.title = "Tráfico de Red"
    
    # Escribir encabezados en la hoja de cálculo
    ws.append(['Fecha', 'Hora', 'Minuto', 'Segundo', 'Bytes Enviados (MB)', 'Bytes Recibidos (MB)', 'Total Enviado (MB)', 'Total Recibido (MB)', 'Total General (MB)', 'IP', 'Aplicación Activa'])
    wb.save(xlsx_file)

def remove_copied_files():
    """Remove files that start with 'copia_'"""
    for file in os.listdir('.'):
        if file.startswith('copia_') and file.endswith('.xlsx'):
            os.remove(file)
            print(f"Archivo eliminado: {file}")

def main():
    # Intervalo de actualización en segundos
    interval = 1
    # Nombre del archivo XLSX
    xlsx_file = 'trafico_red.xlsx'
    
    # Crear el archivo Excel por primera vez
    create_new_excel_file(xlsx_file)
    
    # Inicializar totales
    total_sent = 0
    total_received = 0
    last_date = time.strftime('%Y-%m-%d')
    
    # Obtener IP de la máquina
    ip_address = get_ip_address()
    
    print(f"IP de la máquina: {ip_address}")
    print("Monitoreando tráfico de red. Presiona Ctrl+C para detener.")
    
    try:
        while True:
            # Obtener la fecha actual
            current_date = time.strftime('%Y-%m-%d')
            
            # Reiniciar los totales si es un nuevo día
            if current_date != last_date:
                # Guardar el archivo y enviar por correo
                wb = load_workbook(xlsx_file)
                remove_last_row(xlsx_file)  # Eliminar la última fila del archivo Excel
                wb.save(xlsx_file)
                last_date = get_last_date_from_excel(xlsx_file)
                send_email(xlsx_file, last_date)
                
                # Eliminar el archivo antiguo y crear uno nuevo
                os.remove(xlsx_file)
                create_new_excel_file(xlsx_file)
                
                total_sent = 0
                total_received = 0
                last_date = current_date
                print(f"\nNuevo día detectado. Totales reiniciados.")
            
            bytes_sent_before, bytes_received_before = get_network_traffic()
            
            time.sleep(interval)
            
            bytes_sent_after, bytes_received_after = get_network_traffic()
            
            sent_in_interval = bytes_sent_after - bytes_sent_before
            received_in_interval = bytes_received_after - bytes_received_before
            
            # Convierte bytes a megabytes
            sent_in_mb = bytes_to_mb(sent_in_interval)
            received_in_mb = bytes_to_mb(received_in_interval)
            
            total_sent += sent_in_mb
            total_received += received_in_mb
            total_general = total_sent + total_received
            
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            date, time_str = current_time.split(' ')
            hour, minute, second = time_str.split(':')
            
            active_app = get_active_window_name()

            print(f"Aplicación activa: {active_app}")

            # Abrir el archivo Excel y agregar datos
            wb = load_workbook(xlsx_file)
            ws = wb.active
            ws.append([date, hour, minute, second, f"{sent_in_mb:.2f}", f"{received_in_mb:.2f}", f"{total_sent:.2f}", f"{total_received:.2f}", f"{total_general:.2f}", ip_address, active_app])
            wb.save(xlsx_file)
            
            print(f"Enviado: {sent_in_mb:.2f} MB/s | Recibido: {received_in_mb:.2f} MB/s")
    
    except KeyboardInterrupt:
        print("\nMonitoreo detenido.")

if __name__ == "__main__":
    main()
