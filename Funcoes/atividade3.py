def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

entrada = input('Digite a temperatura em graus Celsius: ')

try:
    celsius = float(entrada)
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f'A temperatura da {celsius} C corresponde a {fahrenheit} F')
except:
    print('Erro, digite um número válido')    