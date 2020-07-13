import os

# Entrada
a = list()
b = list()
c = list()
t = list()

n = int(input('Ingrese el numero de empleados: '))
print('\n')

# Proceso
for i in range(n):
    print('Empleado %d' % (i + 1))
    a.append(float(input('Sueldo: ')))
    b.append(float(input('Asignaciones: ')))
    c.append(float(input('Deducciones: ')))
    t.append(a[i] + b[i] - c[i])
    os.system('clear')

# Salida
for i in range(n):
    print('Total a pagar al empleado %d: %.2f\n' % (i + 1, t[i]))

a.clear()
b.clear()
c.clear()
t.clear()