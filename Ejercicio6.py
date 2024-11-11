# Escribir una función que convierta un número decimal en binario 
# y otra que convierta un número binario en decimal.
def binario_a_decimal(numero):
    """Función que convierte un Nº binario a decimal
    Parámetro:
        -n: Nº en binario
    Salida:
        Nº en decimal"""
    d = 0
    numero = list(numero)
    numero.reverse()
    for x in range(len(numero)):
        d = d + (int(numero[x]) * 2 ** x)
    return "Tú Nº en decimal es", d

def decimal_a_binario(m):
    """Función que convierte un Nº decimal a binario
    Parámetro:
        -m: Nº en decimal
    Salida:
        Nº en decimal"""
    b = []
    while m > 0:
        b.append(str(m % 2))
        m //= 2
    b.reverse()
    return ''.join(b)
    
n = input("Dime un Nº binario:")
print(binario_a_decimal(n))
m = int(input("Dime un Nº en decimal:"))
print(decimal_a_binario(m))