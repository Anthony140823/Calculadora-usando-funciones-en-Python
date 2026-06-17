# 5. division.py
def dividir():
    valor1 = float(input("Dame el valor 1: "))
    valor2 = float(input("Dame el valor 2: "))
    
    if (valor2 != 0):
        print(f"El resultado de la división es: {valor1 / valor2:.2f}\n")
    else:
        print("¡Imposible dividir entre 0!\n")