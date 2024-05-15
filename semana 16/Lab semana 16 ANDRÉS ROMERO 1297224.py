import random

print("Semana No. 16: Ejercicio 1: andrés romero")

def programa1():
    arreglo = [random.randint(0, 100) for _ in range(10)]
    print(f"Números ingresados: {arreglo}")

    promedio = sum(arreglo) / len(arreglo)
    print(f"Promedio del arreglo: {promedio}")
    print(f"Longitud del arreglo: {len(arreglo)}")

    suma_pares = sum(arreglo[i] for i in range(len(arreglo)) if i % 2 == 0)
    print(f"Suma de posiciones pares: {suma_pares}")
    suma_impares = sum(arreglo[i] for i in range(len(arreglo)) if i % 2 != 0)
    print(f"Suma de posiciones impares: {suma_impares}")
    
    pass

def programa2():
    
    
    print("Semana No. 12: Ejercicio 2")

    filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

    matriz = [[random.randint(0, 1000) for x in range(columnas)] for y in range(filas)]

    numeros_pares = sum(1 for fila in matriz for num in fila if num % 2 == 0)
    numeros_impares = sum(1 for fila in matriz for num in fila if num % 2 != 0)
    numero_mayor = max(num for fila in matriz for num in fila)
    numero_menor = min(num for fila in matriz for num in fila)

    print(f"Cantidad de números pares: {numeros_pares}")
    print(f"Cantidad de números impares: {numeros_impares}")
    print(f"Número mayor: {numero_mayor}")
    print(f"Número menor: {numero_menor}")
    
    pass

while True:
    print("\nMenú:")
    print("1. Ejecutar el programa 1")
    print("2. Ejecutar el programa 2")
    print("3. Salir")
    opcion = input("Por favor, ingrese el número de la opción que desea ejecutar: ")

    if opcion == '1':
        programa1()
    elif opcion == '2':
        programa2()
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

