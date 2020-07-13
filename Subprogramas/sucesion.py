# Desarrollo de funciones
def sumar(n):
    acum = 0
    for i in range(n):
        acum += (i+ 1)
    return acum

# Entrada
while True:
    n = int(input('Ingrese un numero mayor a cero: '))
    if (n > 0):
        break
    else:
        print('Error, el numero debe ser mayor a 0.')

# Proceso y salida
print('Suma = ', sumar(n))