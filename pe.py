from sumar import suma
from resta import resta
from dividir import division
from multiplicacion import multiplicacion
from suma_avanzada import sumaAvanzada

def calculadora():
    validar = True
    print("------------------------------------------------------")
    while validar:
        print("Binvenido a Mi calculadora")
        print("Opcion 1: Sumar")
        print("Opcion 2: Restar")
        print("Opcion 3: Multiplicar")
        print("Opcion 4: Dividir")
        print("Opcion 5: Suma Avanzada")    
        print("Opcion 6: Salir")

        opcion = int(input("Hola ingresa la opcion que desees procesar: "))

        if opcion !=5:
            if opcion != 6:
                primerNumero = int(input("Ingresa el primer valor: "))  
                segundoNumero = int(input("Ingresa el segundo valor: "))
            else:
                validar = False
            if opcion == 1:
                print("\n****SUMA****")
                resultado = suma(primerNumero, segundoNumero)
                print(f"Total: {primerNumero} + {segundoNumero} = {resultado}\n")
                print("------------------------------------------------------")
            elif opcion == 2:
                print("\n****RESTA****")
                resultado = resta(primerNumero, segundoNumero)
                print(f"Total: {primerNumero} - {segundoNumero} = {resultado}\n")
                print("------------------------------------------------------")
            elif opcion == 3:
                print("\n****MULTIPLICACION****")
                resultado = multiplicacion(primerNumero, segundoNumero)
                print(f"Total: {primerNumero} * {segundoNumero} = {resultado}\n")
                print("------------------------------------------------------")
            elif opcion == 4:
                print("\n****DIVIDIR****")
                resultado = division(primerNumero, segundoNumero)
                print(f"Total: {primerNumero} / {segundoNumero} = {resultado}\n")
                print("------------------------------------------------------")


            elif opcion == 6:
                print("\n***Bye*****")
                validar = False
        elif opcion == 5:
            valores = input("Ingresa los valores separados de + ejemplo 5+3+5+2: ")
            print("\n****SUMA AVANZADA****")
            resultado = sumaAvanzada(valores)
            print(f"Total: {valores} = {resultado}\n")
            print("------------------------------------------------------")



calculadora()