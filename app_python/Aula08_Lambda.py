#lambda (função anonima) consegue simplificar funções que consegue se resolver em apenas uma linha
#funções mais complexas não funciona.

#exemplo1: contador de letras
contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'ovelha', 'coelho']
print(contador_letras(lista_animais))
#FIM DO CODIGO

#exemplo2: soma
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(2, 10))

#função dicionario

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b}
print(type(calculadora))
soma = calculadora['soma']
# é o mesmo que: soma = lambda a, b: a + b
multiplicacao = calculadora ['multiplicacao']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicacao(10, 2)))