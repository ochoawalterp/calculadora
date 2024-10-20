def sumaAvanzada(valores):
   # Obtener la entrada del usuario


    # Separar los números usando el signo +
    numeros = valores.split('+')

    # Inicializar la suma
    resultado = 0

    # Sumar los números usando un bucle for
    for num in numeros:
        resultado += int(num)

    # Mostrar el resultado
    return resultado
