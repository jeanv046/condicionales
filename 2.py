num = int(input('Digite su numero aleatorio: '))
compra = float(input('Digite el valor de su compra: '))

if num >= 74:
    total = (compra * (20 / 100))
    print(f'Su numero fue {num}, y obtuvo un descuento de ${total}')
else:
    total = (compra * (15 / 100))
    print(f'Su numero fue {num}, y obtuvo un descuento de ${total}')