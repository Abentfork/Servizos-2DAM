import json

import psutil
import math
from datetime import datetime

def mostrarMenu():
    print("1.- Mostrar Informacion Del Sistema\n2.- Guardar Informacion del sistema")

def guardarJson():
        info ={
            "Ncpu" : psutil.cpu_count(),
            "Frecuencia" : psutil.cpu_freq(),
            "Uso Cpu" : psutil.cpu_percent(),
            "Memoria Total" : math.trunc((psutil.virtual_memory().total / 1024**3)*100)/100,
            "Memoria disponible" : math.trunc((psutil.virtual_memory().available / 1024**3)*100)/100,
            "Memoria Usada" :  math.trunc((psutil.virtual_memory().used / 1024**3)* 100)/100,
            "Particiones" : psutil.disk_partitions(),
            "Uso Disco" : psutil.disk_usage('/'),
            "OLectura" : psutil.disk_io_counters().read_count,
            "OEscritura" : psutil.disk_io_counters().write_count,
            "Bytes Leidos" : psutil.disk_io_counters().read_bytes,
            "Bytes Escritos" : psutil.disk_io_counters().write_bytes,
            "Bytes Enviados" : psutil.net_io_counters().bytes_sent,
            "Bytes Recibidos" : psutil.net_io_counters().bytes_recv,
            "Paquetes Enviados" : psutil.net_io_counters().packets_sent,
            "Paquetes Recibidos" : psutil.net_io_counters().packets_recv
        }
        with open(f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json", 'w') as archivo:
            json.dump(info,archivo)
                        
    
opcion = -1

while opcion != 0:
    mostrarMenu()
    opcion = int(input("Seleccione una opcion\n"))
    if opcion == 1:
        if psutil.MACOS:
            print("OS: MacOS")
        if psutil.LINUX:
            print("OS: Linux")
        if psutil.WINDOWS:
            print("OS: windows")
        
        print("Informacion CPU:")
        print(f"    NCpu: {psutil.cpu_count()}")
        print(f"    Frecuencia: {psutil.cpu_freq()}")
        print(f"    Uso Cpu: {psutil.cpu_percent()}")
        print("Informacion Memoria:")
        print(f"    Memoria Total: {math.trunc((psutil.virtual_memory().total / 1024**3)*100) / 100} GB")
        print(f"    Memoria Disponible: {math.trunc((psutil.virtual_memory().available / 1024**3)*100) / 100}")
        print(f"    Memoria Usada: {math.trunc((psutil.virtual_memory().used / 1024**3)* 100)/100}")
        print("Informacion Discos:")
        print(f"    Particiones:")
        for i in psutil.disk_partitions():
            print(f"        {i}")
        print(f"    Uso disco: {psutil.disk_usage('/').percent}%")
        print(f"    OLectura: {psutil.disk_io_counters().read_count}")
        print(f"    OEscritura: {psutil.disk_io_counters().write_count}")
        print(f"    Bytes Leidos: {psutil.disk_io_counters().read_bytes}")
        print(f"    Bytes Escritos: {psutil.disk_io_counters().write_bytes}")
        print("Estadisticas de Red")
        print(f"    Bytes Enviados: {psutil.net_io_counters().bytes_sent}")
        print(f"    Bytes Recibidos: {psutil.net_io_counters().bytes_recv}")
        print(f"    Paquetes Enviados: {psutil.net_io_counters().packets_sent}")
        print(f"    Paquetes Recibidos: {psutil.net_io_counters().packets_recv}")
    if opcion == 2:
        guardarJson()
        
         




