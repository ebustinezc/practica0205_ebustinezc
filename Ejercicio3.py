# Escribir una función que calcule el área de un círculo y otra 
# que calcule el volumen de un cilindro usando la primera función.
def area_circulo(radio):
    """Función que calcula el área de un círculo
    Parámetros:
        -r: radio del círculo
    Salida:
        Área del círculo"""
    import math
    return (math.pi * radio ** 2)
def volumen_cilindro(altura):
    """Función que calcula el volumen de un cilindro
    Parámetros:
        -h: altura del cilindro
    Salida:
        Volumen del cilindro"""
    return (area_circulo(radio) * altura)
radio = float(input("Dime el radio:"))
altura = float(input("Dime la altura:"))
print("El área del círculo es: {}. Y el volumen del cilindro es: {}".format(area_circulo(radio), volumen_cilindro(altura)))