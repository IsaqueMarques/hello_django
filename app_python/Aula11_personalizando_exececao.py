class Error(Exception):
    pass
class ImputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        # if = a se
        if x > 10:
            raise ImputError('Nota não pode ser maior que 10')
        # elif é ultilizado caso o se não solucione.
        elif x < 0:
            raise ImputError('Nota não pode ser menor que 0')
        elif x <= 10:
            raise ImputError('Obrigado pela confirmação :)')
        break
    except ValueError:
        print('Valor invalido. Deve-se digitar apenas numeros.')

    except ImputError as ex:
        print(ex)
    # OU
    #except ImputError:
        #print('Nota não pode se maior que 10')