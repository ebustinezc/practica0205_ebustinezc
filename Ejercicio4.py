# Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def media(numero):
    """Función que calcula la media de una serie de números
    Parámetros:
        -Lista de Números
    Salida:
        Media de todos los números introducidos"""
    media = 0
    numero = numero.split()
    for x in numero:
        media = media + int(x)
    media = media / len(numero)
    return("La media es: {}".format(media))
numero = input("Dime una serie de números separados por espacios:")
print(media(numero))