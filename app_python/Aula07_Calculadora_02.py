# Calculadora 02
# Classe com resultado definido

class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b
    def subtracao(self):
        return self.a - self.b
    def multiplicacao(self):
        return self.a * self.b
    def divisao(self):
        return self.a / self.b


if __name__ == 'main':
    print('       Calculadora')
    num1 = int(input('entre com um numero: '))
    num2 = int(input('Entre com um numero: '))
    Calculadora = Calculadora(num1, num2)

    print('SOMA:', Calculadora.soma())
    print('DIVISÃO:', Calculadora.divisao())
    print('SUBTRAÇÃO:', Calculadora.subtracao())
    print('MULTIPLICAÇÃO:', Calculadora.multiplicacao())

