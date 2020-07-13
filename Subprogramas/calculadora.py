# Desarrollo de funciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

# Entrada
a = float(input('Ingrese el primer numero: '))
b = float(input('Ingrese el segundo numero: '))

while True:
    print('Operacion')
    print('1- Suma')
    print('2- Resta')
    print('3- Multiplicacion')
    print('4- Division')
    op = int(input('Seleccion: '))

    if op > 0 and op < 5:
        break
    else:
        print('Error, opcion invalida.\n') 

# Proceso y salida
if op == 1:
    print('%.1f + %.1f = %.1f' % (a, b, suma(a, b)))
elif op == 2:
    print('%.1f - %.1f = %.1f' % (a, b, resta(a, b)))
elif op == 3:
    print('%.1f * %.1f = %.1f' % (a, b, multiplicacion(a, b)))
else: 
    print('%.1f / %.1f = %.1f' % (a, b, division(a, b)))