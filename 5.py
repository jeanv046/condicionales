precio = float(input('Digita el precio del Carro y el Terreno: '))
incterreno = int(input('Digita el incremento anual del terreno: %'))
devcarro = int(input('Digita la devaluacion anual del carro: %'))


incremento = (((precio * incterreno)/ 100)*3)/2
decremento = ((precio * devcarro)/100)*3

print(f'La devaluacion del carro en 3 años es de $ {decremento}')

if decremento < incremento:
    print('Es buena idea comprar el carro.')
else:
    print('No es buena idea la compra del carro.')


