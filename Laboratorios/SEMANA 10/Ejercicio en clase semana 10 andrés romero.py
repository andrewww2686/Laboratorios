print("Semana No.10: Ejercicio 1")


mes=int(input("Ingrese un numero del mes 1-12"))
if mes < 1 or mes >12:
    print("Errror:el numero debe de estar entre 1 y 12")

else:
    if mes==1:
        print("Mes: Enero")
    elif mes==2:
        print("Mes:Febrero")
    elif mes==3:
        print("Mes:Marzo")
    elif mes==4: 
        print("Mes:Abril")
    elif mes==5:
        print("Mes:Mayo")
    elif mes==6:
        print("Mes:Junio")
    elif mes==7:
        print("Mes:Julio")
    elif mes==8:
        print("Mes:Agosto")
    elif mes==9:
        print("Mes:Septiembre")
    elif mes==10:
        print("Mes:Octubre")
    elif mes==11:
        print("Mes:Noviembre")
    elif mes==12:
        print("Mes:Diciembre")


#EJERCICIO 2
print("Semana No.10: EJERCICIO 2")
a=int(input("Ingrese variable A: "))
b=int(input("Ingrese variable B: "))
c=int(input("Ingrese variable C: "))

if a>b:
    if a>c:
        print("el mayor es",a)
    else:
        if a==c:
         print("los mayores son",a,"y",c)
        else:
         print("el mayor es",c)
else:
    if a==b:
        if a>c:
            print("los mayores son",a,"y",b)
        else: 
            if a==c:
                print("los numeros son iguales")   
            else:
                print("el mayor es",c)   
    else:
        if b>c:
            print("el mayor es",b)   
        else:
            if b==c:
                print("los mayores son",b,"y",c)  
            else:
                print("el mayor es",c) 

#Actividad 3
                print (" Ejercicio 3")
dia = int(input("Introduce el día de nacimiento (1-31): "))
mes = int(input("Introduce el mes de nacimiento (1 a 12): "))

signo= ""

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo= "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo= "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo= "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo= "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo= "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo= "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo= "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo= "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo= "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo= "Capricornio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo= "Acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo= "Piscis"
else:
    signo= "Fecha no válida"

print("tu signo del zodiaco es",signo)
    



