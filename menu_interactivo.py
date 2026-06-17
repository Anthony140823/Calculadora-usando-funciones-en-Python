# 2. menu_interactivo.py

# Importación de modulos
from sumar import sumar
from restar import restar
from multiplicar import multiplicar
from division import dividir

def menu():
    while True:
        print('''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir
''')
        opcion = int(input("Escoge una opción: "))

        match(opcion):
            case 1:
                sumar()
            case 2:
                restar()
            case 3:
                multiplicar()
            case 4:
                dividir()
            case 5:
                print("Saliendo del programa de Calculadora. Hasta pronto...")
                break
            case _:
                print("¡opción NO VÁLIDA!\n")