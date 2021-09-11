monto = float(input('Cual es el monto de la finanza: '))

if monto > 50000:
    total = (monto * (2 / 100))
    print(f'Usted tiene un monto de {monto}, y sus cuotas son de {total}')
else:
    total = (monto * (3 / 100))
    print(f'Usted tiene un monto de {monto}, y sus cuotas son de {total}')