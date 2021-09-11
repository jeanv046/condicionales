
ganancias = float(input('Cuales son las ganancias diarias de la empresa: '))


suma = 0
for x in range(5):
    contaminacion = int(input(f'Dia {x + 1}. Digita la contaminacion:  '))
    suma = suma + contaminacion

total = suma / 5

if total > 170:
    print('Su empresa sobre paso el limite de contaminacion.')
    decision = input('Desea detener la produccion? s/n:  ')
    if decision == 's':
        perdida = ganancias * 5
        print(f'Su perdida es de {perdida}')
    elif decision == 'n':
        perdida = (ganancias * 5) / 2
        print(f'Su perdida es de {perdida}')
    else:
        print('Digita Porfavor una opcion valida s/n')
else:
    print('No tiene ningun tipo de sanción.')