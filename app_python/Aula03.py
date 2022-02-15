#Aula 03

print('Bem Vindos a plataforma de notas da Facottur, por favor informe as respectivas notas de cada bimestre.\nInforme um numero de 0 a 10')

a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Valor invalido. Digite novamente: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Valor invalido. Digite novamente: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Valor invalido. Digite novamente: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Valor invalido. Digite novamente: '))
media = (a+b+c+d)/4
print('media: {}'.format(media))
if media >= 7:
    print('Parabéns você foi aprovado')
else:
    print('Infelizmente não foi dessa vez')

print('Final do programa')


###############################
############# RNW  ############
###############################