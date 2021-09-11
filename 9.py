num1 = float(input('Digita un numero: '))
num2 = float(input('Digita un numero: '))

if num1 == num2:
    resultado = num1 * num2
    print(f'El resultado es {resultado}')
elif num1 > num2:
    resultado = num1 - num2
    print(f'El resultado es {resultado}')
elif num1 < num2:
    resultado = num1 + num2
    print(f'El resultado es {resultado}')