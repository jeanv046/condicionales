monto = int(input('Cuanto es el monto: '))

if monto > 500000:
    inversion = (monto * (55 / 100))
    prestamo = ( monto * (30 / 100))
    presfabrica = (monto *(15 / 100))
    interes = (presfabrica * (20 / 100))
    print(f'La cantidad a invertir es ${inversion}, el prestamo al banco es ${prestamo}, ')
    print(f'el prestamo a la fabrica es ${presfabrica}, y el interes del prestamo a la fabrica es ${interes}')
elif monto < 500000:
    inversion = (monto * (70 / 100))
    presfabrica = (monto *(30 / 100))
    interes = (presfabrica * (20 / 100))
    print(f'La cantidad a invertir es ${inversion}, el prestamo a la fabrica es ${presfabrica},  ')
    print(f'y el interes del prestamo a la fabrica es ${interes}')