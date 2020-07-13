# Entrada
l = list()
n = int(input('Ingrese el valor de N: '))

# Proceso
for i in range(n):
    l.append(int(input('Numero %d: ' % (i + 1))))


# Salida
print('\nLa suma de los elementos es: ', sum(l))
l.clear()