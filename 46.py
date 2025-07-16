import random
numero_secreto = random.randint(1, 100)
noAdivinado = True

def rangoCorrecto(num):
    minimo=1
    maximo=100
    return minimo>num or num>maximo

while noAdivinado:
    numeroIngresado = int(input("Adivina el número (entre 1 y 100): "))
    if rangoCorrecto(numeroIngresado):
        print("Por favor, ingresa un número entre 1 y 100.")
        continue
    if numeroIngresado < numero_secreto:
        print("El número secreto es mayor.")
    if numeroIngresado > numero_secreto:
        print("El número secreto es menor.")
    if numeroIngresado == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        noAdivinado = False