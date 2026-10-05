import psutil


def mostrarMenu():
    print("1.- Mostrar todos los servicios\n2.- Mostrar servicios Filtrados\n3.- Mostrar Descripcion de un servicio")
    

opcion = -1 

while opcion != 0:
    opcion = int(input("Introduzca su opcion\n"))
    
    if opcion == 1:
        procesos = psutil.pids()
        
        for i in procesos:
            p = psutil.Process(i)
            print("--------")
            print(f"Nombre: {p.name()}")
            print(f"PID: {p.ppid()}")
            print(f"Estado: {p.status()}")
        
        print("\n")
    
    if opcion == 2:
        estado = input("Elija el estado del filtro (running, stopped)\n").lower()
        
        if(estado == "running"):
            procesos = psutil.pids()
            
            for i in procesos:
                p = psutil.Process(i)

                if p.status() == "running":
                    print("--------")
                    print(f"Nombre: {p.name()}")
                    print(f"PID: {p.ppid()}")
                    print(f"Estado: {p.status()}")
        elif(estado == "stopped"):
            procesos = psutil.pids()
            
            for i in procesos:
                p = psutil.Process(i)
                
                if p.status() == "stopped":
                    print("--------")
                    print(f"Nombre: {p.name()}")
                    print(f"PID: {p.ppid()}")
                    print(f"Estado: {p.status()}")
    
    if opcion == 3:
        nombre = input("Indique el nombre del proceso para ver su descripcion\n").lower()
        
        procesos = psutil.pids()
        
        for i in procesos:
            
            if psutil.Process(i).name().lower() == nombre:
                print(psutil.Process(i).exe())
                break
        
        
        
                
                    