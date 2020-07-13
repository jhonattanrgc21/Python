# Deaarrollo de funciones
def digito(a):
    if a == '0' or a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8' or a == '9':
        return True
    else:
        return False

# Entrada
while True:
    letra = input('Ingrese un caracter: ')
    if len(letra) < 2:
        break
    else:
        print('Error, debe ingresar un solo caracter.')

# Proceso y salida
if digito(letra):
    print('El caracter ingresado es un digito entre 0 y 9')
else:
    print('El caracter ingresado no es un digito entre 0 y 9')