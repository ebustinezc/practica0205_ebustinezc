# Escribir una función a la que se le pase una cadena <nombre> 
# y muestre por pantalla el saludo ¡hola <nombre>!.
def saludo(nombre):
    '''Funcion que saluda
    Parametros:
        -nombre:Nombre de la persona a saludar
    salida:
        saludo con el nombre de la persona'''
    
    return('¡Hola {}!'.format(nombre))
#nombre = input('Dime tu nombre:')
print(saludo('Bustin'))