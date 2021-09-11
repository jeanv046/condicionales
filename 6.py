numcompu = int(input('Cuantas computadoras comprara: '))
valorcompu = 11000

if numcompu > 0 and numcompu < 5 :
    valor = (numcompu * valorcompu)
    descuento = (valor * (10 / 100))
    total = valor - descuento
    print(f'Hola por tu compra de {numcompu} computadores te damos')
    print(f'un descuento de ${descuento} en tu compra, tienes que pagar ${total} ')
elif numcompu >= 5 and numcompu < 10:
    valor = (numcompu * valorcompu)
    descuento = (valor * (20 / 100))
    total = valor - descuento
    print(f'Hola por tu compra de {numcompu} computadores te damos')
    print(f'un descuento de ${descuento} en tu compra, tienes que pagar ${total} ')
elif numcompu > 10:
    valor = (numcompu * valorcompu)
    descuento = (valor * (40 / 100))
    total = valor - descuento
    print(f'Hola por tu compra de {numcompu} computadores te damos')
    print(f'un descuento de ${descuento} en tu compra, tienes que pagar ${total} ')
else:
    print('Digita un numero mayor que 0')