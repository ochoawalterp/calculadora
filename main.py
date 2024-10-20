from sumar import suma
from resta import resta
from dividir import division
from multiplicacion import multiplicacion
from suma_avanzada import sumaAvanzada
from menu import mostrarMenu
def calculadora():
    while True:
        mostrarMenu()
        try:
            opcion = int(input("Hola ingresa la opcion que desees procesar: ")) 
        except:
            print("Ingresa un número valido")
            continue  
        if opcion == 6:

            print("\n***Bye***")
            break
        if opcion in [1,2,3,4]:               
            try:
                primerNumero = int(input("Ingresa el primer valor: "))
                segundoNumero = int(input("Ingresa el segundo valor: "))
            except ValueError:
                print("Ingrese números validos")         
                continue       
            if opcion == 1:
                print("\n****SUMA****")
                resultado = suma(primerNumero, segundoNumero)
                print(f"Total: {primerNumero} + {segundoNumero} = {resultado}\n")
            elif opcion == 2:
                print("\n****RESTA****")
                resultado = resta(primerNumero, segundoNumero)
                print(f"Total: {primerNumero} - {segundoNumero} = {resultado}\n")

            elif opcion == 3:
                print("\n****MULTIPLICACION****")
                resultado = multiplicacion(primerNumero, segundoNumero)
                print(f"Total: {primerNumero} * {segundoNumero} = {resultado}\n")
            elif opcion == 4:
                print("\n****DIVIDIR****")
                resultado = division(primerNumero, segundoNumero)
                print(f"Total: {primerNumero} / {segundoNumero} = {resultado}\n")

        elif opcion == 5:
            valores = input("Ingresa los valores separados de + ejemplo 5+3+5+2: ")
            print("\n****SUMA AVANZADA****")
            resultado = sumaAvanzada(valores)
            print(f"Total: {valores} = {resultado}\n")
        else:
            print("Ingres un valor o un formato valido")

calculadora()