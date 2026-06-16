# 2. menu_interactivo.py

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
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Saliendo del programa de Calculadora. Hasta pronto...")
                break
            case _:
                print("¡opción NO VÁLIDA!")
                break