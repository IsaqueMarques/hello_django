lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 3
    numero = lista[1]


#encadeamento de exceção
except ZeroDivisionError:
    print('Não é possivel realizar divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre nenhuma exceção')
#caso haja algum erro o no processo o finally fecha o arquivo que foi aberto.
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()