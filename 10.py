num1 = float(input('Digita un numero a: '))
num2 = float(input('Digita un numero b: '))
num3 = float(input('Digita un numero c: '))

if num1 > num2 and num1 > num3:
    print(f'El numero mayor es {num1}')
elif num2 > num1 and num2 > num3:
    print(f'El numero mayor es {num2}')
elif num3 > num1 and num3 > num2:
    print(f'El numero mayor es {num3}')
else:
    print('Todos son iguales.')