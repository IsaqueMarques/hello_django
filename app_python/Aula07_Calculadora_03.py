# Calculadora 02
# Classe com resultado pré definido.

class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b
    def subtracao(self, a, b):
        return a - b
    def multiplicacao(self, a, b):
        return self.a * self.b
    def divisao(self, a, b):
        return self.a / self.b



if __name__ == 'main':
    
    calculadora = Calculadora()

    print('       Soma')
    a = int(input('entre com um numero: '))
    b = int(input('Entre com um numero: '))

    print('Resultado:', calculadora.soma(a, b))

    print('       Subtração')
    a = int(input('entre com um numero: '))
    b = int(input('Entre com um numero: '))

    print('Resultado:', calculadora.subtracao(a, b))







