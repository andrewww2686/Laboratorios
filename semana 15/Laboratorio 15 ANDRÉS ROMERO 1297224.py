import math

def ObtenerAreaTriangulo(b, h):
    a = (b * h) / 2
    return a

def ObtenerAreaCuadrado(l):
    a = l ** 2
    return a

def ObtenerAreaRectangulo(b, h):
    a = b * h
    return a

def ObtenerAreaCirculo(r):
    a = math.pi * (r ** 2)
    return a

def mostrar_menu():
    print("════════════════════════════════════")
    print("       Semana No. 12: Ejercicio 1    ")
    print("════════════════════════════════════")
    print(" a. Área de triángulo               ")
    print(" b. Área de cuadrado                ")
    print(" c. Área de rectángulo              ")
    print(" d. Área de círculo                 ")
    print(" e. Salir                           ")
    print("════════════════════════════════════")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione la opción que desea calcular (a-e): ")

        if opcion == 'a':
            b = float(input("Ingrese la base del triángulo: "))
            h = float(input("Ingrese la altura del triángulo: "))
            a = ObtenerAreaTriangulo(b, h)
            print("El área del triángulo es:", a)
            print("La fórmula usada es: A = (b * h) / 2")

        elif opcion == 'b':
            l = float(input("Ingrese el lado del cuadrado: "))
            a = ObtenerAreaCuadrado(l)
            print("El área del cuadrado es:", a)
            print("La fórmula usada es: A = l ^ 2")

        elif opcion == 'c':
            b = float(input("Ingrese la base del rectángulo: "))
            h = float(input("Ingrese la altura del rectángulo: "))
            a = ObtenerAreaRectangulo(b, h)
            print("El área del rectángulo es:", a)
            print("La fórmula usada es: A = b * h")

        elif opcion == 'd':
            r = float(input("Ingrese el radio del círculo: "))
            a = ObtenerAreaCirculo(r)
            print("El área del círculo es:", a)
            print("La fórmula usada es: A = π * r^2")

        elif opcion == 'e':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")

        continuar = input("¿Quieres realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()

X = 0
Y = 0

def mostrar_texto_inicial():
    print("══════════════════════════════════════════════")
    print("            Semana No. 12: Ejercicio 2        ")
    print("══════════════════════════════════════════════")

def mover_hacia_arriba():
    global Y
    Y += 1

def mover_hacia_abajo():
    global Y
    Y -= 1

def mover_hacia_la_derecha():
    global X
    X += 1

def mover_hacia_la_izquierda():
    global X
    X -= 1

def mostrar_menu():
    while True:
        print("══════════════════════════════════════════════")
        print("                    Menú                     ")
        print("════════════════════════════════════════════")
        print(" a. Sube                                      ")
        print(" b. Baja                                      ")
        print(" c. Izquierda                                 ")
        print(" d. Derecha                                   ")
        print(" e. Salir                                     ")
        print("═════════════════════════════════════════════")

        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            mover_hacia_arriba()
        elif opcion == "b":
            mover_hacia_abajo()
        elif opcion == "c":
            mover_hacia_la_izquierda()
        elif opcion == "d":
            mover_hacia_la_derecha()
        elif opcion == "e":
            print("══════════════════════════════════════════════")
            print(" Coordenadas finales del personaje:", X, ",", Y)
            print("══════════════════════════════════════════════")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def main():
    mostrar_texto_inicial()
    mostrar_menu()

if __name__ == "__main__":
    main()
