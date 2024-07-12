import csv
import random
import statistics
import math
import os

sueldos = []

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sanchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def asignacion_sueldos_random():
    global sueldos
    sueldos = [random.randint(300000,2500000) for _ in trabajadores]
    print("sueldos asignados aleatoriamente.")

def clasificacion_sueldos():
    menor_800k = [(trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if sueldos[i] < 800000]
    entre_800k_y_2M = [(trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if 800000 <= sueldos[i] <= 2000000]
    superior_2M = [(trabajadores[i], sueldos[i]) for i in range(len(sueldos)) if sueldos[i] > 2000000]
    
    print("\nSueldos menores a 800.000")
    print("TOTAL:", len(menor_800k))
    for nombre, sueldo in menor_800k:
        print(f"nombre empleado {nombre} - Sueldo: ${sueldo}")
    
    print("\nSueldos entre 800k y 2M")
    print("TOTAL:", len(entre_800k_y_2M))
    for nombre, sueldo in entre_800k_y_2M:
        print(f"nombre empleado {nombre} - Sueldo: ${sueldo}")
        
    print("\nSueldos mayores a 2M")
    print("TOTAL:", len(superior_2M))
    for nombre, sueldo in superior_2M:
        print(f"nombre empleado {nombre} - Sueldo: ${sueldo}")
        
    print("\nTOTAL DE SUELDOS:", sum(sueldos))
    
def ver_estadisticas():
    if not sueldos:
        print("Primero debe asignar los sueldos")
        return
    sueldomax = max(sueldos)
    sueldomin = min(sueldos)
    promedio = statistics.mean(sueldos)
    media_geometrica = math.exp(sum(math.log(x) for x in sueldos) / len(sueldos))
    
    print ("\nEstadisticas de sueldos:")
    print(f"Sueldo mas alto: ${sueldomax}")
    print(f"Sueldo mas bajo: ${sueldomin}")
    print(f"Promedio de los sueldos: ${promedio:.2f}")
    print (f"Media geometrica: {media_geometrica:.2f}")
    
def Reporte_de_los_sueldos():
    if not sueldos:
        print("primero asigna los sueldos")
        return
    
    with open('Reporte_de_los_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["nombre empleado", "sueldo base", "descuento salud", "descuento afp", "sueldo liquido"])

        print("\nreporte de sueldos:")
        for i in range(len(trabajadores)):
            nombre = trabajadores[i]
            sueldobase = sueldos[i]
            descuentosalud = sueldobase * 0.07
            descuentoafp = sueldobase * 0.12
            sueldoliquido = sueldobase - descuentosalud - descuentoafp
            
            writer.writerow([nombre, sueldobase, descuentosalud, descuentoafp, sueldoliquido])
            print(f"{nombre},  sueldo base: ${sueldobase}, descuento salud: ${descuentosalud:.2f}, descuento afp: ${descuentoafp:.2f}, sueldo liquido: ${sueldoliquido:.2f}")
            
def inicio():
    while True:
        print("1. Asignar sueldos aleatorios.")
        print("2. Clasificar sueldos.")
        print("3. Ver estadísticas.")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opc = input("Seleccione una opcion: ")
        
        if opc == '1':
            asignacion_sueldos_random()
        elif opc == '2':
            clasificacion_sueldos()
        elif opc == '3':
            ver_estadisticas()
        elif opc == '4':
            Reporte_de_los_sueldos()
        elif opc == '5':
            print("Finalizando programa…\nDesarrollado por Matias Manriquez \nRUT 22.057.162-0")
            break


inicio()
        
