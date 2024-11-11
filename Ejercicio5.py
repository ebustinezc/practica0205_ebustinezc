# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus valores al cuadrado.
def cuadrado(numero):
    """Función que recibe unos números y los devuelve al cuadrado
    Parámetros:
        -n: lista de los números
    Salida:
        Lista de los números al cuadrado"""
    cuadrado = []
    numero = numero.split()
    for x in range(len(numero)):
        cuadrado.append(int(numero[x]) ** 2)
    return cuadrado
numero = input("Dime una lista de números separados por espacios:")
print(cuadrado(numero))