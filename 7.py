
costo = float(input('Cuanto cuesta su aparato: '))
marca = input('Que marca es el aparato: ')

if  costo > 2000 and marca == 'NOSY' or marca == 'nosy' or marca == 'Nosy':
    descuento = (costo *(15 / 100))
    valor = costo - descuento
    iva = (valor * (16 / 100))
    valor = valor + iva
    print(f'Usted compro su estéreo marca {marca} le otorga un 5% dsct + 10% dsct de la tienda.')
    print(f'El total a pagar seria ${valor}')
elif costo > 2000:
    descuento = (costo *(10 / 100))
    valor = costo - descuento
    iva = (valor * (16 / 100))
    valor = valor + iva
    print(f'Usted compro su estéreo marca {marca} le otorga 10% dsct de la tienda.')
    print(f'El total a pagar seria ${valor}')
elif costo < 2000 and costo >0:
    iva = (costo * (16 / 100))
    valor = costo + iva
    print(f'Usted compro su estéreo marca {marca} el total a pagar seria ${valor} ')