def contarCaracteres(texto):
    return len(texto)

entrada = input('Digite uma palavra ou frase: ')

try:
    caracteres = contarCaracteres(entrada)
    print(f'A string {entrada}, tem {caracteres} caracteres')

except:
    print('Erro, digite uma palavra ou frase')    