# Desarrollo de funciones
def operar(a, b, c):
    raiz = (b ** 2) - (4 * a * c)
    if raiz < 0:
        print('Error, la raiz es negativa.')
    else:
        print('x1 = %.2f' % ((-b + (raiz ** (1/2))) / (2 * a)))
        print('x2 = %.2f' % ((-b - (raiz ** (1/2))) / (2 * a)))

# Entrada
while True:
    a = float(input('Ingrese un valor distinto de cero para A: '))
    if a > 0:
        break
    else:
        print('Error, el valor debe ser mayor a cero.\n')

b = float(input('Ingrese el valor de B: '))
c = float(input('Ingrese el valor de C: '))

#Proceso y salida
operar(a, b, c)