import sys
import time

inicio = time.time()
def calculadora():
    print("Esta calculadora utiliza la formula de Harris-Benedict")
    print("Sirve para calcular la cantidad de calorias necesarias para ti")
    print("Esto lo hace con base a tu genero, edad, estatura y peso")
    genero = input("Cual es tu genero? (H/M) ")
    if genero == "H" :
        edad = int(input("Cual es tu edad: "))
        estatura = int(input("Cual es tu estatura en cm: "))
        peso = int(input("Cual es tu peso en kg: "))
        resultado = (66.47 + (13.75 * peso) + (5 * estatura) - (6.74 * edad))
        print(f"Base a tus datos, deberias de consumir {resultado:.2f} calorias al dia")
    elif genero == "M":
        edad = int(input("Cual es tu edad: "))
        estatura = int(input("Cual es tu estatura en cm: "))
        peso = int(input("Cual es tu peso en kg: "))
        resultado = (655.1 + (9.56 * peso) + (1.85 * estatura) - (4.68 * edad))
        print(f"Base a tus datos, deberias de consumir {resultado:.2f} calorias al dia")
calculadora()
final = time.time()
total = final - inicio
print(f"El tiempo que toma a la funcion ejecutarse fue de {total:.2f} segundos")
memoria = sys.getsizeof(calculadora)
print(f"La cantidad de memoria utilizada fue de {memoria:.2f} bytes")