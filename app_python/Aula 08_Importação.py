from Aula07_Televisao import Televisao
from Aula07_Calculadora_03 import Calculadora
from Aula08_contador_letras import contador_letras, teste
calculadora = Calculadora()

print('Calculadora      Operação = SOMA')
a = int(input('entre com um numero: '))
b = int(input('Entre com um numero: '))

print('Resultado:', calculadora.soma(a, b))

televisao = Televisao()
print ('Televisão')
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

print('Contador de letras')
lista = ['cachorro', 'gato', 'coelho']
total_letras = contador_letras(lista)
print('total de letras por palavras de lista: {}' .format(total_letras))
print(teste())
