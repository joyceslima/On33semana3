try:
    numero1 = 10
    numero2 = 2
    resultado = numero1/numero2
    print(f'O resultado é {resultado}')
except ZeroDivisionError:
    print('Segundo número não pode ser zero')
else:
    print('Divisão realizada com sucesso')
finally:  
    print('Fim da Divisão')          